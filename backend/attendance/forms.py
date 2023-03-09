from django.forms import ModelForm
from models import Occupant

class ModelForm(ModelForm):
    class Meta:
        model = Occupant
        fields = ['firstName', 'lastName']