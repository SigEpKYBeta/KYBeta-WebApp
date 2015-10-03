from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class SigEpUserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None):
		user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
		user.is_active = True
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, last_name, password):
		user = self.create_user(email, first_name, last_name, password)
		user.is_staff = True
		user.save(using=self._db)
		return user
		
class SigEpUser(AbstractBaseUser):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True, null=False)
	is_staff = models.BooleanField(default=False, null=False)

	objects = SigEpUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'
		
	def get_full_name(self):
		return self.first_name + " " + self.last_name

	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	def __unicode__(self):
		return self.email


