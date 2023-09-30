from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def eshop(request):
    return render(request, 'core/eshop.html')