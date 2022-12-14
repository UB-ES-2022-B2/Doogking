from django.db import models
from django.contrib.auth.models import AbstractUser
from storages.backends.azure_storage import AzureStorage

from .managers import ProfileManager


class Profile(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    otp = models.CharField(max_length=32, blank=True)
    image = models.ImageField(
            storage=AzureStorage,
            upload_to='profile/',
            default='profile/default.svg'
        )
    balance = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return self.email


class Housing(models.Model):
    house_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    street_number = models.CharField(max_length=25)
    floor = models.CharField(max_length=25, blank=True)
    door = models.CharField(max_length=25, blank=True)
    house_dimension = models.IntegerField()
    price = models.IntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=5, decimal_places=4)
    num_ratings = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    house_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return " ".join([self.city, self.street, self.street_number])

    @property
    def house_owner_name(self):
        return " ".join(
            [self.house_owner.first_name,
             self.house_owner.last_name]
        )

    @property
    def image(self):
        return str(
            HousingImage.objects.
            filter(housing=self).
            get(index=0).image.url
        )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=-1) & models.Q(rating__lte=5),
                name="The rating value must be "
                     "-1 (unrated) or an integer "
                     "between 0 and 5",
            ),
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name="Price must be a positive integer",
            )
        ]


class HousingImage(models.Model):
    id = models.AutoField(primary_key=True)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    image = models.ImageField(storage=AzureStorage, default='default.svg')

    def __str__(self):
        return " ".join([str(self.housing), str(self.index), str(self.image)])


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return " ".join(
            [str(self.housing),
             str(self.start_date),
             "--",
             str(self.end_date)])


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)

    def __str__(self):
        return " ".join([str(self.user), "--", str(self.housing)])
