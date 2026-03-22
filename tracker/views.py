from django.shortcuts import render
from .forms import Expenseform
from .models import Expense

def index(request):
    if request.method=="POST":
        expense=Expenseform(request.POST)
        if expense.is_valid():
            expense.save()
    expenses=Expense.objects.all()
    expense_form=Expenseform()
    return render( request,'tracker/index.html',{'expense_form':expense_form,'expenses':expenses})
