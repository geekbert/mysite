from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
    fileattach = models.FileField(blank=True)
    textarea = models.TextField(blank=True)
    tag = models.CharField(max_length=4)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text
