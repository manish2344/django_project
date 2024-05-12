# myapp/tests.py
from django.test import TestCase
from .models import MyModel
from .forms import MyForm
from django.urls import reverse

class MyModelTestCase(TestCase):
    def setUp(self):
        self.obj = MyModel.objects.create(name='Test Model', value=100)

    def test_custom_method(self):
        self.assertEqual(self.obj.name, 'Test Model')

class MyViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world")

class MyFormTestCase(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'Test', 'value': 123}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())
