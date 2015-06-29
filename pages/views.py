from django.http import Http404
from django.shortcuts import render
from .models import Document

def index(request):
    documents = Document.objects.order_by('-update_date')[:10]
    context = {'documents': documents}
    return render(request, 'pages/index.html', context)

def detail(request, slug):
    try:
        document = Document.objects.get(slug=slug)
    except:
        raise Http404("Wiki Page does not exist")
    return render(request, 'pages/detail.html', {'document': document})
