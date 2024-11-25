from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views 



urlpatterns = [
    
    path('', views.index, name='home'),
    path('pages/', views.pages, name='pages'),
    path('logout/', views.custom_logout, name='logout'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('export_enseignants/', views.export_enseignants, name='export_enseignants'),
    path('import_excel/', views.import_excel, name='import_excel'),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:id_categorie>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id_categorie>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('diplomes/', views.liste_diplomes, name='liste_diplomes'),
    path('diplomes/ajouter/', views.ajouter_diplome, name='ajouter_diplome'),
    path('diplomes/modifier/<int:id_diplome>/', views.modifier_diplome, name='modifier_diplome'),
    path('diplomes/supprimer/<int:id_diplome>/', views.supprimer_diplome, name='supprimer_diplome'),
    path('contrats/', views.liste_contrats, name='liste_contrats'),
    path('contrats/ajouter/', views.ajouter_contrat, name='ajouter_contrat'),
    path('contrats/modifier/<int:id_contrat>/', views.modifier_contrat, name='modifier_contrat'),
    path('contrats/supprimer/<int:id_contrat>/', views.supprimer_contrat, name='supprimer_contrat'),
    path('conges/', views.liste_conges, name='liste_conges'),
    path('conges/ajouter/', views.ajouter_conge, name='ajouter_conge'),
    path('conges/modifier/<int:id_conge>/', views.modifier_conge, name='modifier_conge'),
    path('conges/supprimer/<int:id_conge>/', views.supprimer_conge, name='supprimer_conge'),

    path('permissions/', views.liste_permissions, name='liste_permissions'),
    path('permissions/ajouter/', views.ajouter_permission, name='ajouter_permission'),
    path('permissions/modifier/<int:id_permission>/', views.modifier_permission, name='modifier_permission'),
    path('permissions/supprimer/<int:id_permission>/', views.supprimer_permission, name='supprimer_permission'),

    path('typeconges/', views.liste_typeconges, name='liste_typeconges'),
    path('typeconges/ajouter/', views.ajouter_typeconge, name='ajouter_typeconge'),
    path('typeconges/modifier/<int:id_typeconge>/', views.modifier_typeconge, name='modifier_typeconge'),
    path('typeconges/supprimer/<int:id_typeconge>/', views.supprimer_typeconge, name='supprimer_typeconge'),
    path('grades/', views.liste_grades, name='liste_grades'),
    path('grades/ajouter/', views.ajouter_grade, name='ajouter_grade'),
    path('grades/modifier/<int:id_grade>/', views.modifier_grade, name='modifier_grade'),
    path('grades/supprimer/<int:id_grade>/', views.supprimer_grade, name='supprimer_grade'),
    path('employe_profile/<int:employe_id>/', views.employe_profile, name='employe_profile'),
    path('employes/', views.liste_employes, name='liste_employes'),
    path('employes/ajouter/', views.ajouter_employe, name='ajouter_employe'),
    path('employes/modifier/<int:id_em>/', views.modifier_employe, name='modifier_employe'),
    path('employes/supprimer/<int:id_em>/', views.supprimer_employe, name='supprimer_employe'),
    path('situations/', views.liste_situations, name='liste_situations'),
    path('situations/ajouter/', views.ajouter_situation, name='ajouter_situation'),
    path('situations/modifier/<int:id_st>/', views.modifier_situation, name='modifier_situation'),
    path('situations/supprimer/<int:id_st>/', views.supprimer_situation, name='supprimer_situation'),
    path('fonctions/', views.liste_fonctions, name='liste_fonctions'),
    path('fonctions/ajouter/', views.ajouter_fonction, name='ajouter_fonction'),
    path('fonctions/modifier/<int:id_fc>/', views.modifier_fonction, name='modifier_fonction'),
    path('fonctions/supprimer/<int:id_fc>/', views.supprimer_fonction, name='supprimer_fonction'),
    path('mentions/', views.liste_mentions, name='liste_mentions'),
    path('mentions/ajouter/', views.ajouter_mention, name='ajouter_mention'),
    path('mentions/modifier/<int:id_me>/', views.modifier_mention, name='modifier_mention'),
    path('mentions/supprimer/<int:id_me>/', views.supprimer_mention, name='supprimer_mention'),
    path('corps/', views.liste_corps, name='liste_corps'),
    path('corps/ajouter/', views.ajouter_corps, name='ajouter_corps'),
    path('corps/modifier/<int:id_cr>/', views.modifier_corps, name='modifier_corps'),
    path('corps/supprimer/<int:id_cr>/', views.supprimer_corps, name='supprimer_corps'),
    path('enseignant_profile/<int:enseignant_id>/', views.enseignant_profile, name='enseignant_profile'),
    
    path('enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/modifier/<int:id_en>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/supprimer/<int:id_en>/', views.supprimer_enseignant, name='supprimer_enseignant'),
    path('domaines/', views.liste_domaines, name='liste_domaines'),
    path('domaines/ajouter/', views.ajouter_domaine, name='ajouter_domaine'),
    path('domaines/modifier/<int:id_dom>/', views.modifier_domaine, name='modifier_domaine'),
    path('domaines/supprimer/<int:id_dom>/', views.supprimer_domaine, name='supprimer_domaine'),
    path('departements/', views.liste_departements, name='liste_departements'),
    path('departements/ajouter/', views.ajouter_departement, name='ajouter_departement'),
    path('departements/modifier/<int:id_dep>/', views.modifier_departement, name='modifier_departement'),
    path('departements/supprimer/<int:id_dep>/', views.supprimer_departement, name='supprimer_departement'),
    path('list_affectations/', views.list_affectations, name='list_affectations'),
    path('affectations/ajouter/', views.create_affectation, name='create_affectation'),
    path('affectations/modifier/<int:pk>/', views.update_affectation, name='update_affectation'),
    path('affectations/supprimer/<int:pk>/', views.delete_affectation, name='delete_affectation'),
    path('get_sex_data/', views.get_sex_data, name='get_sex_data'),
    path('get_age_data/', views.get_age_data, name='get_age_data'),
    path('get_dept_data/', views.get_dept_data, name='get_dept_data'),
    path('get_enseignant_info/<int:enseignant_id>/', views.get_enseignant_info, name='get_enseignant_info'),
    path('get_employee_info/<int:employe_id>/', views.get_employee_info, name='get_employee_info'),
    path('export_affectations_to_excel/', views.export_affectations_to_excel, name='export_affectations_to_excel'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)