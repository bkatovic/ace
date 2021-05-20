from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.user.is_authenticated:
        print("dobar dan")
        return redirect("/")

    if response.method == "POST":
        #   creating new user
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
