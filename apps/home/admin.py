from django.contrib import admin

from django.contrib.auth.models import Permission



from .models import (
    Categorie,
    Diplome,
    Contrat,
    Conge,
    TypeConge,
    Grade,
    Employe,
    Situation,
    Domaine,
    Departement,
   
    Fonction,
    Mention,
    Corps,
    Enseignant,
    Affectation,
)

# Register your models here.

admin.site.register(Permission)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('num_cat',)

@admin.register(Diplome)
class DiplomeAdmin(admin.ModelAdmin):
    list_display = ('type_dip', 'description')

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ('type_con', 'dure_con')

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ('date_debut', 'date_fin', 'type_conge', 'employe', 'enseignant')

@admin.register(TypeConge)
class TypeCongeAdmin(admin.ModelAdmin):
    list_display = ('nom_tc', 'nb_jour')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('num_classe', 'num_echellon')

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom_em', 'prenom_em', 'age', 'sex', 'im', 'date_nais', 'date_PF', 'cin', 'adresse', 'num_tel', 'indice', 'categorie', 'diplome', 'contrat', 'situation', 'domaine', 'departement', 'grade', 'fonction')

@admin.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ('type_st',)

@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    list_display = ('nom_dom', 'description')

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom_dep', 'description')




@admin.register(Fonction)
class FonctionAdmin(admin.ModelAdmin):
    list_display = ('nom_fc',)

@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('nom_me', 'description')

@admin.register(Corps)
class CorpsAdmin(admin.ModelAdmin):
    list_display = ('nom_cr', 'description')

# @admin.register(Enseignant)
# class EnseignantAdmin(admin.ModelAdmin):
#     list_display = ('nom_en', 'prenom_en', 'age', 'sex', 'im', 'date_nais', 'date_PF', 'grade', 'diplome', 'corps', 'situation')


class AffectationAdmin(admin.ModelAdmin):
    list_display = ('date_aff', 'motif', 'employe')

admin.site.register(Affectation, AffectationAdmin)

    