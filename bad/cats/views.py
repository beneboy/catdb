from django.shortcuts import render, redirect

from cats.forms import CatForm, BreedForm
from cats.models import Cat, Breed


def index(request):
    return render(request, 'index.html')


def cats(request):
    return render(request, 'object_list.html', {'single_view_name': 'single_cat', 'objects': Cat.objects.all()})


def single_cat(request, cat_id):
    if cat_id != 'new':
        cat = Cat.objects.get(id=cat_id)
    else:
        cat = None

    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)

    return render(request, 'single_object.html', {'form': form, 'nice_name': 'Kitty'})


def breeds(request):
    return render(request, 'object_list.html', {'single_view_name': 'single_breed', 'objects': Breed.objects.all()})


def single_breed(request, breed_id):
    if breed_id != 'new':
        breed = Breed.objects.get(id=breed_id)
    else:
        breed = None

    if request.method == 'POST':
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            return redirect('breed_list')
    else:
        form = BreedForm(instance=breed)

    return render(request, 'single_object.html', {'form': form, 'nice_name': 'Breed'})
