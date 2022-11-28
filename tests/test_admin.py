from django.test import TestCase, Client
from doogkingapp.models import Profile


class SuperUserTestCase(TestCase):

    def create_superuser(self):
        return Profile.objects.create_superuser(email="superusertest@gmail.com",
                                                password="Password123", is_staff=True,
                                                is_superuser=True, is_active=True)

    def test_superuser(self):
        admin = self.create_superuser()
        client = Client()
        client.login(username=admin.email, password=admin.password)

        data_housing = {
            "city": "Barcelona",
            "street": "Gran Via de les Corts Catalanes",
            "street_number": "580",
            "floor": "Planta Baixa",
            "door": "La gran del mig",
            "house_dimension": 10836,
            "house_owner": "http://localhost:8000/api/profiles/1/"}

        client.post("/api/housing/", data_housing)
        '''super_user_pages = []        #lista a llenar con los endpoints de un superuser
        for page in super_user_pages:
            resp = client.get(page)
            assert resp.status_code == 200
            assert "<!DOCTYPE html" in resp.content'''
