from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Link
from .forms import NewLinkForm

# Create your views here.
 

def list_links(request):
    
    links = Link.objects.all()

    return render(request, 'linktracker/list.html', {'links': links})


def detail_links(request, pk):

    detail = get_object_or_404(Link, id=pk)

    return render(request, 'linktracker/detail.html', {'detail': detail})
 
def create_link(request):
    
    submitted = False

    if request.method == "POST":
        form = NewLinkForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newlink?submitted=True')


    else:
        form = NewLinkForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "linktracker/newlink.html", {"form": form, 'submitted': submitted})

def delete_link(request, pk):
    pass

def update_link(request, pk):
    pass


def home(request):
    return render(request, "linktracker/home.html")