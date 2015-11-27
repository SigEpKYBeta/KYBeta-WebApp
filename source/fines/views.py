from django.shortcuts import render
from django.db.models import Sum

from accounts.models import User

from .forms import FineForm
from .models import Fine


def manage_fines(request):
    fines = Fine.objects \
                .values('user__id', 'user__first_name', 'user__last_name') \
                .annotate(total=Sum('amount')) \
                .order_by('user__last_name')
    return render(request, 'fines/manager.html', {'fines': fines})


def manage_user_fines(request, id):
    fines = Fine.objects.filter(user=id)
    return render(request, 'fines/user_manager.html', {'fines': fines})


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
