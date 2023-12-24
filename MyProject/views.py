from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import Register

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data.get("username"),
                form.cleaned_data.get("email"),
                form.cleaned_data.get("password")
            )
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return render(request, 'register_done.html', {})
    else:
        form = Register()
        return render(request, 'registration/register.html', {'form': form})