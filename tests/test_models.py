from django.test import TestCase
from doogkingapp.models import Profile


class ModelsTestCase(TestCase):

    def create_Profile(self):
        return Profile.objects.create_user(email="test@gmail.com", password="Password123")

    def test_profile_creation(self):
        user = self.create_Profile()
        self.assertTrue(isinstance(user, Profile))
        self.assertEqual(user.__str__(), user.email)

    def create_superuser(self):
        return Profile.objects.create_superuser(email="superusertest@gmail.com", password="Password123", is_staff=True,
                                                is_superuser=True, is_active=True)

    def test_superuser_creation(self):
        super_user = self.create_superuser()
        self.assertTrue(isinstance(super_user, Profile))
        self.assertEqual(super_user.__str__(), super_user.email)

    def test_wrong_email(self):
        with self.assertRaises(ValueError) as ex:
            Profile.objects.create_user(email="testgmailcom", password="Password123")
        self.assertEqual('The email is not correct', str(ex.exception))

    def test_wrong_password_length(self):
        with self.assertRaises(ValueError) as ex:
            Profile.objects.create_user(email="test@gmail.com", password="Pass")
        self.assertEqual('Password length should be at least 8', str(ex.exception))

    def test_wrong_password_number(self):
        with self.assertRaises(ValueError) as ex:
            Profile.objects.create_user(email="test@gmail.com", password="Passwordasdf")
        self.assertEqual('Password should have at least one number', str(ex.exception))

    def test_wrong_password_uppercase(self):
        with self.assertRaises(ValueError) as ex:
            Profile.objects.create_user(email="test@gmail.com", password="password123")
        self.assertEqual('Password should have at least one uppercase letter', str(ex.exception))

    def test_wrong_password_lowercase(self):
        with self.assertRaises(ValueError) as ex:
            Profile.objects.create_user(email="test@gmail.com", password="PASSWORD123")
        self.assertEqual('Password should have at least one lowercase letter', str(ex.exception))
