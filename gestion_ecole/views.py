from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions, status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
from rest_framework.views import APIView
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse

# Create your views here.

def get_total_eleves(request):
    total_eleves = Eleves.objects.count()
    return JsonResponse({'count': total_eleves})

class ProfesseursView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Professeurs.objects.all()
    serializer_class = ProfesseurSerializer
        
class MatiereView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Matieres.objects.all()
    serializer_class = MatiereSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['niveau']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            libelle = serializer.validated_data.get('libelle')
            coeficient = serializer.validated_data.get('coeficient')
            niveau = serializer.validated_data.get('niveau')

            matiere_coef = Matieres.objects.filter(libelle__iexact=libelle, coeficient=coeficient)
            print(matiere_coef)

            if matiere_coef:
                matiere = Matieres.objects.get(libelle__iexact=libelle, coeficient=coeficient)
                matiere.niveau.add(niveau)
                return Response({'message': 'le niveau à bien été ajouté'},status=status.HTTP_201_CREATED)
            else:
                # niveau_assoicie = Niveaux.objects.get(id=niveau)
                # serializer.save(niveau=niveau_assoicie)
                news_matiere = Matieres.objects.create(libelle=libelle, coeficient=coeficient)
                news_matiere.niveau.add(niveau)
                return Response(serializer.data, status=status.HTTP_201_CREATED)



class SalleView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Salles.objects.all()
    serializer_class = SalleSerializer

class NiveauView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Niveaux.objects.all()
    serializer_class = NiveauSerializer

class ParentsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Parents.objects.all()
    serializer_class = ParentSerializer

class NoteView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eleve']


class EleveUploadExcelView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            file_obj = request.data.get("file")
            classe = request.headers.get('niveau', None)
            print(f"voici {classe}")

            if not file_obj or classe == None:
                return Response({'message': 'Vous navez pas chargé de fichier. ou indiqué la classe'}, status=status.HTTP_400_BAD_REQUEST)

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

                return Response({'message': 'Téléchargement réussi'}, status=status.HTTP_200_OK)
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
    # permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]

    def get_serializer_class(self):
        if self.action in ['create']:
            return EleveCreateSerializer
<<<<<<< HEAD
        if self.action in ['update', 'partial_update', 'list', 'retrieve']:
=======
        if self.action in ['update', 'partial_update', 'list', 'retreive']:
>>>>>>> 8b225fb43be9070511e0619a7f04b24546b9a3ff
            return EleveSerializer
        return EleveCreateSerializer  # Par défaut
        
    def list(self, request, *args, **kwargs):
        niveau = request.headers.get('niveau', None)

        if niveau:
            niveau_classe = Niveaux.objects.get(libelle__iexact=niveau)
            eleves_queryset = Eleves.objects.filter(niveau=niveau_classe)
            serializer = self.get_serializer(eleves_queryset, many=True)
            response_data = {
            'count': eleves_queryset.count(),
            'results': serializer.data
             }
            return Response(response_data, status=status.HTTP_200_OK  )
        else:
            return Response({"message": "Le niveau n'est pas spécifié dans l'en-tête de la requête."}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        niveau = request.headers.get('niveau', None)
        
        if niveau:
            try:
                niveau_classe = Niveaux.objects.get(libelle__iexact=niveau)
                serializer = self.get_serializer(data=request.data)

                if serializer.is_valid():
                    # récupération info parent dans le serializer et enrgistrement du parent 
                    nom = serializer.validated_data.pop('parent_nom')
                    prenom = serializer.validated_data.pop('parent_prenom')
                    telephone = serializer.validated_data.pop('parent_telephone')
                    email = serializer.validated_data.pop('parent_email')
                    adresse = serializer.validated_data.pop('parent_adresse')
                    parent, created = Parents.objects.get_or_create(nom=nom, prenom=prenom, telephone=telephone,
                                                                    email=email, adresse=adresse)
                
                    # donnation du matricule à l'élève
                    matricule = f"{niveau_classe.libelle}-{nom}"
                    serializer.save(matricule=matricule, niveau=niveau_classe, tuteur=parent)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            except Niveaux.DoesNotExist:
                return Response({"message": "Le niveau spécifié n'existe pas."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Le niveau n'est pas spécifié dans l'en-tête de la requête."}, status=status.HTTP_400_BAD_REQUEST)

     

        
        


