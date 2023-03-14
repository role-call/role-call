from django.forms import ModelForm
from  attendance.models import  Occupant, Occupant_Picture
from bootstrap_modal_forms.forms import BSModalModelForm

class OccupantForm(ModelForm):
    class Meta:
        model = Occupant
        fields = ['firstName', 'lastName']
class OccupantPictureForm(BSModalModelForm):
    class Meta:
        model = Occupant_Picture
        fields = ['occupant', 'img']