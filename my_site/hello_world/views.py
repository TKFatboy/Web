from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm
from .models import Member

def index(request):
  if request.method =='POST':
    details = request.POST

    print(request.POST['title'])
    ##member = Member()
    ##member.username = details['username'].value()
    ##member.password = details['password'].value()
    ##for obj in Member.objects.all():
      ##print(obj.username)
    ##member.save()
    return HttpResponseRedirect('/home2')
  
  else:
    form ={}
    form = RegisterForm()
    
  return render(request, "home2.html", {'form': form})
  

def home(request):
  return render(request, "Home.html")
def home2(request):
  return render(request, "home2.html")
def read1(request):
  return render(request, "read.html")
def read2(request):
  return render(request, "read2.html")
def read3(request):
  return render(request, "read3.html")
def read4(request):
  return render(request, "read4.html")
def read5(request):
  return render(request, "read5.html")
def search(request):
  return render(request, "search.html")
def info(request):
  return render(request, "info.html")
def action(request):
  return render(request, "action.html")
def adventure(request):
  return render(request, "adventure.html")
def comedy(request):
  return render(request, "comedy.html")
def drama(request):
  return render(request, "drama.html")
def fantasy(request):
  return render(request, "fantasy.html")
def horror(request):
  return render(request, "horror.html")
def romance(request):
  return render(request, "romance.html")
def thriller(request):
  return render(request, "thriller.html")
def western(request):
  return render(request, "western.html")
def scifi(request):
  return render(request, "scifi.html")
def crime(request):
  return render(request, "crime.html")
def mystery(request):
  return render(request, "mystery.html")
def test(request):
  print("test")
  if request.method == "POST":
        print(request.body)
  return render(request, "test.html")