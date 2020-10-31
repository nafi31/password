from django.shortcuts import render, redirect
from .models import Website, Password
from django.http import HttpResponse
# Create your views here.
def create(request):
	if request.method == 'POST':
		website= request.POST.get("website")
		password = request.POST.get("password")
		w = Website(name=website)
		w.save()
		p = Password(web=w,password=password)
		p.save()
		request.user.todo.add(w)
		return redirect("/list")
	else:
		return render(request,'password/create.html',{})
	return render(request,'password/create.html',{})
def list(request):
	web = Website.objects.all()
	return render(request,'password/list.html',{"web":web})


def solo(request,id):
	solo = Website.objects.get(id=id)
	if solo in request.user.todo.all():
		if request.method == "POST":
			solo.delete()
			return redirect("/list")
	else:
		
		return HttpResponse("<strong><h1>You do Not belong here </h1> </strong>")
	return render(request,'password/solo.html',{"solo":solo})