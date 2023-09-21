from django import forms
from .models import *

from .models import *

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = ['name','group','course']