from django.test import TestCase
from .models import Student,Animal
from django.shortcuts import reverse


# Create your tests here.

class SimpleTests(TestCase):
    def test_empty(self):
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(response.context['students'])

class AnimalTestCase(TestCase):
    def setUp(self) -> None:
        print('Setting up.')
        Animal.objects.create(name='lion',sound='roar')
        Animal.objects.create(name='cat',sound='meow')

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name='lion')
        cat = Animal.objects.get(name='cat')
        self.assertEqual(lion.speak(),'The lion says \"roar\"')
        self.assertEqual(cat.speak(),'The cat says \"meow\"')
