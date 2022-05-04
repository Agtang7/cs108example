# project/urls.py
from django.urls import path
from .views import HomePageView, GroupInfoView # our view class definition 


urlpatterns = [
    # map the URL (empty string) to the view
    path('', HomePageView.as_view(), name='home'), # generic class-based view
    path('group/<int:pk>',GroupInfoView.as_view(), name='group'), # show one group
]