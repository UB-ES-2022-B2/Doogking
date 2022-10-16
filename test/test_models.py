from django.test import TestCase
from doogkingapp.models import Profile

class ModelsTestCase(TestCase):

    def create_Profile(self):
        return Profile.objects.create_user(email = "test@gmail.com", password= "password123")

    def test_profile_creation(self):
        user = self.create_Profile()
        self.assertTrue(isinstance(user, Profile))
        self.assertEqual(user.__str__(), user.email)

    def create_superuser(self):
        return Profile.objects.create_superuser(email = "superusertest@gmail.com", password= "password123",is_staff= True,is_superuser= True,is_active=True)

    def test_superuser_creation(self):
        super_user= self.create_superuser()
        self.assertTrue(isinstance(super_user,Profile))
        self.assertEqual(super_user.__str__(), super_user.email)

