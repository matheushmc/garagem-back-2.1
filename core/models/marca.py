from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f" Marca: {self.nome.upper()} | Nacionalidade: {self.nacionalidade} | ID: {self.id}"