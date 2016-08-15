import os

from shutil import rmtree

import pickle

STORE_ROOT = "/tmp/catdb"


def ensure_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


class DataFacade(object):
    _cat_root = None
    _breed_root = None

    def __init__(self):
        ensure_directory_exists(STORE_ROOT)

    @staticmethod
    def relative_store_path(store_name):
        store_path = os.path.join(STORE_ROOT, store_name)
        ensure_directory_exists(store_path)
        return store_path

    @property
    def cat_root(self):
        if self._cat_root is None:
            self._cat_root = self.relative_store_path('cats')
        return self._cat_root

    @property
    def breed_root(self):
        if self._breed_root is None:
            self._breed_root = self.relative_store_path('breeds')
        return self._breed_root

    def clear(self):
        rmtree(self.cat_root)
        rmtree(self.breed_root)  # these two lines might create the directory then delete. shrug
        self._cat_root = None
        self._breed_root = None

    @staticmethod
    def object_path(object_root, object_id):
        return os.path.join(object_root, '{}'.format(object_id))

    @staticmethod
    def set_obj_id(obj, store_path):
        if obj.id is None:
            dir_list = os.listdir(store_path)
            if len(dir_list) == 0:
                obj.id = 1
                return
            obj.id = max(map(int, dir_list)) + 1

    @staticmethod
    def store_object(object_path, obj):
        pickle.dump(obj, open(object_path, "wb"))

    @staticmethod
    def load_object(object_path):
        return pickle.load(open(object_path, "rb"))

    def get_cat(self, cat_id):
        return self.load_object(self.object_path(self.cat_root, cat_id))

    def put_cat(self, cat):
        self.set_obj_id(cat, self.cat_root)
        self.put_breed(cat.breed)
        self.store_object(self.object_path(self.cat_root, cat.id), cat)
        return cat.id

    def get_all_cats(self):
        return map(self.get_cat, os.listdir(self.cat_root))

    def get_breed(self, breed_id):
        return self.load_object(self.object_path(self.breed_root, breed_id))

    def put_breed(self, breed):
        self.set_obj_id(breed, self.breed_root)
        self.store_object(self.object_path(self.breed_root, breed.id), breed)
        return breed.id

    def get_all_breeds(self):
        return map(self.get_breed, os.listdir(self.breed_root))
