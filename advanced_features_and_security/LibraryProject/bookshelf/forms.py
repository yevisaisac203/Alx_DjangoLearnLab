from django import forms

# Simple example form (for CSRF and form demonstration)
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
