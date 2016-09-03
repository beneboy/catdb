import sys

sys.path.append('frontend')

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frontend.settings")

import unittest
import mock

import django
django.setup()

from cats import views as cat_views


class BreedViewTest(unittest.TestCase):
    def setUp(self):
        self.data_facade = mock.Mock()
        facade_patcher = mock.patch("cats.views.settings.FACADE_CLASS", return_value=self.data_facade)
        facade_patcher.start()

        render_patcher = mock.patch("cats.views.render")
        self.mock_render = render_patcher.start()

        breed_form_patcher = mock.patch("cats.views.BreedForm")
        self.breed_form = breed_form_patcher.start()

    def test_breed_list(self):
        request = mock.Mock()
        expected_response = self.mock_render.return_value

        expected_context = {
            'single_view_name': 'single_breed',
            'objects': self.data_facade.get_all_breeds.return_value
        }

        actual_response = cat_views.breeds(request)

        self.assertEqual(actual_response, expected_response)
        self.mock_render.assert_called_with(request, 'object_list.html', expected_context)

    def test_single_breed_get_existing(self):
        request = mock.Mock()
        expected_response = self.mock_render.return_value

        breed_id = '42'

        expected_initial = {
            'name': self.data_facade.get_breed.return_value.name
        }

        expected_context = {
            'form': self.breed_form.return_value,
            'nice_name': 'Breed'
        }

        actual_response = cat_views.single_breed(request, breed_id)

        self.breed_form.assert_called_with(initial=expected_initial)
        self.data_facade.get_breed.assert_called_with(42)
        self.mock_render.assert_called_with(request, 'single_object.html', expected_context)

        self.assertEqual(actual_response, expected_response)

    def test_single_breed_get_new(self):
            request = mock.Mock()
            expected_response = self.mock_render.return_value

            breed_id = 'new'

            expected_initial = {
                'name': ''
            }

            expected_context = {
                'form': self.breed_form.return_value,
                'nice_name': 'Breed'
            }

            actual_response = cat_views.single_breed(request, breed_id)

            self.breed_form.assert_called_with(initial=expected_initial)
            self.assertFalse(self.data_facade.get_breed.called)
            self.mock_render.assert_called_with(request, 'single_object.html', expected_context)

            self.assertEqual(actual_response, expected_response)
