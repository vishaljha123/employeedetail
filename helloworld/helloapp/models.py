from django.db import models
from datetime import datetime


# Create your models here.
class employeedetails(models.Model):
    name = models.CharField(max_length=155)
    designation = models.CharField(max_length=155)
    location = models.CharField(max_length=155)
    servicestart = models.DateTimeField(default=None,blank=True)
    serviceends = models.DateTimeField(default=None,blank=True)


    class Meta:
        ordering=['servicestart']
    
    def __str__(self):
        name = self.name
        designation = self.designation
        location = self.location
        servicestart = self.servicestart
        serviceends = self.serviceends

        return '{}{}{}{}{}'.format(self.name, self.location,self.designation,self.serviceends,self.servicestart)


