class Cat(object):
    id = None

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.breed.name)


class Breed(object):
    id = None

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return self.name

