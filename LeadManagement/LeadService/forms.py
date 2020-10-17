from django import forms
class FilterForm(forms.Form):
    contact_person_name = forms.BooleanField(label="Contact Person Name")
    phone_numer         = forms.BooleanField(label="Phone Number",required=False)
    address             = forms.BooleanField(label="Address",required=False)
    source              = forms.BooleanField(label="Source",required=False)
    current_stage       = forms.BooleanField(label="Current Stage",required=False)
    start_date          = forms.DateField(label="Start Date") 
    end_date            = forms.DateField(label="End Date") 