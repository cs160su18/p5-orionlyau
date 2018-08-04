from django import forms

class NewFlightForm(forms.Form):
    date = forms.DateField(label='Date')
    type = forms.CharField(label='Aircraft Type', max_length=50)
    identifier = forms.CharField(label='Tail Number', max_length=50)
    route = forms.CharField(label='Route', max_length=50)
    duration = forms.DecimalField(label='Duration', max_digits=6, decimal_places=3)
    landings = forms.IntegerField(label='Landings')