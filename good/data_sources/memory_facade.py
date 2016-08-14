class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
            cls._instance.clear()

        return cls._instance


class DataFacade(Singleton):
    cats = None
    breeds = None

    def clear(self):
        self.cats = {}
        self.breeds = {}

    @staticmethod
    def set_obj_id(obj, store):
        if obj.id is None:
            if len(store) == 0:
                obj.id = 1
                return
            obj.id = max(o.id for o in store.itervalues()) + 1

    def get_cat(self, cat_id):
        return self.cats[cat_id]

    def put_cat(self, cat):
        self.set_obj_id(cat, self.cats)
        self.put_breed(cat.breed)
        self.cats[cat.id] = cat
        return cat.id

    def get_all_cats(self):
        return self.cats.values()

    def get_breed(self, breed_id):
        return self.breeds[breed_id]

    def put_breed(self, breed):
        self.set_obj_id(breed, self.breeds)
        self.breeds[breed.id] = breed
        return breed.id

    def get_all_breeds(self):
        return self.breeds.values()
