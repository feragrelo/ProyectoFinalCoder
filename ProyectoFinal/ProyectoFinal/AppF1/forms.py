from django import forms


class PilotosFormulario(forms.Form):

    nombre = forms.CharField()
    nacionalidad = forms.CharField()
    fecha_nacimiento=forms.DateField()
    
class ConstructoresFormulario(forms.Form):

    nombre = forms.CharField()
    nacionalidad = forms.CharField()
    email=forms.EmailField()
    
class CircuitosFormulario(forms.Form):

    nombre = forms.CharField()
    país = forms.CharField()
    año_primer_carrera=forms.DateField()
    
    