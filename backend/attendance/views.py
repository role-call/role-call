from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Group
from .models import Occupant, Occupant_Picture
from rest_framework import viewsets
from rest_framework import permissions
from django.views import generic
from .serializers import UserSerializer, GroupSerializer, OccupantSerializer,Occupant_PictureSerializer
from rest_framework import generics
from .forms import OccupantPictureForm

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)
class IndexView(TemplateView):
    template_name = "index.html"

class OccupantsListView(generic.ListView):
    template_name = "occupants.html"
    context_object_name = 'occupants'

    def get_queryset(self):
        """Return the last five published questions."""
        return Occupant.objects.all()
    permission_classes = [permissions.IsAuthenticated]
class OccupantDetailView(generic.DetailView):
    slug_field = "external_id"
    template_name = "occupantdetail.html"
    model = Occupant
    permission_classes = [permissions.IsAuthenticated]
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class OccupantViewSet(viewsets.ModelViewSet):
    queryset = Occupant.objects.all()
    serializer_class = OccupantSerializer
    lookup_field = 'external_id'
    permission_classes = [permissions.IsAuthenticated]
class OccupantDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field= "external_id"
    queryset = Occupant.objects.all()
    serializer_class = OccupantSerializer
    permission_classes = [permissions.IsAuthenticated]

class OccupantPictureViewSet(viewsets.ModelViewSet):
    lookup_field = "external_id"
    queryset = Occupant_Picture.objects.all()
    serializer_class = Occupant_PictureSerializer
    permission_classes = [permissions.IsAuthenticated]

from django.views.generic.edit import CreateView, DeleteView, UpdateView


from django.urls import reverse_lazy

class OccupantCreateView(CreateView):
    model = Occupant
    fields = ['firstName','lastName']
    template_name = 'attendance/occupant_new_form.html'
    success_url = reverse_lazy('occupants_list')



class OccupantUpdateView(UpdateView):
    slug_field = "external_id"
    model = Occupant
    fields = ['firstName','lastName']
    success_url = reverse_lazy('occupants_list')


class OccupantDeleteView(DeleteView):
    slug_field = "external_id"
    model = Occupant
    success_url = reverse_lazy('occupants_list')


class OccupantPictureCreateView(BSModalCreateView):
    form_class = OccupantPictureForm
    # template_name = 'attendance//occupant_picture_form.html'
    success_messagge = "Success"
    success_url = reverse_lazy('occupant_detail')
    model = Occupant_Picture
    # fields = ['occupant','img']

class OccupantPictureUpdateView(UpdateView):
    slug_field = "external_id"
    model = Occupant_Picture
    fields = ['img']
