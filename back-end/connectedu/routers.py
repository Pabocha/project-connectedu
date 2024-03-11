from rest_framework.routers import DefaultRouter
from gestion_ecole.views import *
from gestion_ecole_2.views import *

router = DefaultRouter()

# gestion_ecole
router.register('professeur', ProfesseursView, basename='professeur')
router.register('matiere', MatiereView, basename='matiere')
router.register('salle', SalleView, basename='salle')
router.register('niveau', NiveauView, basename='niveau')


# gestion_ecole_2
router.register('emploi_du_temps', EmploiDuTempView, basename='emploi_du_temps')
router.register('appreciation', AppreciationView, basename='appreciation')
router.register('annonce', AnnonceView, basename='annonce')


urlpatterns = router.urls