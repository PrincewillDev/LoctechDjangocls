from django import forms

class feedBackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(max_length=70)
    designation = forms.CharField(max_length=70)
    feedback = forms.CharField(widget=forms.Textarea)