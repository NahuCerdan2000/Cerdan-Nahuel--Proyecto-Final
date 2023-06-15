from django import forms

from . import models


class PersonalForm(forms.ModelForm):
    class Meta:
        model = models.Personal
        fields = "__all__"


class SectorForm(forms.ModelForm):
    class Meta:
        model = models.Sector
        fields = "__all__"
