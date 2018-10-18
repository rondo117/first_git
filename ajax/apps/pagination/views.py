from django.shortcuts import render, HttpResponse, redirect
from apps.pagination.models import User
from django.core import serializers
from django.db.models import Q
  # the index function is called when root is visited
def index(request):
  users =  User.objects.all()
  users = serializers.serialize("json", users)
  return render(request, "pagination/index.html", {"users":users})

def search(request):
  if request.method == "POST":
    name = request.POST["name"]
    users = User.objects.filter(Q(first_name__contains=name) | Q(last_name__contains =name) )
    return HttpResponse(serializers.serialize("json", users))