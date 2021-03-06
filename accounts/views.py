from django.shortcuts import render, redirect
from .forms import UserCreationForm 

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/accounts/login")
	else:
		form = UserCreationForm()
	return render(request,'accounts/register.html',{"form":form})