from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, "post/index.html")

def newNote(request):
    if request.method == "POST":
        return render(request, "post/note.html", {"note": request.POST["note"]})
