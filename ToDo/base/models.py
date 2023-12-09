from django.db import models

# Create your models here.
status_list=[('Done','Done'),('Not Done','Not Done')]
class Todo(models.Model):
    name= models.CharField(max_length=300) 
    description=models.TextField()
    status=models.CharField(max_length=50,choices=status_list)
    
    def __str__(self) :
        return (self.name)