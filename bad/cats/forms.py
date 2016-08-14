from django.forms import ModelForm

from cats.models import Cat, Breed


class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed']


class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = ['name']
