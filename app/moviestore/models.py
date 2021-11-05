from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                        PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Category(models.Model):
    """Category to be used in a movie"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Actor(models.Model):
    """Actor to be used in a movie"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Movie to be used in our store"""
    title = models.CharField(max_length=255)
    year = models.IntegerField(default=2018)
    summary = models.TextField(max_length=1000, blank=True)
    categories = models.ManyToManyField('Category')
    actors = models.ManyToManyField('Actor')
    Rent_date = models.DateField(default=timezone.now)
    Return_date = models.DateField(default=timezone.now)
    user_charge = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    first_three_days_cost = 1
    extra_days_cost = 0.5

    def find_rent_days(self, *args, **kwargs):
        """Calculate the days a user used a movie"""
        return ((self.Return_date - self.Rent_date).days)

    def calculate_charge(self, *args, **kwargs):
        """Calculate user's charge for a movie he/she rent"""
        rent_days = self.find_rent_days()

        if rent_days <= 3:
            self.user_charge = rent_days*self.first_three_days_cost
        else:
            self.user_charge = (
                                (rent_days-3) * self.extra_days_cost + 3 *
                                self.first_three_days_cost
                                )

    def __str__(self):
        return self.title
