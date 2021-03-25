from .form import CreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('signup')
    template_name = 'signup.html'