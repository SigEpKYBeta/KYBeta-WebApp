from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from accounts.models import User

from .forms import FineForm
from .models import Fine


def set_fine_status(fine, status='UNPAID'):
    fine.status = status
    fine.save()


def manage_fines(request):
    fines = Fine.objects.unpaid_fines()
    return render(request, 'fines/manager.html', {'fines': fines})


def manage_user_fines(request, id):
    fines = Fine.objects.filter(user=id, status='UNPAID')
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
                fine = Fine(user=user, amount=amount,
                            status='UNPAID', reason=reason)
                fine.save()
    else:
        fine_form = FineForm()
    return render(request, 'fines/add.html', {'form': fine_form})


@ensure_csrf_cookie
def paid_status(request):
    fine_ids = request.POST.getlist('fines[]')
    for fine_id in fine_ids:
        fine = Fine.objects.get(id=fine_id)
        set_fine_status(fine, 'PAID')
    return JsonResponse({'status': 'OK'})
