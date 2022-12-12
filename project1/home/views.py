from django.shortcuts import render
from .models import detail,feature,Doc

# Create your views here.
def index(request):
    dict_doc ={
        'doc':Doc.objects.all()
    }
    return render(request,'index.html',dict_doc)
def abouts(request):
    dict_about ={
        "abt": feature.objects.all()
    }
    return render(request,'abouts.html',dict_about)
def details(request):
    dict_det = {
        'det': detail.objects.all()
    }
    return render(request,'details.html',dict_det) 
