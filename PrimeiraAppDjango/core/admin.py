from django.contrib import admin


from .models import Produtos, Cliente
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produtos, ProdutoAdmin)
admin.site.register(Cliente, ClientAdmin)