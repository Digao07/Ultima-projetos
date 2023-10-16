from django.urls import path

from rest_api.views import *

app_name = 'rest_api'

urlpatterns = [
  path('hello_world', hello_world, name='hello_world_api'),
  path('contato', listar_contatos, name='listar_contatos'),
  path('contato/<int:id>', obter_contato_pelo_id, name="obter_contato"),
  path('reservadebanho/', reservadebanho, name='reservadebanho'),
  path('adicionar_banho/', adicionar_banho, name='adicionar_banho'),
  path('quantidade_de_letras_pet/', quantidade_de_letras_pet, name='quantidade_de_letras_pet'),
  path('dias_reserva_banho_ate_fim_do_ano/', dias_reserva_banho_ate_fim_do_ano, name='dias_reserva_banho_ate_fim_do_ano')

]

