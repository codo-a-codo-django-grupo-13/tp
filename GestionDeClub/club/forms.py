from django import forms


class DisciplinaForm(forms.Form):
    nombre = forms.CharField(label="Nombre")
    cuota = forms.IntegerField(label="Cuota", required=False)
    horarios = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'