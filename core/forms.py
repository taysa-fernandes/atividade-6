from django import forms
from .models import Sebo_discos

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Sebo_discos
        fields = '__all__'