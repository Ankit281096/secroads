from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/secroads.html')

def department(request):
    return render(request, 'accounts/department.html')