import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_unauthorized(client):
   url = reverse('admin:index')
   response = client.get(url)
   assert (response.status_code == 302) and ( response.url == "/backend/admin/login/?next=/backend/admin/")



@pytest.mark.django_db
def test_superuser_view(admin_client):
   url = reverse('admin:index')
   response = admin_client.get(url)
   assert response.status_code == 200