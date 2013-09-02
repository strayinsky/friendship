from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    #choices
    SEX_CHOICES = (("M", 'male'), ("F", 'female'))
    REL_CHOICES = (
        ('S', 'single, no kids'),
        ('P', 'single, with kid(s)'),
        ('R', 'in a relationship, no kids'),
        ('K', 'in a relationship, with kid(s)'),
    )
    ED_CHOICES = (
        ('H', 'high school'),
        ('C', 'college'),
        ('A', 'advanced degree'),
    )
    PER_CHOICES = (
        ('I', 'introverted'),
        ('E', 'extroverted')
    )


    #model fields
    user = models.OneToOneField(User)
    age = models.IntegerField(max_length=2)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    rstatus = models.CharField(max_length=1, choices=REL_CHOICES)
    education = models.CharField(max_length=1, choices=ED_CHOICES)
    personality = models.CharField(max_length=1, choices=PER_CHOICES)
    blurb = models.CharField(max_length=200)
    date = models.DateTimeField('date added')

    #many to many relationship to User in order to track who likes who and who is liked by who
    likes = models.ManyToManyField("self", related_name="liked by")


#class Picture(models.model):
#   pic = models.ImageField


class Location(models.Model):
    homezip = models.CharField(max_length=5)
    workzip = models.CharField(max_length=5)
    date = models.DateTimeField('date added')

#this is a simple model to store all of the activities and the group they fall in
class Activity(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    date = models.DateTimeField('date added')
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

#who likes who
class Like(models.Model):
    userA = models.ForeignKey(User, related_name='like_userA')
    userB = models.ForeignKey(User, related_name='like_userB')
    date = models.DateTimeField('date added')

    def __unicode__(self):
        return self.userA.name + " likes " + self.userB.name


#who likes to do what
# class UserActivity(models.Model):
#     user = models.ForeignKey(User)
#     activity = models.ForeignKey(Activity)
#     date = models.DateTimeField('date added')





