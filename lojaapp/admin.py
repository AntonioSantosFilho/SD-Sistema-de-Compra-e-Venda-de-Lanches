# lojaapp/admin.py
from django.contrib import admin
from .models import Usuario, Vendedor, Produto, Pedido, Avaliacao, Chat, Notificacao, Pagamento

admin.site.register(Usuario)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Avaliacao)
admin.site.register(Chat)
admin.site.register(Notificacao)
admin.site.register(Pagamento)
