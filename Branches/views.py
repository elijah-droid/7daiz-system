from django.shortcuts import render, redirect
from .models import Branch
from django.contrib import messages

def switch_branch(request, branch):
    branch = Branch.objects.get(id=branch)
    try:
        request.user.admin.current_branch = branch
        request.user.admin.save()
        request.user.employee.Branch = branch
        request.user.employee.save()
        recent = request.META['HTTP_REFERER']
        messages.success(request, f"You are now operating {branch.Name}'s Branch")
        return redirect(recent)
    except:
        messages.success(request, 'You are not an administrator')
        recent = request.META['HTTP_REFERER']
        return redirect(recent)