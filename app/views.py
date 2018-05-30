from django.shortcuts import render, redirect
from . import models, forms
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        #context
    })

def freezers(request):
    allFreezers = models.Freezer.objects.all()
    form = forms.ShowFreezersForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['ordering']:
            allFreezers = allFreezers.order_by(form.cleaned_data['ordering'])
    return render(request, 'freezers.html', {
        'form': form,
        'freezers_list': allFreezers,
    })

def tvs(request):
    allTVs = models.TV.objects.all()
    form = forms.ShowTVsForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['ordering']:
            allTVs = allTVs.order_by(form.cleaned_data['ordering'])
    return render(request, 'tvs.html', {
        'form': form,
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
