from django.db import models
from django.utils import timezone

from accounts.models import User


class FinesManager(models.Manager):

    def unpaid_fines(self):
        return self.fines_by_status('UNPAID')

    def paid_fines(self):
        return self.fines_by_status('PAID')

    def waived_fines(self):
        return self.fines_by_status('WAIVED')

    def fines_by_status(self, fine_status='UNPAID'):
        fines = self.values('user__id',
                            'user__first_name',
                            'user__last_name') \
                    .filter(status=fine_status) \
                    .annotate(total=models.Sum('amount')) \
                    .order_by('user__last_name')
        return fines


class Fine(models.Model):

    STATUS_CHOICES = (
            ('UNPAID', 'Unpaid'),
            ('PAID', 'Paid'),
            ('WAIVED', 'Waived'),
        )

    user = models.ForeignKey(User)
    amount = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reason = models.TextField()
    created = models.DateTimeField(editable=False)

    objects = FinesManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Fine, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.get_full_name() \
                + ' - ' + str(self.amount) \
                + ' - ' + self.reason
