from django.db import models
import uuid

# Create your models here.

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank=True)
    share_id = models.UUIDField(default=uuid.uuid4, editable=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    
class SessionPins(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    picture = models.ImageField(upload_to='pins/', null=True, blank=True)
    is_pin = models.BooleanField(default=False)
    score = models.IntegerField(default=0, null=False)