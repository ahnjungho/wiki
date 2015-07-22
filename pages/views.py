from django.http import Http404
from django.shortcuts import render
from .models import Category, Document, Tag


def index(request):
    recent_documents = Document.objects.order_by('-update_date')[:10]

    context = {'recent_documents': recent_documents}
    return render(request, 'pages/index.html', context)


def detail(request, slug):
    try:
        document = Document.objects.get(slug=slug)
    except:
        raise Http404("Wiki Page does not exist")
    return render(request, 'pages/detail.html', {'document': document})


def category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except:
        raise Http404("Category does not exist")
    return render(request, 'pages/category.html', {'category': category})


def tag(request, slug):
    try:
        tag = Tag.objects.get(slug=slug)
    except:
        raise Http404("Tag does not exist")
    return render(request, 'pages/tag.html', {'tag': tag})
