from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 200)
    info = models.TextField(default='empty')
    authors = models.ManyToManyField(User)
    #deadline = models.Foriegn()
    #milestones = models.ForiegnKey()


    saleDocLink = models.URLField(blank=True, null=True)
    salePointsCreated = models.NullBooleanField()
    researchDone = models.NullBooleanField()
    internalMeetingCreated = models.NullBooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/projectdetails/%i/" % self.id


class Event(models.Model):

    TYPE_CHOICE = (
        ('E', 'Event'),
        ('T', 'Task'),
    )

    title = models.CharField(max_length=100, null=True)
    datetime = models.DateField()
    description = models.TextField(max_length=750, default='Add a description of the event!')
    project = models.ForeignKey('Project', null=True)
    users = models.ManyToManyField(User)
    eventtype = models.CharField(max_length=1, choices=TYPE_CHOICE, default='T')

    def __str__(self):
        return self.title
