from django.contrib import admin
from .models import  Installation,Facility,Occupant,Room,Room_x_Occupant,Occupant_Picture,Occupant_Status
# Register your models here.
# admin.site.register([Installation, Facility,Occupant,Room,Occupant_Picture,Occupant_Status])
admin.site.register([Installation, Facility,Occupant,Room,Room_x_Occupant,Occupant_Picture,Occupant_Status])