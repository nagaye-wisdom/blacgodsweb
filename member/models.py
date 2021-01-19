from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Member(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    bio = models.TextField(max_length=1000, default='')
    country = models.ImageField(default='', upload_to='flags')
    image = models.ImageField(default='', upload_to='profile_pics')

    def __str__(self):
        return self.name



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


