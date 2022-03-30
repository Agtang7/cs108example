##### quotes/views.py #####

from .models import Quote
from django.views.generic import ListView, DetailView, CreateView, UpdateView ## NEW
rom .forms import CreateQuoteForm, UpdateQuoteForm ## NEW

class UpdateQuoteView(UpdateView):
    '''Update an existing Quote object and store it in the database.'''

    model = Quote # which model to create
    form_class = UpdateQuoteForm # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the display to this template