import uuid
from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Installation(models.Model):
    external_id = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    prefs = models.TextField()


class Facility(models.Model):
    external_id = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)


class Occupant(models.Model):
    external_id = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('occupant_detail', kwargs={'slug': self.external_id})

class Room(models.Model):
    external_id = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)


class Room_x_Occupant(models.Model):
    class Meta:
        models.UniqueConstraint(fields=['inRoom', 'person'], name="room_occupant_id",)
    inRoom = models.ForeignKey(Room, on_delete=models.CASCADE)
    person = models.ForeignKey(Occupant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, blank=True)
    modified_at = models.DateTimeField(auto_now=True)


class Occupant_Picture(models.Model):
    external_id = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    occupant = models.ForeignKey(Occupant, on_delete=models.CASCADE, related_name="picture")
    imageType = models.CharField(max_length=10, default='profile', blank=True)
    img = models.ImageField(upload_to='images/', default=None)
    created_at = models.DateTimeField(default=now, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('occupant_detail', kwargs={'slug': self.occupant.external_id})

class Occupant_Status(models.Model):
    occupant = models.ForeignKey(Occupant, on_delete=models.CASCADE, related_name="status")
    status = models.CharField(max_length=20)
    modified_at = models.DateTimeField(auto_now=True)

class Occupant_Type(models.Model):
    external_id = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    name = models