from django.db import models


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"Acessório: {self.descricao} | ID: {self.id}"

    class Meta:
        verbose_name = "Acessório"
        verbose_name_plural = "Acessórios"