from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from apps.search.models import User
from django.core import serializers
  # the index function is called when root is visited
def index(request):
    return render(request,"search/index.html")

def search(request):
    return render(request,"search/search.html")
# <QueryDict: {'newUser': ['first_name=&last_name=&gender=male&image_url=&sport=basketball']}>
def add(request):
  if request.method == "POST":
    print("*"*50)
    print(request.POST)
    print("*"*50)
    User.objects.create(
      first_name = request.POST["first_name"],
      last_name  = request.POST["last_name"],
      gender     = request.POST["gender"],
      image_path = request.POST["image_url"],
      sport      = request.POST["sport"]
    )
    return HttpResponse("done")

def fetch(request):
  if request.method == "POST":
    users = User.objects.all()[:int(request.POST["num"])]
    return HttpResponse(serializers.serialize("json", users))
# <QueryDict: {'name': ['hea'], 'male': ['false'], 'female': ['false'], 
# 'basketball': ['false'], 'volleyball': ['false'], 'soccer': ['false'], 'football': ['false']}>
def filter(request):
  if request.method == "POST":
    genders = []
    sports = []

    if request.POST["male"] == 'true':
      genders.append("Male")
    if request.POST["female"] == 'true':
      genders.append("Female")

    if request.POST["basketball"] == 'true':
      sports.append("Basketball")
    if request.POST["volleyball"] == 'true':
      sports.append("Volleyball")
    if request.POST["soccer"] == 'true':
      sports.append("Soccer")
    if request.POST["football"] == 'true':
      sports.append("Football")

    users = None
    if len(genders) > 0 and len(sports) > 0:
      users = User.objects.filter(
        (Q(first_name__contains = request.POST["name"]) | Q(last_name__contains = request.POST["name"]))
        & (Q(gender__in=genders))
        & (Q(sport__in=sports))
      )
    elif len(genders) > 0:
      users = User.objects.filter(
        (Q(first_name__contains = request.POST["name"]) | Q(last_name__contains = request.POST["name"]))
        & (Q(gender__in=genders))
      )
    elif len(sports) > 0:
      users = User.objects.filter(
        (Q(first_name__contains = request.POST["name"]) | Q(last_name__contains = request.POST["name"]))
        & (Q(sport__in=sports))
      )
    else:
      users = User.objects.filter(
        (Q(first_name__contains = request.POST["name"]) | Q(last_name__contains = request.POST["name"]))
      )
    
    return HttpResponse(serializers.serialize("json", users))