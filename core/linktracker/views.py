from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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
            return HttpResponseRedirect('/links/new?submitted=True')

    else:
        form = NewLinkForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "linktracker/newlink.html", {"form": form, 'submitted': submitted})


def update_link(request, pk):
    submitted = False

    link = get_object_or_404(Link, id=pk)

    if request.method == "POST":

        form = NewLinkForm(request.POST, instance=link)
    
        if form.is_valid():
            form.save()
            url = reverse("linktracker:update_link", args=[pk])
            return redirect(f"{url}?submitted=True")

    else:
        form = NewLinkForm(instance=link)
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, "linktracker/updatelink.html", {"form": form, 'submitted': submitted, "link_pk": pk, "link_obj": link})

def delete_link(request, pk):
    link = get_object_or_404(Link, id=pk)

    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('linktracker:list_links')

        link.delete()
        return redirect('linktracker:list_links')

    return render(request, 'linktracker/deletelink.html', {'link': link})


def home(request):
    return render(request, "linktracker/home.html")