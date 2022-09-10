from django.db import models

COMPANY_CHOICE = [
   ('RELIANCE' , 'RELIANCE'),
   ('SBIN' , 'SBIN'),
   ('INFY', 'INFY')
]

class Company(models.Model):
    symbol = models.CharField(max_length = 30 ,blank=True, choices=COMPANY_CHOICE)
    

    def __str__(self):
       return self.name