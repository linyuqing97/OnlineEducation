from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


GENDE_CHOSE=(
    ("male","Male"),
    ("female","Female")
)

class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Time adding this course")

    # Don't create a new table
    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=60, verbose_name="Name", null=True, blank=True)
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="Gender",choices=GENDE_CHOSE, max_length = 6)
    address=models.CharField(verbose_name="Address", max_length=100, default="")
    phoneNumber  = models.CharField(verbose_name="Phone Number", max_length=10)
    image = models.ImageField(upload_to="head_image/%Y/%m",default="default.jpg")

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
# Create your models here.
