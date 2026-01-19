from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_view(request):
    user_form = UserCreationForm()  # código pronto do django
    return render(request, "register.html", {"user_form": user_form})
