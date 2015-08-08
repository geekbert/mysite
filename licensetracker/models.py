from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

import datetime
from django.utils import timezone


class License(models.Model):
    Year = models.CharField(max_length=4)
    Quarter = models.CharField(max_length=1)
    #Date = models.DateTimeField('Date')
    Date = models.DateField('Date')
    Customer = models.CharField(max_length=50, blank=True)
    Industry = models.CharField(max_length=50, blank=True)
    Products = models.CharField(max_length=200)
    License = models.***Field(max_length=50)
    Maintenance = models.***Field(max_length=50, blank=True)
    Consulting = models.***Field(max_length=50, blank=True)
    Region = models.CharField(max_length=20, blank=True)
    Was_I_Involved = models.NullBooleanField(null=True) 
    #LocalPreSalesInvolve = models.BooleanField() # checkbox widget 
    #Name_of_SE = models.CharField(max_length=50)
    #If_no_SE_why_not = models.CharField(max_length=100, blank=True)
    #Active_Role_What_Kind = models.CharField(max_length=100, blank=True)
    #GovSolutions = models.BooleanField()
    #Effort_Incl_Prep = models.CharField(max_length=50, blank=True)
    Comment = models.CharField(max_length=200, blank=True)
    #Whatwasgoodwhatbad = models.TextField() # textarea widget
    active = models.BooleanField(default=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.Year
    def __str__(self):              # __unicode__ on Python 2
        return self.Quarter
    def __str__(self):              # __unicode__ on Python 2
        return self.Date
    def __str__(self):              # __unicode__ on Python 2
        return self.Customer    
    def __str__(self):              # __unicode__ on Python 2
        return self.Industry
    def __str__(self):              # __unicode__ on Python 2
        return self.Products
    def __str__(self):              # __unicode__ on Python 2
        return self.License
    def __str__(self):              # __unicode__ on Python 2
        return self.Maintenance
    def __str__(self):              # __unicode__ on Python 2
        return self.Consulting
    def __str__(self):              # __unicode__ on Python 2
        return self.Region
    def __str__(self):              # __unicode__ on Python 2
        return self.Was_I_Involved
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.GovSolutions
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.EffortInclPrep
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.Comment
    def was_published_recently(self):
        return self.Date >= timezone.now() - datetime.timedelta(days=1)
    #def __str__(self):  # Python 3: def __str__(self):
     #   return self.active
