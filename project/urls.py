# project/urls.py
from django.urls import path
from .views import HomePageView, GroupInfoView, CreatePlayerView, CreateGroupView, PlayerInfoView, UpdateGroupView# our view class definition 


urlpatterns = [
    # map the URL (empty string) to the view
    path('', HomePageView.as_view(), name='home'), # generic class-based view
    path('group/<int:pk>',GroupInfoView.as_view(), name='group'),#show groip
    path('player',PlayerInfoView.as_view(),name='playerlist'),#Show list of player signed up
    path('create_player',CreatePlayerView.as_view(), name='player'), # show add player
    path('create_group',CreateGroupView.as_view(), name='addgroup'), # show add group
    path('group/<int:pk>/update', UpdateGroupView.as_view(), name="update_group"), #show update group site
]