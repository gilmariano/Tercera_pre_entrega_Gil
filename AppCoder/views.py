from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Model1, Model2, Model3
from .forms import Model1Form, Model2Form, Model3Form

def model1_create(request):
    form = Model1Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('model1_search')
    return render(request, 'AppCoder/model1_create.html', {'form': form})

def model1_search(request):
    data = Model1.objects.all()
    return render(request, 'AppCoder/model1_search.html', {'data': data})

def model2_create(request):
    form = Model2Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('model2_search')
    return render(request, 'AppCoder/model2_create.html', {'form': form})

def model2_search(request):
    data = Model2.objects.all()
    return render(request, 'AppCoder/model2_search.html', {'data': data})

def model3_create(request):
    form = Model3Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('model3_search')
    return render(request, 'AppCoder/model3_create.html', {'form': form})

def model3_search(request):
    data = Model3.objects.all()
    return render(request, 'AppCoder/model3_search.html', {'data': data})

def home(request):
    return redirect('model1_create')

def search(request):
    query = request.GET.get('q')
    if query:
        model1_results = Model1.objects.filter(Q(field1__icontains=query) | Q(field2__icontains=query))
        model2_results = Model2.objects.filter(Q(field1__icontains=query) | Q(field2__icontains=query))
        model3_results = Model3.objects.filter(Q(field1__icontains=query) | Q(field2__icontains=query))
    else:
        model1_results = Model1.objects.none()
        model2_results = Model2.objects.none()
        model3_results = Model3.objects.none()
    return render(request, 'search_results.html', {
        'query': query,
        'model1_results': model1_results,
        'model2_results': model2_results,
        'model3_results': model3_results,
    })
