from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contrat
from .models import Avancement, Affectation
from datetime import date, timedelta

@receiver(post_save, sender=Contrat)
def avancer_grade_employe(sender, instance, **kwargs):
    avancement = Avancement(employee=instance.employe, date_effective=instance.date_fin_contrat)
    avancement.avance_employee_grade()
    avancement.save()



@receiver(post_save, sender=Affectation)
def avancer_grade_enseignant(sender, instance, **kwargs):
    if instance.enseignant:
        date_actuelle = date.today()  # Obtient la date actuelle
        date_debut_service = instance.enseignant.date_PF  # Date de début de service de l'enseignant

        # Vérifie si 2 ans se sont écoulés depuis la date de début de service
        deux_ans_plus_tard = date_debut_service + timedelta(days=730)  # 2 ans représentent 730 jours

        if date_actuelle >= deux_ans_plus_tard:
            avancement = Avancement(teacher=instance.enseignant, date_effective=date_actuelle)
            avancement.avance_teacher_grade()
            avancement.save()

