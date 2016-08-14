from django.shortcuts import render, redirect
from django.conf import settings

from cats.forms import CatForm, BreedForm
#from cats.models import Cat, Breed

from model_classes.models import Cat, Breed


def index(request):
    return render(request, 'index.html')


def cats(request):
    return render(request, 'object_list.html', {'single_view_name': 'single_cat', 'objects': Cat.objects.all()})


def single_cat(request, cat_id):
    facade = settings.FACADE_CLASS()

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
