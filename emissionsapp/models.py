from django.db import models

# Create your models here.
class Emission(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    Date_Created = models.DateField(auto_now_add=True, null=False)
    Accounting_Period = models.CharField(max_length=100, null=False)
    Scope1 = models.IntegerField(null=True)
    Scope2 = models.IntegerField(null=True)
    Scope3 = models.IntegerField(null=True)