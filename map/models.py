from django.db import models
import uuid

# Create your models here.

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('accounts.UserAccount', on_delete=models.CASCADE)
    share_id = models.UUIDField(default=uuid.uuid4, editable=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.id
    
class SessionPin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    picture = models.ImageField(null=True, blank=True)
    is_pin = models.BooleanField(default=False)
    score = models.IntegerField(default=0, null=False)

    def __self__(self):
        return self.id