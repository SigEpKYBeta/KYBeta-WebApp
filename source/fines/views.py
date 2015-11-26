from django.shortcuts import render

from accounts.models import User

from .forms import FineForm
from .models import Fine


def add_fine(request):
    if request.method == 'POST':
        fine_form = FineForm(request.POST)
        if fine_form.is_valid():
            users = request.POST.getlist('users')
            amount = request.POST['amount']
            reason = request.POST['reason']
            for user_id in users:
                user = User.objects.get(id=user_id)
                fine = Fine(user=user, amount=amount, reason=reason)
                fine.save()
    else:
        fine_form = FineForm()
    return render(request, 'fines/add.html', {'form': fine_form})
