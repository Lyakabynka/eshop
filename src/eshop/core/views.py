from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewCategoryForm, NewRoleForm, NewOrderForm
from .forms import NewUserItemForm,SignupForm, NewItemForm,NewDiscountForm, NewDeliveryDataForm
from .models import User, Item, Category, Role
from django.db.models import Q
from .forms import NewWishedItemUserForm,NewOwnedItemUserForm,NewOrderUserForm, NewOrderItemForm

# Create your views here.
def landing(request):
    return render(request, 'core/index.html')

def imprint(request):
    return render(request, 'core/imprint.html') 

def forms_main(request):
    return render(request, 'core/input/main_form_page.html')

def create_category(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()

            return redirect('/successful_operation')
    
    else:
        form = NewCategoryForm()

    return render(request, 'core/input/category_form.html', {
        'form': form
    })

def create_role(request):
    if request.method == 'POST':
        form = NewRoleForm(request.POST, request.FILES)

        if form.is_valid():
            role = form.save(commit=False)
            role.save()

            return redirect('/successful_operation')
    
    else:
        form = NewRoleForm()

    return render(request, 'core/input/roles_form.html', {
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            return redirect('/successful_operation')
    else:
        form = SignupForm()

    return render(request, 'core/input/users_form.html', {
        'form': form
    })

def create_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            item = form.save()
            item.save()

            return redirect('/successful_operation')
    else:
        form = NewItemForm()

    return render(request, 'core/input/items_form.html', {
        'form': form
    })

def create_discount(request):
    if request.method == 'POST':
        form = NewDiscountForm(request.POST)

        if form.is_valid():
            discount = form.save()
            discount.save()

            return redirect('/successful_operation')
    else:
        form = NewDiscountForm()

    return render(request, 'core/input/discount_form.html', {
        'form': form
    })

def create_order(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            order.save()

            return redirect('/successful_operation')
    else:
        form = NewOrderForm()

    return render(request, 'core/input/orders_form.html', {
        'form': form
    })

def create_delivery_data(request):
    if request.method == 'POST':
        form = NewDeliveryDataForm(request.POST)

        if form.is_valid():
            delivery_data = form.save()
            delivery_data.save()

            return redirect('/successful_operation')
    else:
        form = NewDeliveryDataForm()

    return render(request, 'core/input/delivery_data_form.html', {
        'form': form
    })

def create_user_item(request):
    if request.method == 'POST':
        form = NewUserItemForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['users']
            item = form.cleaned_data['items']
            
            user.cart_items.add(item)

            return redirect('/successful_operation')
    else:
        form = NewUserItemForm()
    
    return render(request, 'core/input/user_item_form.html', {
        'form': form
    })

def create_user_order(request):
    if request.method == 'POST':
        form = NewOrderUserForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data['users']
            order = form.cleaned_data['orders']
            
            user.orders.add(order)

            return redirect('/successful_operation')
    else:
        form = NewOrderUserForm()
    
    return render(request, 'core/input/ordered_form.html', {
        'form': form
    })

def create_order_item(request):
    if request.method == 'POST':
        form = NewOrderItemForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['items']
            order = form.cleaned_data['orders']
            
            order.items.add(item)

            return redirect('/successful_operation')
    else:
        form = NewOrderItemForm()
    
    return render(request, 'core/input/ordered_items_form.html', {
        'form': form
    })

def create_owneditem_user(request):
    if request.method == 'POST':
        form = NewOwnedItemUserForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['items']
            users = form.cleaned_data['users']
            
            users.items.add(item)

            return redirect('/successful_operation')
    else:
        form = NewOwnedItemUserForm()
    
    return render(request, 'core/input/owns_form.html', {
        'form': form
    })

def create_wisheditem_user(request):
    if request.method == 'POST':
        form = NewWishedItemUserForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['items']
            users = form.cleaned_data['users']
            
            users.wished_items.add(item)

            return redirect('/successful_operation')
    else:
        form = NewWishedItemUserForm()
    
    return render(request, 'core/input/wished_user_items_form.html', {
        'form': form
    })

def successful_operation(request):
    return render(request, 'core/input/success.html')

def search_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'core/search/search_items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'core/search/item_detail.html', {
        'item': item,
    })

def search_users(request):
    query = request.GET.get('query', '')
    role_id = request.GET.get('role', 0)
    roles = Role.objects.all()
    users = User.objects.all()
    
    if role_id:
        users = users.filter(role_id=role_id)

    if query:
        users = users.filter(Q(username__icontains=query) | Q(address__icontains=query))

    user_order_counts = [{'user': user, 'order_count': user.orders.count()} for user in users]

    return render(request, 'core/search/search_users.html', {
        'user_order_counts': user_order_counts,
        'query': query,
        'roles': roles,
        'role_id': int(role_id)
    })


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)

    return render(request, 'core/search/user_detail.html', {
        'user': user,
    })