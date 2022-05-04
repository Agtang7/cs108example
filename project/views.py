from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Raid
from .models import Player
from .models import Group

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