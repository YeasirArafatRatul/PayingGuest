from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

#PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,email,full_name,phone=None,bio=None,Address=None,password=None,is_active = True,is_staff=False,is_admin=False): 
    #all the required fields must be passed as arguments
        if not email:
            raise ValueError("Put an email address")
        if not password:
            raise ValueError("Input a password")
        if not full_name:
            raise ValueError("You must add your fullname")
        user= self.model(
        	email=self.normalize_email(email),
            full_name=full_name,
        )
        user.phone = phone
        user.Address = Address
        user.bio = bio
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user 

        # user = user_object

    def create_staffuser(self,email,full_name,phone,bio,Address,password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            phone=phone,
            bio=bio,
            Address=address,
            is_staff=True
            )
        return user

    def create_superuser(self,email,full_name,phone=None,bio=None,Address=None,password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            # phone=phone,
            # bio=bio,
            # Address=address,
            is_staff=True,
            is_admin=True
            )
        return user  


# Create your models here.
class User(AbstractBaseUser):  #CustomUserClass
    email      = models.EmailField(max_length=50,unique=True)
    full_name  = models.CharField(max_length=200,blank=True,unique=True)
    phone      = models.IntegerField(null=True,blank=True)
    bio        = models.TextField(max_length=100,null=True,blank=True)
    Address    = models.CharField(max_length=100,null=True,blank=True)
    Gender     = models.CharField(max_length=1, blank = True, choices = (('1','Male'),('2','Female'),('3','Others')))

    active     = models.BooleanField(default=True)
    staff      = models.BooleanField(default=False)
    admin      = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name'] #username & password is required by django default

    objects = UserManager()

    def __str__(self):
        return self.email
        
    def __str__(self):
        return self.full_name

    # def __str__(self):
    #     return str(self.phone)
        

        

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
             


    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_level):
        return True

    @property
    def is_staff(self):
        return self.staff


    @property
    def is_admin(self):
        return self.admin


    @property
    def is_active(self):
        return self.active
    


    
