from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .model_admin_mixins import ChildCrfModelAdminMixin
from ..admin_site import flourish_child_admin
from ..forms import ChildCovid19Form
from ..models import ChildCovid19


@admin.register(ChildCovid19, site=flourish_child_admin)
class Covid19Admin(ChildCrfModelAdminMixin, admin.ModelAdmin):
    form = ChildCovid19Form

    fieldsets = (
        (None, {
            'fields': [
                'child_visit',
                'report_datetime',
                'test_for_covid',
                'date_of_test',
                'is_test_estimated',
                'reason_for_testing',
                'other_reason_for_testing',
                'result_of_test',
                'isolation_location',
                'other_isolation_location',
                'isolations_symptoms',
                'has_tested_positive',
                'date_of_test_member',
                'close_contact',
                'symptoms_for_past_14days',
                'fully_vaccinated',
                'vaccination_type',
                'other_vaccination_type',
                'first_dose',
                'second_dose',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'test_for_covid': admin.VERTICAL,
        'is_test_estimated': admin.VERTICAL,
        'reason_for_testing': admin.VERTICAL,
        'result_of_test': admin.VERTICAL,
        'isolation_location': admin.VERTICAL,
        'has_tested_positive': admin.VERTICAL,
        'close_contact': admin.VERTICAL,
        'fully_vaccinated': admin.VERTICAL,
        'vaccination_type': admin.VERTICAL,
    }

    filter_horizontal = ('isolations_symptoms', 'symptoms_for_past_14days')
