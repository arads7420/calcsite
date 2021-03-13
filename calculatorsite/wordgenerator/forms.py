from django import forms

class QueryForm(forms.Form):
    query_input = forms.CharField(label="Enter words", max_length=100)