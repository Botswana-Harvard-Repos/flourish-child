from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO

from flourish_caregiver.choices import CLINIC_VISIT_CHOICES, SYMPTOMS_CHOICES
from ..list_models import ChronicConditions


class ChildMedicalHistoryMixin(models.Model):

    """A model completed by the user on Medical History for all children."""

    chronic_since = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name='Does the Child/Adolescent have any chronic conditions?',)

    child_chronic_other = OtherCharField(
        max_length=35,
        verbose_name='If other, specify.',
        blank=True,
        null=True)

    """Quartely phone calls stem question"""
    med_history_changed = models.CharField(
        verbose_name='Has any of your following medical history changed?',
        max_length=20,
        choices=YES_NO,
        null=True)

    current_illness_child = models.CharField(
        verbose_name="Does your child have any current illness?",
        max_length=10,
        choices=YES_NO
    )

    current_symptoms_child = models.CharField(
        verbose_name="What are your child's current symptoms",
        max_length=30,
        blank=True,
        null=True,
        choices=SYMPTOMS_CHOICES
    )

    current_symptoms_child_other = OtherCharField(
        max_length=35,
        verbose_name='If other, specify.',
        blank=True,
        null=True
    )

    symptoms_start_date_child = models.DateField(
        verbose_name="When did the symptoms start.",
        null=True,
        blank=True
    )

    clinic_visit_child = models.CharField(
        verbose_name="Has your child been seen at a local clinic or have you been seen"
                     " for consultation at a local clinic because of this illness?",
        max_length=20,
        choices=CLINIC_VISIT_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
