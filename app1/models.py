from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
#from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def create_user(self, email, Phone, Address, password=None):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, Phone=Phone, Address=Address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, Phone, Address, password=None):
        """Create and save a SuperUser with the given email and password."""
        user = self.model(email=email, Phone=Phone, Address=Address)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    Phone = models.IntegerField()
    Address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Phone','Address']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
