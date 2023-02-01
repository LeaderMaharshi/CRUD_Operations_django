from django.shortcuts import render

# Create your views here.
def accounts(request):
    return render(request, 'crud.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')