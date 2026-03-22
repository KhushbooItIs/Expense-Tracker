from django.shortcuts import render,redirect
from .forms import Expenseform
from .models import Expense
from django.db.models import Sum

def index(request):
    if request.method=="POST":
        expense=Expenseform(request.POST)
        if expense.is_valid():
            expense.save()
    expenses=Expense.objects.all()
    total_expense=expenses.aggregate(Sum("amount"))['amount__sum']
    print(total_expense)
    expense_form=Expenseform()
    return render( request,'tracker/index.html',{'expense_form':expense_form,'expenses':expenses,'total_expense':total_expense})


def edit(request,id):
   
    expense=Expense.objects.get(id=id)
    expense_form=Expenseform(instance=expense)
    if request.method=="POST":
        form = Expenseform(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'tracker/edit.html',{'expense_form':expense_form})


def delete(request,id):
  if request.method=="POST":
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('index')