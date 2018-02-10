from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def index(request):
    return render(request, 'personal/home.html', {'year':datetime.now().year,})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'personal/basic.html',
        {
            'title':'Contact',
            'message':'If you require any further information, feel free to contact me.',
            'year':datetime.now().year,
        }
    )

def download(request):
    """Renders the download page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'personal/download.html',
    )

def einleitung(request):
    """Renders the download page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'personal/einleitung.html', {'year':datetime.now().year,}
    )