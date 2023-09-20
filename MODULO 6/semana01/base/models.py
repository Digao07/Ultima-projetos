from django.db import models

class Contato(models.Model):
    nome = models.CharField(verbose_name = 'Nome', max_length=50)
    email = models.EmailField(verbose_name= 'Email', max_length=75)
    mensagem = models.TextField(verbose_name = 'Mansagem')
    data = models. DateTimeField(verbose_name = 'Data Envio', auto_now_add=True)
    lido = models.BooleanField(verbose_name = 'Lido', default=False, blank=True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']
    
    
class ReservaBanho(models.Model):
    petnome = models.CharField(max_length=50)
    telefone = models.IntegerField()
    datareserva = models.DateTimeField()
    observacoes = models.TextField()
    datacriacao = models. DateTimeField(auto_now_add=True)
    
