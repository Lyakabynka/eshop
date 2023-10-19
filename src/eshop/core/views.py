from django.shortcuts import render, redirect
from .forms import NewCategoryForm
# Create your views here.
def landing(request):
    return render(request, 'core/index.html')

def imprint(request):
    return render(request, 'core/imprint.html') 

def create_category(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()

            return redirect('/')    
    
    else:
        form = NewCategoryForm()

    form = NewCategoryForm()

    return render(request, 'core/input/category_form.html', {
        'form': form
    })