from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.utils.timezone import now

def expenses(request):
    expenses = Expense.objects.filter(Date__date=now().date(), Branch=request.user.employee.Branch)
    context = {
        'expenses': expenses
    }
    return render(request, 'expenses.html', context)

def add_expense(request):
    form = ExpenseForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.Branch = request.user.employee.Branch
            expense.save()
            request.user.employee.Branch.Expenses.add(expense)
            return redirect('expenses')
    else:
        return render(request, 'new_expense.html', context)