from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .choices import GENDER

# class UserManager(BaseUserManager):
#     #.................Create our custom user................
#     def create_user(self, first_name, last_name, email, username, password = None, is_active = True, is_admin = False, is_staff = False):
#         if not email:
#             raise ValueError("A user must have an email")
#         if not username:
#             raise ValueError("A user must have a username")
#         # if not phone:
#         #     raise ValueError("A user must have a phone number")
#         if not password:
#             raise ValueError("users must have a password")

#         if not first_name:
#             raise ValueError("users must have a fist name")

#         if not last_name:
#             raise ValueError("users must have a last name")

#         #.................Modeling our required fields...................
#         user = self.model(
#             first_name  = first_name,
#             last_name   = last_name,
#             email       = self.normalize_email(email),
#             username    = username,
#         ) 

#         user.set_password(password)
#         user.admin  = is_admin
#         user.active = is_active
#         user.staff  = is_staff
#         user.save(using = self._db)
#         return user

#     #................Creating a stsff user.......................
#     def create_staffuser(self, first_name, last_name, email, username, password = None):
#         user = self.create_user(
#             first_name,
#             last_name,
#             email,
#             username,
#             password = password,
#             is_staff = True,
#         )
#         return user

#     #..................Creating a superuser.......................
#     def create_superuser(self, first_name, last_name, email, username, password):
#         user = self.create_user(
#             first_name  = first_name,
#             last_name   = last_name,
#             email       = self.normalize_email(email),
#             username    = username,
#             password    = password,
#         )

#         user.admin   = True
#         user.active  = True
#         user.staff   = True
#         user.save(using = self._db)
#         return user





# class User(AbstractBaseUser):
#     email       = models.EmailField(unique = True)
#     username    = models.CharField(max_length = 100, unique = True)
#     first_name  = models.CharField(max_length = 100, blank = True)
#     last_name   = models.CharField(max_length = 100, blank = True, null = None)
#     sex         = models.CharField(max_length = 10, choices = GENDER)
#     date_created= models.DateTimeField(auto_now_add = True)
#     last_login  = models.DateTimeField(auto_now_add = True)
#     admin       = models.BooleanField(default = False)
#     staff       = models.BooleanField(default = False)
#     active      = models.BooleanField(default = True)



#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

#     objects = UserManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.email

#     def get_shorn_name(self):
#         return self.email
    
#     def has_perm(self, perm, obj = None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_active(self):
#         return self.active

#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_staff(self):
#         return self.staff