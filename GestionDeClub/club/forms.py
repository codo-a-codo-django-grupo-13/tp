from django import forms


class DisciplinaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    #horarios = forms.Textarea(label="Horarios")
    cuota = forms.IntegerField(label="Cuota")