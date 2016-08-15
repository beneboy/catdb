from django.shortcuts import render, redirect
from django.conf import settings

from cats.forms import CatForm, BreedForm
#from cats.models import Cat, Breed

from model_classes.models import Cat, Breed


def index(request):
    return render(request, 'index.html')


def cats(request):
    facade = settings.FACADE_CLASS()
    all_cats = facade.get_all_cats()

    return render(request, 'object_list.html', {'single_view_name': 'single_cat', 'objects': all_cats})


def single_cat(request, cat_id):
    facade = settings.FACADE_CLASS()

    if cat_id != 'new':
        cat = facade.get_cat(int(cat_id))
    else:
        cat = None

    form_initial = {'name': getattr(cat, 'name', ''), 'breed': getattr(getattr(cat, 'breed', ''), 'id', None)}

    breeds = facade.get_all_breeds()
    breed_choices = [(breed.id, breed.name) for breed in breeds]

    if request.method == 'POST':
        form = CatForm(request.POST, initial=form_initial)
        form.fields['breed'].choices = breed_choices
        if form.is_valid():
            breed = facade.get_breed(int(form.cleaned_data['breed']))
            c = Cat(form.cleaned_data['name'], breed)
            if cat_id != 'new':
                c.id = int(cat_id)
            facade.put_cat(c)
            return redirect('cat_list')
    else:
        form = CatForm(initial=form_initial)

        form.fields['breed'].choices = breed_choices

    return render(request, 'single_object.html', {'form': form, 'nice_name': 'Kitty'})


def breeds(request):
    facade = settings.FACADE_CLASS()
    all_breeds = facade.get_all_breeds()

    return render(request, 'object_list.html', {'single_view_name': 'single_breed', 'objects': all_breeds})


def single_breed(request, breed_id):
    facade = settings.FACADE_CLASS()

    if breed_id != 'new':
        breed = facade.get_breed(int(breed_id))
    else:
        breed = None

    form_initial = {'name': getattr(breed, 'name', '')}

    if request.method == 'POST':
        form = BreedForm(request.POST, initial=form_initial)
        if form.is_valid():
            b = Breed(form.cleaned_data['name'])
            if breed_id != 'new':
                b.id = int(breed_id)
            facade.put_breed(b)
            return redirect('breed_list')
    else:
        form = BreedForm(initial=form_initial)

    return render(request, 'single_object.html', {'form': form, 'nice_name': 'Breed'})
