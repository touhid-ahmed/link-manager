from django.shortcuts import render, get_object_or_404
from .models import Link

# Create your views here.
 

def list_links(request):
    
    links = Link.objects.all()

    return render(request, 'linktracker/list.html', {'links': links})


def detail_links(request, pk):

    detail = get_object_or_404(Link, id=pk)

    return render(request, 'linktracker/detail.html', {'detail': detail})
 
def create_link(request):
    pass

def delete_link(request, pk):
    pass

def update_link(request, pk):
    pass