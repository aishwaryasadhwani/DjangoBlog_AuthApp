from django.db import models

# Create your models here.
class PostBlog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    file = models.FileField(upload_to= 'images/')
    author = models.CharField(max_length=50)
    posted_date= models.DateTimeField(auto_now_add= True)
