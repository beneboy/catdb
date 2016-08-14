from django.forms import Form, CharField, ChoiceField


class CatForm(Form):
    name = CharField()
    breed = ChoiceField(choices=[])


class BreedForm(Form):
    name = CharField()
