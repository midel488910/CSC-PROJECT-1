from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime
from django.core.validators import FileExtensionValidator
#import magic

#validator that accepts only pdf files
ext_validator = FileExtensionValidator(["pdf"])
#################
# def validate_file_mimetype(file):
#     accept = ['application/pdf']
#     file_mine_type = magic.from_buffer(file.read(2048), mime=True)
#     if file_mine_type not in accept:
#         raise ValidationError("Unsupported File Type")
#
#*****CURRENTLY DOES NOT WORK**


#Database columns for PDF Files 
class CaseFile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    date_of_decision = models.DateField(default=datetime.today)
    docket_number = models.CharField(max_length=50,blank=True)
    respondents = models.CharField(max_length=50,blank=True)
    remarks = models.CharField(max_length=50,blank=True)
    filePdf = models.FileField(upload_to='files',blank=False,validators=[ext_validator])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
    
    #when delete is clicked the file is also removed from the database
    def delete(self, *args, **kwargs):
        # Delete the file from the media directory
        if self.filePdf:
            os.remove(self.filePdf.path)
        # Call the parent class's delete method
        super().delete(*args, **kwargs)
    



    



