from django.db import models
#from django.db import IntegrityError, models, router, transaction

class India(models.Model):
    states = models.CharField(max_length=200)
    cm = models.CharField(max_length=300)
    ministers = models.CharField(max_length=200)
    mla = models.CharField(max_length=200)

    def __str__(self):
        return self.states


class Pm(models.Model):
    india = models.ForeignKey(India, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


