from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(default='', upload_to='videos')

    def __str__(self):
        return self.title



class Picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(default='', upload_to='pictures')

    def __str__(self):
        return self.title
