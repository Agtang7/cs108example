
from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new Profile.'''
    
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email Address", required=True)
    

    class Meta:
        '''additional data about the form.'''

        model = Profile
        fields = ['first_name', 'last_name', 'birthday', 'city', 'email_address', 'profile_pic']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a Profile.'''

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="City", required=True)
    email_address = forms.CharField(label="Email Address", required=True)

    class Meta:
        '''additional data about the form.'''

        model = Profile
        fields = ['first_name', 'last_name', 'birthday', 'city', 'email_address', 'profile_pic']

class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create a Message.'''

    image = forms.ImageField(label="image", required=False)

    class Meta:
        '''additional data about the form.'''

        model = StatusMessage
        fields = ['message', 'image']
