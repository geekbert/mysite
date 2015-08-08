from django.db import models

# Create your models here.

import datetime
from django.utils import timezone


class Event(models.Model):
    Year = models.CharField(max_length=4)
    Quarter = models.CharField(max_length=1)
    #Date = models.DateTimeField('Date')
    Date = models.DateField('Date')
    Customer = models.CharField(max_length=50, blank=True)
    Event_Type = models.CharField(max_length=100)
    RSM_Overlay_Local = models.CharField(max_length=50)
    Region = models.CharField(max_length=20, blank=True)
    Local_PreSales_Involved = models.NullBooleanField(null=True) 
    #LocalPreSalesInvolve = models.BooleanField() # checkbox widget 
    Name_of_SE = models.CharField(max_length=50)
    If_no_SE_why_not = models.CharField(max_length=100, blank=True)
    Active_Role_What_Kind = models.CharField(max_length=100, blank=True)
    GovSolutions = models.BooleanField()
    POC = models.BooleanField(default=None) # otherwise asks for default
    Effort_Incl_Prep = models.CharField(max_length=50, blank=True)
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
        return self.Event_Type
    def __str__(self):              # __unicode__ on Python 2
        return self.RSMOverlayLocal
    def __str__(self):              # __unicode__ on Python 2
        return self.Region
    def __str__(self):              # __unicode__ on Python 2
        return self.LocalPreSalesInvolved
    def __str__(self):              # __unicode__ on Python 2
        return self.Name_of_SE
    def __str__(self):              # __unicode__ on Python 2
        return self.IfnoSEwhynot
    def __str__(self):              # __unicode__ on Python 2
        return self.ActiveRoleWhatKind
    def __str__(self):              # __unicode__ on Python 2
        return self.GovSolutions
    def __str__(self):              # __unicode__ on Python 2
        return self.POC
    def __str__(self):              # __unicode__ on Python 2
        return self.EffortInclPrep
    def __str__(self):              # __unicode__ on Python 2
        return self.Comment
    def was_published_recently(self):
        return self.Date >= timezone.now() - datetime.timedelta(days=1)
    #def __str__(self):  # Python 3: def __str__(self):
     #   return self.active



    
