from django import forms

class MatrixInput2x2(forms.Form):
    a11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

class MatrixInput3x3(forms.Form):
    a11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))