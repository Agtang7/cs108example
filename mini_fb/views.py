from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from mini_fb.forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from .models import Profile, StatusMessage

class ShowAllProfilesView(ListView):
    '''Obtain data for all Profile records.'''
    model  = Profile # retrieve Profile objects from the database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    '''Obtain data for one Profile record.'''
    model  = Profile # retrieve Profile objects from the database
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    '''Create a new Profile object and store it in the database.'''

    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    '''Update a Profile object and store it in the database.'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet
            
            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()

            # create the Image object, but not save yet
            status_image = form.save(commit=False)

            # attach FK profile to this image
            status_image.profile = profile

            # now commit image to database
            status_image.save()
        
        else:
            print("Error: the form was not valid.")

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

class DeleteStatusMessageView(DeleteView):
    '''A view to delete a quote and remove it from the database.'''

    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        '''Return a dictionary with context data for this template to use.'''

        # get the default context data:
        # this will include the Profile record for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        
        # retrieving it from database and putting it into dictionary:
        status_message = StatusMessage.objects.get(pk=self.kwargs['status_pk'])

        # adding it into dictionary
        context['status_message'] = status_message

        # return the context dictionary:
        return context

    def get_object(self):
        ''''''
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        status_message = StatusMessage.objects.get(pk=status_pk)

        return status_message

    def get_success_url(self):
        
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        return reverse('show_profile_page', kwargs={'pk':profile_pk})

class ShowNewsFeedView(DetailView):
    '''Represents the status messages of profile's friends.'''

    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profile"

class ShowPossibleFriendsView(DetailView):
    '''Displays possible friends.'''

    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object_name = "profile"

def add_friend(request, profile_pk, friend_pk):
    '''Add a friend for a given profile.'''

    # find the Profile object which is adding the friend, and store it into a variable
    profile = Profile.objects.get(pk=profile_pk)

    # find the Profile object of the friend to add, and store it into another variable
    friend = Profile.objects.get(pk=friend_pk)

    # add that friend’s Profile into the profile.friends object (using the method add).
    profile.friends.add(friend)

    # save the profile object.
    profile.save()

    url = reverse('show_profile_page', kwargs={'pk':profile_pk})
    return redirect(url)