from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import User
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings


def indexfunction(request):
	return HttpResponse("HIIII")

def userfunction(request):
	return HttpResponse("userpage")

def user1function(request):
	return HttpResponse("user1page")


def userfunction1(request,id):
	return HttpResponse(id)


def addfunction(request,a,b):
	return HttpResponse(a+b)

def indexfunction(request):
	return HttpResponse("<h1>index</h1>")

def userpage(request):
	return redirect("user")


def apppage(request):
	return render(request, "apppage.html")


def questions(request):
	return render(request, "questions.html")





def adminpage(request):
	return render(request, "admin.html")


def contactuspage(request):
	return render(request, "contactus.html")


def adminhome(request):
	return render(request, "adminhome.html")


def userlogin(request):
	return render(request, "userlogin.html")


def alogout(request):
	return render(request, "admin.html")


def payment(request):
	return render(request, "payment.html")


def birthday(request):
	return render(request, "birthday.html")


def final(request):
	return render(request, "final.html")


def farewell(request):
	return render(request, "farewell.html")


def fests(request):
	return render(request, "fests.html")



def aboutus(request):
	return render(request, "aboutus.html")


def wedding(request):
	
	return render(request, "wedding.html")




def regsuccess(request):
	return render(request, "regsuccess.html")


def contactme(request):
	return render(request, "contactme.html")







def viewusers(request):

	users=User.objects.all()
	return render(request, "viewusers.html", {'users':users})


def deleteuser(request,id):
	User.objects.filter(id=id).delete()
	users=User.objects.all()
	return render(request,"viewusers.html",{'users':users})



def checkadmin(request):
	if request.method == "POST":
		aid=request.POST['aid']
		apwd=request.POST['apwd']
		if aid=='dinesh' and apwd=='dinesh':
			return redirect("adminhome")
		else:
			return HttpResponse("Invalid Login")




def userreg(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			subject="Thanks for registering,Welcome to our site"
			email=EmailMessage(subject,"You are now a member of our site.",to=[form.data['email']])
			email.send()
			return redirect('regsuccess')
	else:
		form = RegistrationForm()
	return render(request,'user.html',{'form':form})




def  checkuser(request):
	if request.method == "POST":
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		flag=User.objects.filter(Q(username=uname) & Q(password=pwd))
		if flag:
			request.session['uname'] = uname
			return render(request,'usershop.html',{'uname':uname})
		else:
			return HttpResponse("INVALID LOGIN")
	else:
		return render("userlogin.html")
	return render("userlogin.html")




