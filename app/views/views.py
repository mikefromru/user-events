from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/signin/')
def foo(request):
    return render(request, 'app/app.html')