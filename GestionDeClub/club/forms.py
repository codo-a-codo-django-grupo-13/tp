from django import forms

PROFESORES = {
    "": "Seleccionar...",
    "1": "Arnoldo André",
    "2": "Esteban Peláez",
    "3": "Carlos Paz",
    "4": "Arturo Quick",
    "5": "Paolo Malini",
    "6": "Carla Buonanote",
    "7": "Stella Maris Boido",
}

class DisciplinaForm(forms.Form):
    nombre = forms.CharField(label="Nombre")
    cuota = forms.IntegerField(label="Cuota", required=False)
    profesores = forms.ChoiceField(label="Profesor", choices=PROFESORES, required=False)
    horarios = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
