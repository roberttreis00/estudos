from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class Produto(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque']
