from django.shortcuts import render, redirect
from .forms import ExpenseForm

def expenses(request):
    return render(request, 'expenses.html')

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