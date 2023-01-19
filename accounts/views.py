from django.shortcuts import render, redirect
from accounts.forms import LogInForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_login(request):
  if request.method == "POST":
    form = LogInForm(request.POST)
    if form.is_valid():
      # check if user is in database
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(
        request,
        username=username,
        password=password,
      )
      if user is not None:
        login(request, user)
        return redirect("home")

  else:
    form = LogInForm()
  context = {
    'form' : form
  }
  return render(request, 'accounts/login.html', context)
