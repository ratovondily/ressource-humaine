from django import forms
from django.forms import ModelForm
from .models import Categorie
from .models import Diplome
from .models import Contrat
from .models import Conge
from .models import Permission
from .models import TypeConge
from .models import Grade
from .models import Employe
from .models import Situation
from .models import Domaine
from .models import Departement

from .models import Fonction
from .models import Mention
from .models import Corps
from .models import Enseignant

from django.core.exceptions import ValidationError

from django import forms
from .models import Affectation
from datetime import date
from .validators import date_not_in_past






class AffectationForm(forms.ModelForm):
    class Meta:
        model = Affectation
        fields = ['employe', 'date_aff', 'motif', 'n_domaine', 'n_departement', 'n_fonction']

    def __init__(self, *args, **kwargs):
        super(AffectationForm, self).__init__(*args, **kwargs)
        # Vous pouvez personnaliser les widgets ou ajouter des attributs à vos champs ici
        self.fields['employe'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_aff'].widget.attrs.update({'class': 'form-control'})
        self.fields['motif'].widget.attrs.update({'class': 'form-control'})
        self.fields['n_domaine'].widget.attrs.update({'class': 'form-control'})
        self.fields['n_departement'].widget.attrs.update({'class': 'form-control'})
        self.fields['n_fonction'].widget.attrs.update({'class': 'form-control'})

  



class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['num_cat']

        # Vous pouvez également ajouter des widgets ou des labels personnalisés si nécessaire
        widgets = {
            'num_cat': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'num_cat': 'Numéro de catégorie',
        }



class DiplomeForm(forms.ModelForm):
    class Meta:
        model = Diplome
        fields = ['type_dip', 'description']




class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'









class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['date_debut', 'date_fin', 'type_conge', 'employe', 'enseignant']

    date_debut = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[date_not_in_past]  # Ajoutez votre validation personnalisée ici
    )



class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['date_debut', 'date_fin', 'employe']

    date_debut = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        validators=[date_not_in_past]  # Ajoutez votre validation personnalisée ici
    )


class TypeCongeForm(forms.ModelForm):
    class Meta:
        model = TypeConge
        fields = ['nom_tc', 'nb_jour']




class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['num_classe', 'num_echellon']





class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # Ajoutez le champ image comme un champ d'image

    widgets = {
        'categorie': forms.Select(attrs={'class': 'form-control'}),
        'diplome': forms.Select(attrs={'class': 'form-control'}),
        'contrat': forms.Select(attrs={'class': 'form-control'}),
        'situation': forms.Select(attrs={'class': 'form-control'}),
        'domaine': forms.Select(attrs={'class': 'form-control'}),
        'departement': forms.Select(attrs={'class': 'form-control'}),
        'grade': forms.Select(attrs={'class': 'form-control'}),
        'fonction': forms.Select(attrs={'class': 'form-control'}),
    }
    # Vous pouvez également personnaliser les widgets et les étiquettes de champ ici
   




class SituationForm(forms.ModelForm):
    class Meta:
        model = Situation
        fields = '__all__' 




class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = '__all__'  # Utilisez '__all__' pour inclure tous les champs du modèle

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'  # Utilisez '__all__' pour inclure tous les champs du modèle
        








class FonctionForm(forms.ModelForm):
    class Meta:
        model = Fonction
        fields = '__all__'





class MentionForm(forms.ModelForm):
    class Meta:
        model = Mention
        fields = '__all__'





class CorpsForm(forms.ModelForm):
    class Meta:
        model = Corps
        fields = ['nom_cr', 'description']




class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'  # Utilisez tous les champs du modèle

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # Ajoutez le champ image comme un champ d'image

    widgets = {
        
        'corps': forms.Select(attrs={'class': 'form-control'}),
        'diplome': forms.Select(attrs={'class': 'form-control'}),
        'situation': forms.Select(attrs={'class': 'form-control'}),
        'domaine': forms.Select(attrs={'class': 'form-control'}),
        'departement': forms.Select(attrs={'class': 'form-control'}),
        'grade': forms.Select(attrs={'class': 'form-control'}),
        'mention': forms.Select(attrs={'class': 'form-control'}),
        
    }



class ImportExcelForm(forms.Form):
    fichier_excel = forms.FileField(label="Sélectionnez un fichier Excel")


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()





