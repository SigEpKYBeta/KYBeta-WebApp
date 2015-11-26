from django import forms
from django.contrib.auth.models import Group


class FineForm(forms.Form):
    users = forms.ModelMultipleChoiceField(
        Group.objects.get(name='Active Brother').user_set.all())
    amount = forms.FloatField()
    reason = forms.CharField(widget=forms.Textarea)
