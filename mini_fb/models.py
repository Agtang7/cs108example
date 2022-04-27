from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    '''Represents the data attributes of Facebook users.'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    birthday = models.DateField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_pic = models.URLField(blank=True)
    friends = models.ManyToManyField("self")

    def __str__(self):
        '''Return a string representation of the profiles.'''

        return f'{self.first_name} {self.last_name} - {self.city} - {self.email_address}'
    
    def GetStatusMessage(self):
        '''Return all status messages for this person.'''

        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('show_profile_page', kwargs={'pk':self.pk})

    def get_friends(self):
        '''Allow any Profile object to have other Profile objects as friends.'''

        return self.friends.all()
    
    def get_news_feed(self):
        '''Return a QuerySet of all StatusMessages by this Profile and all of its friends.'''

        return StatusMessage.objects.filter(profile__in=self.get_friends()).order_by("-timestamp")

    def get_friends_suggestions(self):
        '''Obtain and return a QuerySet of all Profile that could be added as friends.'''

        possible_friends = Profile.objects.exclude(pk__in=self.friends.all()).exclude(pk=self.pk)
        return possible_friends

class StatusMessage(models.Model):
    '''Model the data attributes of Facebook Status message.'''

    # data attributes:
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''Return string representation of the message status.'''

        return f'{self.timestamp} {self.message} {self.image}'

