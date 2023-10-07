from django.db import models

genero_choices= (
    ("t","terror"),
    ("d","drama")
)
class selo_fonografico(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class artista(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
class Sebo_discos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    selo_fonografico = models.ForeignKey(selo_fonografico,on_delete=models.CASCADE)
    ano = models.IntegerField()
    pais = models.CharField(max_length=20)
    genero = models.CharField(
        max_length=10,
        choices=genero_choices
    )
    quantidade = models.IntegerField()
    artistas = models.ManyToManyField(artista)
    
    def __str__(self):
        return self.nome
