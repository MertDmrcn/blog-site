from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image= models.CharField(max_length=50,null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.name
    