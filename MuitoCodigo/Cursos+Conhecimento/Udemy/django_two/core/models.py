from django.db import models
from stdimage import StdImageField, JPEGField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

'''
Link de como usar o modulo para upar imagens 
https://github.com/codingjoe/django-stdimage#migration-instructions
'''


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('ImagemBacana', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


# Isso aqui pega nome tipo "nome assim tipo" e transforma em "nome-assim-tipo"
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
