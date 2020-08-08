from django.db import models

class Gdrive(models.Model):

    title = models.CharField(max_length=200,null=False)
    discription = models.TextField(max_length=600,null=False)
    thumbnail = models.ImageField(upload_to='streamd/thumbnail',null=False)
    gdrive_link = models.CharField(max_length=200,null=False)

    def __str__(self):

        return self.title
