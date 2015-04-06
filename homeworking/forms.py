from django.forms import ModelForm

from .models import homework

def HomeWorkForm(ModelForm):
	class Meta:
		model = Homework