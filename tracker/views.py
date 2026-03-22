from django.shortcuts import render,redirect
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