from django.shortcuts import render
from django.http import HttpResponse


def demofunction(request):
	return HttpResponse("Demo here")


def mainpage(request):
	return render(request,"project.html")

