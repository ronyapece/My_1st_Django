from django import forms
from sharad_app.models import Tasklist


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task', 'done']