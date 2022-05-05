from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Group
from .models import Player
from .forms import CreatePlayerForm, CreateGroupForm, UpdateGroupForm




# Create your views here.

class HomePageView(ListView):
    '''Create a subclass of ListView to display all quotes.'''

    model = Group
    template_name = 'groups/home.html'
    context_object_name = 'groups' # how to find the data in the template file


class GroupInfoView(DetailView):
    "display a single group view"

    model = Group
    template_name = 'groups/group.html'
    context_object_name = 'group'

class PlayerInfoView(ListView):

    model = Player
    template_name = 'groups/player.html'
    context_object_name = 'players' # how to find the data in the template file


class UpdateGroupView(UpdateView):
    '''Update a Profile object and store it in the database.'''

    model = Group
    form_class = UpdateGroupForm
    template_name = "groups/update_group.html"

class CreatePlayerView(CreateView):

    "display add up in player"

    model = Player
    form_class = CreatePlayerForm
    template_name = 'groups/create_player_form.html'



class CreateGroupView(CreateView):

    "display add up in player"

    model = Group
    form_class = CreateGroupForm
    template_name = 'groups/create_group_form.html'



