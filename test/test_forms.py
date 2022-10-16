from django.test import TestCase
from doogkingapp.forms import ProfileCreationForm

class ProfileFormTestCase(TestCase):


    def test_profile_form(self):
       '''data = {
            'email': "prova@gmail.com",
            'password' : 'password1234'
        }
       form = ProfileCreationForm(data=data)
       self.assertTrue(form.is_valid())'''