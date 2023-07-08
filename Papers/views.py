from django.shortcuts import render, redirect
from .forms import PaperForm
from .models import Paper

def papers(request):
    papers = Paper.objects.all()
    context = {
        'papers': papers
    }
    return render(request, 'papers.html', context)

def add_paper(request):
    form = PaperForm()
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('papers') 
    else:
        return render(request, 'add_paper.html', {'form': form})