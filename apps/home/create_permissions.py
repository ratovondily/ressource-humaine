from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Categorie, Diplome, Contrat, Grade, Domaine, Departement, Avancement, Fonction, Mention, Corps, Situation, Enseignant, Employe, Affectation, TypeConge, Conge

class Command(BaseCommand):
    help = 'Creates necessary permissions for multiple models'

    def create_employe_permissions():
        content_type = ContentType.objects.get_for_model(Employe)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_employe',
            name='Can add Employe',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_employe',
            name='Can change Employe',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_employe',
            name='Can delete Employe',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_employe',
            name='Can view Employe',
            content_type=content_type,
        )

    if __name__ == "__main":
        create_employe_permissions()

    def create_enseignant_permissions():
        content_type = ContentType.objects.get_for_model(Enseignant)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_enseignant',
            name='Can add Enseignant',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_enseignant',
            name='Can change Enseignant',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_enseignant',
            name='Can delete Enseignant',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_enseignant',
            name='Can view Enseignant',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_enseignant_permissions()


    def create_categorie_permissions():
        content_type = ContentType.objects.get_for_model(Categorie)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_categorie',
            name='Can add Categorie',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_categorie',
            name='Can change Categorie',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_categorie',
            name='Can delete Categorie',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_categorie',
            name='Can view Categorie',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_categorie_permissions()



    def create_diplome_permissions():
        content_type = ContentType.objects.get_for_model(Diplome)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_diplome',
            name='Can add Diplome',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_diplome',
            name='Can change Diplome',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_diplome',
            name='Can delete Diplome',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_diplome',
            name='Can view Diplome',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_diplome_permissions()



    def create_contrat_permissions():
        content_type = ContentType.objects.get_for_model(Contrat)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_contrat',
            name='Can add Contrat',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_contrat',
            name='Can change Contrat',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_contrat',
            name='Can delete Contrat',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_contrat',
            name='Can view Contrat',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_contrat_permissions()



    def create_grade_permissions():
        content_type = ContentType.objects.get_for_model(Grade)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_grade',
            name='Can add Grade',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_grade',
            name='Can change Grade',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_grade',
            name='Can delete Grade',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_grade',
            name='Can view Grade',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_grade_permissions()


    def create_domaine_permissions():
        content_type = ContentType.objects.get_for_model(Domaine)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_domaine',
            name='Can add Domaine',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_domaine',
            name='Can change Domaine',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_domaine',
            name='Can delete Domaine',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_domaine',
            name='Can view Domaine',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_domaine_permissions()



    def create_departement_permissions():
        content_type = ContentType.objects.get_for_model(Departement)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_departement',
            name='Can add Departement',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_departement',
            name='Can change Departement',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_departement',
            name='Can delete Departement',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_departement',
            name='Can view Departement',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_departement_permissions()



    def create_avancement_permissions():
        content_type = ContentType.objects.get_for_model(Avancement)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_avancement',
            name='Can add Avancement',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_avancement',
            name='Can change Avancement',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_avancement',
            name='Can delete Avancement',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_avancement',
            name='Can view Avancement',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_avancement_permissions()


    def create_fonction_permissions():
        content_type = ContentType.objects.get_for_model(Fonction)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_fonction',
            name='Can add Fonction',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_fonction',
            name='Can change Fonction',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_fonction',
            name='Can delete Fonction',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_fonction',
            name='Can view Fonction',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_fonction_permissions()


    def create_mention_permissions():
        content_type = ContentType.objects.get_for_model(Mention)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_mention',
            name='Can add Mention',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_mention',
            name='Can change Mention',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_mention',
            name='Can delete Mention',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_mention',
            name='Can view Mention',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_mention_permissions()


    def create_corps_permissions():
        content_type = ContentType.objects.get_for_model(Corps)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_corps',
            name='Can add Corps',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_corps',
            name='Can change Corps',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_corps',
            name='Can delete Corps',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_corps',
            name='Can view Corps',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_corps_permissions()




    def create_situation_permissions():
        content_type = ContentType.objects.get_for_model(Situation)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_situation',
            name='Can add Situation',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_situation',
            name='Can change Situation',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_situation',
            name='Can delete Situation',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_situation',
            name='Can view Situation',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_situation_permissions()




    def create_affectation_permissions():
        content_type = ContentType.objects.get_for_model(Affectation)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_affectation',
            name='Can add Affectation',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_affectation',
            name='Can change Affectation',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_affectation',
            name='Can delete Affectation',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_affectation',
            name='Can view Affectation',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_affectation_permissions()



    def create_type_conge_permissions():
        content_type = ContentType.objects.get_for_model(TypeConge)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_typeconge',
            name='Can add TypeConge',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_typeconge',
            name='Can change TypeConge',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_typeconge',
            name='Can delete TypeConge',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_typeconge',
            name='Can view TypeConge',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_type_conge_permissions()



    def create_conge_permissions():
        content_type = ContentType.objects.get_for_model(Conge)

        add_permission, _ = Permission.objects.get_or_create(
            codename='add_conge',
            name='Can add Conge',
            content_type=content_type,
        )

        change_permission, _ = Permission.objects.get_or_create(
            codename='change_conge',
            name='Can change Conge',
            content_type=content_type,
        )

        delete_permission, _ = Permission.objects.get_or_create(
            codename='delete_conge',
            name='Can delete Conge',
            content_type=content_type,
        )

        view_permission, _ = Permission.objects.get_or_create(
            codename='view_conge',
            name='Can view Conge',
            content_type=content_type,
        )

    if __name__ == "__main__":
        create_conge_permissions()









