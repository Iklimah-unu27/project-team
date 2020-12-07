from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)
    nodata = models.IntegerField(null=True)
    norole = models.IntegerField(null=True)
    

    def __str__(self):
        return self.user.username