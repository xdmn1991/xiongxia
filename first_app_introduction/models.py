from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
  title = models.TextField()
  image = ProcessedImageField(
    upload_to = 'static/image/posts',
    format = 'JPEG',

  )

  def __str__(self):
    return self.title