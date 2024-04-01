from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions, status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
from rest_framework.views import APIView
from django.db import transaction


# Create your views here.


class ProfesseursView(viewsets.ModelViewSet):
    queryset = Professeurs.objects.all()
    serializer_class = ProfesseurSerializer
        
class MatiereView(viewsets.ModelViewSet):
    queryset = Matieres.objects.all()
    serializer_class = MatiereSerializer

class SalleView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Salles.objects.all()
    serializer_class = SalleSerializer

class NiveauView(viewsets.ModelViewSet):
    queryset = Niveaux.objects.all()
    serializer_class = NiveauSerializer

class ParentsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]
    queryset = Parents.objects.all()
    serializer_class = ParentSerializer

class NoteView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer


class EleveUploadExcelView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        try:
            file_obj = request.data.get("excel")
            classe = request.data.get("classe")
            print(f"voici {classe}")

            if not file_obj:
                return Response({'message': 'Vous navez pas chargé de fichier.'}, status=status.HTTP_400_BAD_REQUEST)

            df = pd.read_excel(file_obj)
            if not df.isna().any().any():
                for _, row in df.iterrows():
                    date_naissance = row.get('date_naissance', None)

                    if isinstance(date_naissance, pd.Timestamp):
                        date_naissance_iso = date_naissance.strftime('%Y-%m-%d')
                    elif isinstance(date_naissance, str):
                        date_naissance_iso = date_naissance

                    tuteur_data = {
                        'nom': row['nom_tuteur'],
                        'prenom': row['prenom_tuteur'],
                        'telephone': row['telephone_tuteur'],
                        'email': row['email_tuteur'],
                        'adresse': row['adresse_tuteur'],
                        'mot_de_passe': "pablo"
                    }

                    niveau = Niveaux.objects.get(libelle__iexact=classe)

                    with transaction.atomic():
                        tuteur, created = Parents.objects.get_or_create(email=row['email_tuteur'], defaults=tuteur_data)

                        eleve_data = {
                            'matricule': row['matricule'],
                            'nom': row['nom'],
                            'prenom': row['prenom'],
                            'date_naissance': date_naissance_iso,
                            'lieu_naissance': row['lieu_naissance'],
                            'adresse': row['adresse'],
                            'telephone': row['telephone'],
                            'niveau': niveau.id,
                            'tuteur': tuteur.id
                        }

                        serializer = EleveSerializer(data=eleve_data)
                        serializer.is_valid(raise_exception=True)
                        serializer.save()

                return Response({'message': 'Téléchargement réussi'})
            else:
                colonnes_avec_vide = df.columns[df.isnull().any()].tolist()
                return Response({'message': f'Les colonnes {colonnes_avec_vide} sont manquantes dans le fichier Excel.'}, status=status.HTTP_400_BAD_REQUEST)
        except pd.errors.EmptyDataError:
            return Response({'message': 'Le fichier Excel est vide.'}, status=status.HTTP_400_BAD_REQUEST)
        except pd.errors.ParserError as e:
            return Response({'message': f'Erreur lors de la lecture du fichier Excel : {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': f'Erreur inattendue : {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ElevesView(viewsets.ModelViewSet):
    
    queryset = Eleves.objects.all()
    serializer_class = EleveSerializer
    permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]

    def list(self, request, *args, **kwargs):
        niveau = request.headers.get('niveau', None)

        if niveau:
            niveau_classe = Niveaux.objects.get(libelle__iexact=niveau)
            eleves_queryset = Eleves.objects.filter(niveau=niveau_classe)
        else:
            eleves_queryset = Eleves.objects.all()

        serializer = self.get_serializer(eleves_queryset, many=True)
        return Response(serializer.data)

     

        
        


