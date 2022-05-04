import imp
from django.contrib import admin

# Register your models here.
from .models import Raid
from .models import Group
from .models import Player

admin.site.register(Raid)
admin.site.register(Group)
admin.site.register(Player)