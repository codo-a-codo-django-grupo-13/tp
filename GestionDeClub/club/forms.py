from django import forms

from .models import Disciplina, Profe, Socio


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        #fields = "__all__"
        fields = ['nombre', 'cuota', 'horarios', 'profe']
        widgets = {
            'horarios': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
    #profesores = forms.ChoiceField(label="Profesor", choices=PROFESORES, required=False)

    def __init__(self, *args, **kwargs):
        super(DisciplinaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ProfeForm(forms.ModelForm):
    class Meta:
        model = Profe
        fields = ['nombre', 'apellido', 'dni', 'email', 'cuit']

    def __init__(self, *args, **kwargs):
        super(ProfeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if Profe.objects.filter(dni=dni).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este DNI ya existe para un Profe.')
        return dni

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'dni', 'email', 'numero']

    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if Socio.objects.filter(dni=dni).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este DNI ya existe para un Socio.')
        return dni

'''
from django import forms
from .models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'

    def clean_dni(self):
        dni = self.cleaned_data['dni']
        if Socio.objects.filter(dni=dni).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este DNI ya existe para un Socio.')
        return dni
'''
