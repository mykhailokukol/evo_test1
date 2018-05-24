from django.shortcuts import render, redirect
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html', {

    })

def freezers(request):
    allFreezers = models.Freezer.objects.all().order_by('id')
    return render(request, 'freezers.html', {
        'freezers_list': allFreezers,
    })

def tvs(request):
    allTVs = models.TV.objects.all().order_by('id')
    return render(request, 'tvs.html', {
        'tvs_list': allTVs,
    })

def add_tv(request, pk):
    item = get_object_or_404(models.TV, pk=pk)
    item.clicks += 1
    item.save()
    return redirect('/tvs/')

def add_freezer(request, pk):
    item = get_object_or_404(models.Freezer, pk=pk)
    item.clicks += 1
    item.save()
    return redirect('/freezers/')
