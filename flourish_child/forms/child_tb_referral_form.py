from django import forms
from django.apps import apps as django_apps
from flourish_child.forms.child_form_mixin import ChildModelFormMixin
from flourish_child.models.child_tb_referral import ChildTBReferral
from flourish_child_validations.form_validators.child_tb_referral_form_validator import \
    ChildTBReferralFormValidator
from flourish_child.models.list_models import ChildTbReferralReasons
from edc_constants.constants import YES


class ChildTBReferralForm(ChildModelFormMixin, forms.ModelForm):
    form_validator_cls = ChildTBReferralFormValidator
    tb_screening_model = 'flourish_child.childtbscreening'

    @property
    def tb_screening_model_cls(self):
        return django_apps.get_model(self.tb_screening_model)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subject_identifier = self.initial.get('subject_identifier', None)

        referral_reasons = []

        tb_screening_options = {
            'cough': 'cough_duration',
            'fever': 'fever_duration',
            'sweats': 'sweats_duration',
            'weight_loss': 'weight_loss_duration',
        }
        tb_screening_options_other = {
            'household_diagnosed_with_tb': 'fatigue_or_reduced_playfulness'
        }
        tb_screening_obj = self.tb_screening_model_cls.objects.filter(
            child_visit__subject_identifier=subject_identifier).first()
        if tb_screening_obj:
            for symptom, duration in tb_screening_options.items():
                symptom_value = getattr(tb_screening_obj, symptom)
                duration_value = getattr(tb_screening_obj, duration)
                if symptom_value == YES and duration_value == '>= 2 weeks':
                    referral_reason = ChildTbReferralReasons.objects.filter(
                        short_name=symptom).first()
                    if referral_reason:
                        referral_reasons.append(referral_reason.id)
            for house_hold, fatigue in tb_screening_options_other.items():
                house_hold_value = getattr(tb_screening_obj, house_hold)
                fatigue_value = getattr(tb_screening_obj, fatigue)
                if house_hold_value == YES:
                    house_hold_reason = ChildTbReferralReasons.objects.filter(
                        short_name=house_hold).first()
                    referral_reasons.append(house_hold_reason.id)
                if fatigue_value == YES:
                    fatigue_reason = ChildTbReferralReasons.objects.filter(
                        short_name=fatigue
                    ).first()
                    if fatigue_reason:
                        referral_reasons.append(fatigue_reason.id)
        self.initial['reason_for_referral'] = referral_reasons

    class Meta:
        model = ChildTBReferral
        fields = '__all__'
