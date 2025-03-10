from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)
    #blank = true lets url to be empty
    def __str__(self):
        return self.title
