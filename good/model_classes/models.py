class ModelBase(object):
    def __eq__(self, other):
        return type(self) == type(other) and self.id == other.id


class Cat(ModelBase):
    id = None

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.breed.name)


class Breed(ModelBase):
    id = None

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return self.name

