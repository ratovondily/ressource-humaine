from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import schedule
import time
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



from datetime import datetime, date
from django.dispatch import receiver
from django.db.models.signals import post_save

from datetime import timedelta










# Assurez-vous de créer d'autres autorisations pour d'autres vues (ajout, modification, suppression) si nécessaire.

# Assurez-vous de créer d'autres autorisations pour ajouter, modifier et supprimer si nécessaire.


class Categorie(models.Model):
    num_cat = models.CharField(max_length=3)

    def num_cat_to_roman(self):
        # Dictionnaire pour mapper les chiffres arabes aux chiffres romains
        roman_numerals = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            # Ajoutez plus de correspondances ici si nécessaire
        }

        # Assurez-vous que le champ `num_cat` contient une valeur numérique valide
        try:
            num = int(self.num_cat)
        except ValueError:
            return self.num_cat  # Si ce n'est pas un nombre, renvoyez la valeur d'origine

        # Vérifiez si le nombre est dans le dictionnaire
        if num in roman_numerals:
            return roman_numerals[num]

        return self.num_cat  # Si le nombre n'a pas de correspondance, renvoyez la valeur d'origine

    def __str__(self):
        return self.num_cat_to_roman()



class Diplome(models.Model):
    type_dip = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)




    

class Contrat(models.Model):
    type_con = models.CharField(max_length=30)
    dure_con = models.IntegerField(null=False)


def validate_digit_1_to_3(value):
    if len(value) != 1 or value not in ('1', '2', '3'):
        raise ValidationError('Ce champ doit contenir les chiffres 1, 2 ou 3.')

class Grade(models.Model):
    num_classe = models.CharField(max_length=1, validators=[validate_digit_1_to_3])
    num_echellon = models.CharField(max_length=1, validators=[validate_digit_1_to_3])
def get_grade_display(self):
    return f'{self.num_classe}C{self.num_echellon}E'
    
    




class Domaine(models.Model):
    nom_dom = models.CharField(max_length=50)
    description = models.TextField(max_length=50, null=True, blank=True)





class Departement(models.Model):
    nom_dep = models.CharField(max_length=25)
    description = models.TextField(max_length=100, null=True, blank=True)
   


    
    

def age_validator(value):
    if not 10 <= int(value) <= 99:
        raise ValidationError('L\'âge doit être composé de deux chiffres.')

def im_validator(value):
    if not value.isdigit() or len(value) != 6:
        raise ValidationError('Le numéro matricule doit contenir exactement 6 chiffres.')

def cin_validator(value):
    if not value.isdigit() or len(value) != 12:
        raise ValidationError('Le numéro CIN doit contenir exactement 12 chiffres.')

def num_tel_validator(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Le numéro de téléphone doit contenir exactement 10 chiffres.')

def indice_validator(value):
    if not value.isdigit() or len(value) != 6:
        raise ValidationError('L\'indice doit être composé de six chiffres.')



 




  


class Fonction(models.Model):
    nom_fc = models.CharField(max_length=30)

class Mention(models.Model):
    nom_me = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

class Corps(models.Model):
    nom_cr = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)

class Situation(models.Model):
    type_st = models.CharField(max_length=25)  # Exemple de champ de type CharField

    def __str__(self):
        return self.type_st



class Enseignant(models.Model):
    nom_en = models.CharField(max_length=30)
    prenom_en = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField()
    adress = models.TextField(default="Maninday")
    SEX_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    num_tel = models.CharField(max_length=10, validators=[num_tel_validator], null=True)
    cin = models.CharField(max_length=12, validators=[cin_validator], null=True, unique=True)
    indice = models.CharField(max_length=6, null=True)
    im = models.CharField(max_length=6, unique=True)  # Numéro matricule
    date_nais = models.DateField()
    date_PF = models.DateField()
    image = models.ImageField(upload_to='enseignant_images/', null=True, blank=True)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    diplome = models.ForeignKey('Diplome', on_delete=models.CASCADE)
    corps = models.ForeignKey('Corps', on_delete=models.CASCADE, null=True)
    situation = models.ForeignKey('Situation', on_delete=models.CASCADE) # Champ pour la situation
    mention = models.ForeignKey('Mention', on_delete=models.CASCADE, null=True)
    domaine = models.ForeignKey('Domaine', on_delete=models.CASCADE, null=True)
    departement = models.ForeignKey('Departement', on_delete=models.CASCADE, null=True)



    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ''
    


    def validate_im(self):
        if len(self.im) != 6 or not self.im.isdigit():
            raise ValidationError('Le numéro matricule doit contenir exactement 6 chiffres.')

    def validate_age(self):
        if not 10 <= self.age <= 99:  # Vérifie que l'âge est composé de deux chiffres.
            raise ValidationError('L\'âge doit être composé de deux chiffres.')

    def save(self, *args, **kwargs):
        self.validate_im()  # Appeler la validation du numéro matricule
        self.validate_age()  # Appeler la validation de l'âge

        # Vérifier si l'âge est de 60 ans ou plus
    


        super(Enseignant, self).save(*args, **kwargs)
    
    



    
   






