from django import forms

from .models import Disciplina, Profe, Socio, Inscripcion


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

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        socio_id = kwargs.pop('socio_id', None)
        super(InscripcionForm, self).__init__(*args, **kwargs)
        if socio_id:
            socio_inscripciones = Inscripcion.objects.filter(socio_id=socio_id)
            disciplinas_excluidas = Disciplina.objects.filter(inscripcion__in=socio_inscripciones)
            self.fields['disciplina'].queryset = Disciplina.objects.exclude(id__in=disciplinas_excluidas)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'