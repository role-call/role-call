from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('occupant/', views.OccupantsListView.as_view(), name="occoupants_list"),
    path('occupant-detail/<uuid:slug>/', views.OccupantDetailView.as_view(), name="occupant_detail"),
    path('occupant/add/', views.OccupantCreateView.as_view(), name='occupant_add'),
    path('occupant/<uuid:slug>/', views.OccupantUpdateView.as_view(), name='occupant_update'),
    path('occupant_picture/<uuid:slug>/', views.OccupantPictureUpdateView.as_view(), name='occupant_picture_update'),
    path('occupant_picture/add/', views.OccupantPictureCreateView.as_view(), name='occupant_picture_add'),
]