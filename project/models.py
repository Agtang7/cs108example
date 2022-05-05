from django.db import models
from django.urls import reverse


# Create your models here.


#first class
class Raid(models.Model):
    '''represent the party for a raid section'''

     # data attributes:

    raid_name = models.TextField(blank=True)
    difficulty = models.TextField(blank=True)
    level_requirment = models.IntegerField(blank=True)
    faction = models.TextField(blank=True)
    #if i need to use image
    #image_url = models.URLField(blank=True)
    #python manage.py makemigrations
    #python manage.py migrate

    def __str__(self):
        '''Return a string representation of the raid.'''

        return f'{self.raid_name} {self.difficulty} - {self.level_requirment} - {self.faction}'


#second class

class Player(models.Model):
    '''represent the player info in game'''

     # data attributes:

    player_tag = models.TextField(blank=True)
    discord_id = models.TextField(blank=True)
    player_class= models.TextField(blank=True)
    player_role = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of the player.'''

        return f'{self.player_tag} {self.discord_id} - {self.player_class} - {self.player_role}'

    
    
    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('playerlist')

#class 3

class Group(models.Model):
    '''represent the party for a group party'''

     # data attributes:

    raid_name = models.ForeignKey(Raid, on_delete=models.CASCADE)
    player_tag = models.ForeignKey(Player, on_delete=models.CASCADE)
    discord_group = models.TextField(blank=True)
    time = models.TextField(blank=True)
    player_needed = models.IntegerField(blank=True)
    image = models.URLField(blank=True)



    def __str__(self):
        '''Return a string representation of the raid.'''

        return f'{self.raid_name} {self.discord_group} - {self.time} - {self.player_needed} - {self.player_tag} - {self.image}'

    def get_absolute_url(self):
        '''Provide a url to show this object.'''

        return reverse('home')
