from django.db import models

# Create your models here.

class Song(models.Model):
   
   title = models.CharField(max_length= 50)
   singer = models.CharField(max_length= 50)
   image = models.ImageField(upload_to=" ", max_length=250)
   audio_file = models.FileField(upload_to=" ", max_length=250 )
   audio_link = models.CharField(max_length=200, blank=True, default= " ")
   lyrics = models.TextField(blank=True, default= " ")
   duration = models.CharField(max_length=20)
   # paginate_by = 10

   def __str__(self):
      return self.title + self.duration