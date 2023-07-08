from Branches.models import Branch


def context_processors(request):
    branches = Branch.objects.all()
    return {'branches': branches}