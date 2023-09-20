from django import forms
from base.models import Contato, ReservaBanho

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
    
class ReservaBanhoForm(forms.ModelForm):
    class Meta:    
        model = ReservaBanho
        fields = ['petnome', 'telefone', 'datareserva', 'observacoes']
        labels = {
            'petnome': 'Nome do Pet',
            'telefone': 'Telefone',
            'datareserva': 'Data da Reserva',
            'observacoes': 'Observações'
        }