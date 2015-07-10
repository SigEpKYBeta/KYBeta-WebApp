from django.shortcuts import render
from registration.models import SigEpUser, SigEpUserManager

from .forms import RegistrationForm 

def register(request):
	if request.method == 'POST':
		reg_form = RegistrationForm(request.POST)
		if reg_form.is_valid():
			user = SigEpUser.objects.create_user(request.POST['email'], request.POST['first_name'],
				request.POST['last_name'], request.POST['password'])
	else:
		reg_form = RegistrationForm()

	return render(request, 'register.html', {'form': reg_form})