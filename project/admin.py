import imp
from django.contrib import admin

# Register your models here. list or use *
from .models import Raid
from .models import Player
from .models import Group


admin.site.register(Raid)
admin.site.register(Group)
admin.site.register(Player)

