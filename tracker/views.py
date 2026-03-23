from django.shortcuts import render,redirect
from .forms import Expenseform
from .models import Expense
from django.db.models import Sum
import datetime

def index(request):
    if request.method=="POST":
        expense=Expenseform(request.POST)
        if expense.is_valid():
            expense.save()
    expenses=Expense.objects.all()
    total_expense=expenses.aggregate(Sum("amount"))['amount__sum']
    print(total_expense)
    expense_form=Expenseform()
    
    
    last_year=datetime.date.today()-datetime.timedelta(days=365)

    data=Expense.objects.filter(date__gt=last_year)

    yearly_sum=expenses.aggregate(Sum("amount"))['amount__sum']


    last_month=datetime.date.today()-datetime.timedelta(days=30)

    data=Expense.objects.filter(date__gt=last_month)
    monthly_sum=expenses.aggregate(Sum("amount"))['amount__sum']

    last_week=datetime.date.today()-datetime.timedelta(days=7)

    data=Expense.objects.filter(date__gt=last_week)
    weekly_sum=expenses.aggregate(Sum("amount"))['amount__sum']
         
    daily_sum = Expense.objects.filter().values('date').order_by('date').annotate(
    total=Sum('amount'))

    categorical_sums = Expense.objects.filter().values('category').annotate(
    total=Sum('amount'))
    print(categorical_sums)
    print(daily_sum)

    return render(request, 'tracker/dark-modern-index.html', {
    'expense_form': expense_form,
    'expenses': expenses,
    'total_expense': total_expense,
    'yearly_sum': yearly_sum,
    'monthly_sum': monthly_sum,
    'weekly_sum': weekly_sum,
    'daily_sum': daily_sum,
    'categorical_sums':categorical_sums,

})

def edit(request,id):
   
    expense=Expense.objects.get(id=id)
    expense_form=Expenseform(instance=expense)
    if request.method=="POST":
        form = Expenseform(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request,'tracker/modern-edit.html',{'expense_form':expense_form})


def delete(request,id):
  if request.method=="POST":
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('index')