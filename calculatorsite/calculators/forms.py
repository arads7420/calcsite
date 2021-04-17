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


class MatrixInput4x4(forms.Form):
    a11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a14 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

    a21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a24 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    a31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a34 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    a41 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a42 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a43 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a44 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b14 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

    b21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b24 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b34 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b41 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b42 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b43 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b44 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

class MatrixInput5x5(forms.Form): 
    a11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a14 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a15 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

    a21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a24 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a25 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    a31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a34 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a35 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    a41 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a42 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a43 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a44 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a45 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    a51 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a52 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a53 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a54 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a55 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b14 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b15 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

    b21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b24 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b25 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b34 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b35 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b41 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b42 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b43 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b44 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b45 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    
    b51 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b52 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b53 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b54 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    b55 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

class SingleMatrix2x2(forms.Form):
    a11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))

class SingleMatrix3x3(forms.Form):
    a11 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a12 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a13 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a21 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a22 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a23 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a31 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a32 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))
    a33 = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'matrix-element'}))