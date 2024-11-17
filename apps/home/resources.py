from import_export import resources
from .models import Employe

class EmployeResource(resources.ModelResource):
    class Meta:
        model = Employe
        fields = ('nom_em', 'prenom_em', 'sex', 'im', 'date_nais',
                  'departement__nom_dep', 'diplome__type_dip', 'categorie__num_cat',
                  'indice', 'fonction__nom_fc', 'date_PF', 'contrat__type_con',
                  'contrat__dure_con', 'cin', 'adress_em', 'num_tel')
