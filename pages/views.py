from django.shortcuts import render
from .models import Document

def index(request):
    documents = Document.objects.order_by('-update_date')[:10]
    context = {'documents': documents}
    return render(request, 'pages/index.html', context)
