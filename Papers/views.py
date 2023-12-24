from django.shortcuts import render, redirect
from .forms import PaperForm
from .models import Paper
from django.contrib import messages
from Products.models import Product

def papers(request):
    papers = Paper.objects.all()
    context = {
        'papers': papers
    }
    return render(request, 'papers.html', context)

def add_paper(request):
    form = PaperForm()
    form.fields['product'].queryset = Product.objects.filter(Type='Paper')
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('papers') 
    else:
        return render(request, 'add_paper.html', {'form': form})

def edit_paper(request, paper):
    paper = Paper.objects.get(id=paper)
    form = PaperForm(instance=paper)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('papers')
    else:
        return render(request, 'edit_paper.html', context)


def delete_paper(request, paper):
    paper = Paper.objects.get(id=paper)
    paper.delete()
    message = f'Deleted {paper} successfully!'
    messages.success(request, message)
    return redirect('papers')