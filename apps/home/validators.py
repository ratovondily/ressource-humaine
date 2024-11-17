# validators.py

from django.core.exceptions import ValidationError
from django.utils import timezone

def date_not_in_past(value):
    if value < timezone.now().date():
        raise ValidationError("La date ne doit pas être dans le passé.")
