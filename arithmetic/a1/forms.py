from django import forms

class ExpressionForm(forms.Form):
    expression = forms.CharField(label='Arithmetic Expression', max_length=100)