class Employe(models.Model):
    nom_em = models.CharField(max_length=30)
    prenom_em = models.CharField(max_length=30, null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    adresse = models.TextField(default="Maninday") # Corrected "adress_em" to "adresse"
    sex = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    im = models.CharField(max_length=6, unique=True)
    date_nais = models.DateField()
    date_PF = models.DateField(null=True, blank=True)
    cin = models.CharField(max_length=12, unique=True)
    num_tel = models.CharField(max_length=10)
    image = models.ImageField(upload_to='employe_photos/', null=True, blank=True)
    indice = models.CharField(max_length=6)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    situation = models.ForeignKey(Situation, on_delete=models.CASCADE)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE, null=True, blank=True)
 

    class Meta:
        verbose_name = "Employé"
        verbose_name_plural = "Employés"  
    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return ''




class Affectation(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_aff = models.DateField()
    motif = models.TextField()
    n_domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    n_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    n_fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)
@receiver(post_save, sender=Affectation)
def update_employee_info(sender, instance, created, **kwargs):
    if created:  # Vérifie si c'est une nouvelle affectation
        employe = instance.employe
        employe.domaine = instance.n_domaine
        employe.departement = instance.n_departement
        employe.fonction = instance.n_fonction
        employe.save()
   
  


class TypeConge(models.Model):
    nom_tc = models.CharField(max_length=40)
    nb_jour = models.IntegerField(default=0)





class Conge(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    type_conge = models.ForeignKey(TypeConge, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True, blank=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True)
    jours_utilises = models.PositiveIntegerField(null=True, default=0)
    jours_restants = models.PositiveIntegerField(null=True, default=0)  # Ajustez la valeur par défaut

    def save(self, *args, **kwargs):
        if self.date_debut and self.type_conge:
            
            if isinstance(self.date_debut, str):
                self.date_debut = datetime.strptime(self.date_debut, '%Y-%m-%d').date()

            if isinstance(self.date_fin, str):
                self.date_fin = datetime.strptime(self.date_fin, '%Y-%m-%d').date()

            aujourdhui = date.today()

            if self.date_debut > aujourdhui:  # Si la date de début est dans le futur
                self.jours_utilises = 0
                self.jours_restants = 0
            elif self.date_fin and self.date_fin > self.date_debut:
                # Calcul des jours utilisés jusqu'à la date actuelle
                jours_utilises = (min(aujourdhui, self.date_fin) - self.date_debut).days + 1

                # Calcul des jours restants
                self.jours_utilises = jours_utilises
                self.jours_restants = self.type_conge.nb_jour - jours_utilises
            else:  # Si les dates ne sont pas valides
                self.jours_utilises = 0
                self.jours_restants = self.type_conge.nb_jour

        super().save(*args, **kwargs)





class Permission(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, null=True, blank=True)
    jours_utilises = models.PositiveIntegerField(null=True, default=0)
    jours_restants = models.PositiveIntegerField(null=True, default=0)  # Ajustez la valeur par défaut

    def save(self, *args, **kwargs):
        if self.date_debut and self.type_permission:
            
            if isinstance(self.date_debut, str):
                self.date_debut = datetime.strptime(self.date_debut, '%Y-%m-%d').date()

            if isinstance(self.date_fin, str):
                self.date_fin = datetime.strptime(self.date_fin, '%Y-%m-%d').date()

            aujourdhui = date.today()

            if self.date_debut > aujourdhui:  # Si la date de début est dans le futur
                self.jours_utilises = 0
                self.jours_restants = 0
            elif self.date_fin and self.date_fin > self.date_debut:
                # Calcul des jours utilisés jusqu'à la date actuelle
                jours_utilises = (min(aujourdhui, self.date_fin) - self.date_debut).days + 1

                # Calcul des jours restants
                self.jours_utilises = jours_utilises
                self.jours_restants = self.type_conge.nb_jour - jours_utilises
            else:  # Si les dates ne sont pas valides
                self.jours_utilises = 0
                self.jours_restants = self.type_conge.nb_jour

        super().save(*args, **kwargs)

   


