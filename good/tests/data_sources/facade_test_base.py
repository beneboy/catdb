from model_classes import models


class FacadeTestBase(object):
    def test_save_retrieve_breed(self):
        expected = models.Breed('Ginger')
        b_id = self.facade.put_breed(expected)
        actual = self.facade.get_breed(b_id)

        self.assertEqual(expected, actual)

    def test_save_cat_also_saves_breed(self):
        breed = models.Breed('Tabby')
        cat = models.Cat('Thomas', breed)
        self.facade.put_cat(cat)

        actual_breed = self.facade.get_breed(breed.id)
        self.assertEqual(actual_breed, breed)

        actual_cat = self.facade.get_cat(cat.id)
        self.assertEqual(actual_cat, cat)

    def test_get_all_breeds(self):
        breeds = self.facade.get_all_breeds()
        self.assertEqual(len(breeds), 0)

        breed1 = models.Breed('Black')
        breed2 = models.Breed('White')

        self.facade.put_breed(breed1)
        self.facade.put_breed(breed2)

        breeds = self.facade.get_all_breeds()

        self.assertEqual(len(breeds), 2)

        self.assertIn(breed1, breeds)
        self.assertIn(breed2, breeds)

    def test_multiple_save_overwrites(self):
        breed = models.Breed('Black and White')
        self.facade.put_breed(breed)

        breeds = self.facade.get_all_breeds()
        self.assertEqual(len(breeds), 1)

        self.facade.put_breed(breed)

        breeds = self.facade.get_all_breeds()
        self.assertEqual(len(breeds), 1)
