from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='Description', max_length=100)
