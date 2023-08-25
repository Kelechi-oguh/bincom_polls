from django import forms
from .models import PollingUnit, AnnouncedPuResults
 
# creating a form
class polling_unit_form(forms.ModelForm):

    class Meta:
        model = PollingUnit
        fields = ["polling_unit_id", "ward_id", "lga_id", "polling_unit_number", "polling_unit_name", "polling_unit_description"]



class result_form(forms.ModelForm):

    class Meta:
        model = AnnouncedPuResults
        fields = ["polling_unit_uniqueid", "party_abbreviation", "party_score", "entered_by_user", "user_ip_address"]