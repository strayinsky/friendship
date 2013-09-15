from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up, user_logged_in

#this is a simple model to store all of the activities and the group they fall in
from django.dispatch import receiver


class Activity(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    date = models.DateTimeField('date added')
    #users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name


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
    # age = models.IntegerField(max_length=2)
    # sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    # rstatus = models.CharField(max_length=1, choices=REL_CHOICES)
    # education = models.CharField(max_length=1, choices=ED_CHOICES)
    # personality = models.CharField(max_length=1, choices=PER_CHOICES)
    # blurb = models.CharField(max_length=200)
    # date = models.DateTimeField('date added')

    #many to many relationship to User in order to track who likes who and who is liked by who
    likes = models.ManyToManyField("self", related_name="liked by")

    #many to many relationship with Activity
    activities = models.ManyToManyField(Activity, null=True)

    color = models.CharField(max_length=20)

    def __unicode__(self):
        return self.user.username

#right after someone signs up, create a new profile for them
@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    print "Create profile for", user
    p = Profile(user=user)
    p.save()


class Location(models.Model):
    homezip = models.CharField(max_length=5)
    workzip = models.CharField(max_length=5)
    date = models.DateTimeField('date added')




