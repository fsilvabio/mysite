from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField('Data')


    def __str__(self):
        return self.nome + ' - ' + str(self.data_nascimento)

    