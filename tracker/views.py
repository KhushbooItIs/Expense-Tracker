from django.shortcuts import render
from .forms import Expenseform

def index(request):
    if request.method=="POST":
        expense=Expenseform(request.POST)
        if expense.is_valid():
            expense.save()
      
    expense_form=Expenseform()
    return render( request,'tracker/index.html',{'expense_form':expense_form})
