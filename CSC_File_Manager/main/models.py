from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

class CaseFile(models.Model):
    title = models.CharField(max_length=50)
    filePdf = models.FileField(upload_to='files')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title   
    
    def delete(self, *args, **kwargs):
        # Delete the file from the media directory
        if self.filePdf:
            os.remove(self.filePdf.path)

        # Call the parent class's delete method
        super().delete(*args, **kwargs)
    


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    



