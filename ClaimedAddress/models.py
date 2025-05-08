from django.db import models
from django.contrib.auth.models import User

class ClaimedAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    claimed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} claimed {self.address}"
