from django import forms

class CreateStudentForm(forms.Form):
     name = forms.CharField(max_length=100, label='Student_name')