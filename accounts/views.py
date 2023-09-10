from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    # form_class = CustomUserCreationForm
    model=CustomUser
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
