from django.db import models

genero_choices= (
    ("t","terror"),
    ("d","drama")
)

class Sebo_discos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=200)
    ano = models.IntegerField()
    pais = models.CharField(max_length=20)
    genero = models.CharField(
        max_length=10,
        choices=genero_choices
    )
    quantidade = models.IntegerField()
    def __str__(self):
        return self.nome
