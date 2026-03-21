from django.forms import ModelForm
from .models import Expense

class Expenseform(ModelForm):
    class Meta:
        model=Expense
        fields=('name','amount','category')
