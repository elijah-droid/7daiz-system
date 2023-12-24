from django.shortcuts import render, redirect
from .models import Roll, LargeformatPrinting
from .forms import LargeFormatForm, RollForm
from django.utils.timezone import now

def largeformat(request):
    large_format = LargeformatPrinting.objects.filter(Date__date=now())
    context = {
        'large_format': large_format
    }
    return render(request, 'largeformat.html', context)

def calculator(request):
    rolls = Roll.objects.all()
    context = {
        'rolls': rolls
    }
    return render(request, 'calculator.html', context)


def register_largeformat(request):
    form = LargeFormatForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = LargeFormatForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            meters = data['Width_Printed'] * data['Height_Printed']
            large_print = form.save()
            large_print.Total_Meters_Printed = meters
            large_print.Amount_Expected = meters * large_print.Roll.Price_per_sq_meter
            large_print.save()
            large_print.Staff.large_format_attribute.add(large_print)
            large_print.Roll.Meters_Left -= meters
            large_print.Roll.save()
            return redirect('largeformat')
    else:
        return render(request, 'add_largeformat.html', context)


def rolls(request):
    rolls = Roll.objects.all()
    context = {
        'rolls': rolls
    }
    return render(request, 'rolls.html', context)


def add_roll(request):
    form = RollForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = RollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rolls')
    else:
        return render(request, 'add_roll.html', context)


def edit__roll(request, roll):
    roll = Roll.objects.get(id=roll)
    form = RollForm(instance=roll)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = RollForm(request.POST, instance=roll)
        if form.is_valid():
            roll = form.save()
            Roll.objects.filter(Type=roll.Type).update(Price_per_sq_meter=roll.Price_per_sq_meter)
            return redirect('rolls')
    else:
        return render(request, 'edit_roll.html', context)