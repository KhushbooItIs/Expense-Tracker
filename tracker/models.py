from django.db import models

class Expense(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200)
    amount=models.IntegerField()
    category=models.CharField()
    date=models.DateField(auto_now=True)
