from django import forms

from .models import Concerto, Palco


class ConcertoForm(forms.ModelForm):
    class Meta:
        model = Concerto
        fields = ["dia", "hora", "banda", "palco"]


class PalcoForm(forms.ModelForm):
    class Meta:
        model = Palco
        fields = ['nome', 'capacidade', 'imagem', 'acessibilidade_mobilidade_reduzida']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'acessibilidade_mobilidade_reduzida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
