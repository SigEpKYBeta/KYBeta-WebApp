from django.db import models
from accounts.models import User


class Fine(models.Model):
    user = models.ForeignKey(User)
    amount = models.FloatField()
    reason = models.TextField()

    def __str__(self):
        return self.user.get_full_name() \
                + ' - ' + str(self.amount) \
                + ' - ' + self.reason
