from django import forms
from .models import Player
from .models import Group

class CreatePlayerForm(forms.ModelForm):
    '''A form to add a new Player.'''
    

    

    class Meta:
        '''additional data about the form.'''

        model = Player
        fields = ['player_tag', 'discord_id', 'player_class', 'player_role']


class CreateGroupForm(forms.ModelForm):
    '''A form to add a new Player.'''
    

    

    class Meta:
        '''additional data about the form.'''

        model = Group
        fields = ['raid_name', 'player_tag', 'discord_group', 'time','player_needed','image']


class UpdateGroupForm(forms.ModelForm):
    '''A form to update a group.'''

    class Meta:
        '''additional data about the form.'''

        model = Group
        fields = ['raid_name', 'player_tag', 'discord_group', 'time','player_needed','image']