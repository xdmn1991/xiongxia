from django.db import models
from django.urls import reverse
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

  def get_absolute_url(self):
    return reverse("post_detail", args=[str(self.id)])