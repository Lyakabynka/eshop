from django import forms
from .models import User, Category, DeliveryData, Discount, Item, Order, Item, Role
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'info'
            })
        }

class NewRoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'info'
            })
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 
                  'email', 
                  'first_name',
                  'last_name',
                  'address',
                  'phone',
                  'role',
                  'password1', 
                  'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your last name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your phone',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    
class NewItemForm(forms.ModelForm):

    discount_choice = forms.ModelChoiceField(
        queryset=Discount.objects.all(),  # Provide a queryset of existing discounts
        required=False,  # Make it optional
        widget=forms.Select(attrs={'class': 'info'}),
    )
    
    class Meta:
        model = Item
        fields = ('status',
                    'category', 
                    'type',
                    'title',
                    'description',
                    'quantity',
                    'price',
                    'owner')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'info'
            }),
            'description': forms.Textarea(attrs={
                'class': 'info'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'info'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'info'
            }),
        }

class NewDiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('item',
                    'percentage',
                    'user')

        widgets = {
            'percentage': forms.NumberInput(attrs={
                'class': 'info'
            }),
        }

        
class NewOrderForm(forms.ModelForm):

    delivery_data_choice = forms.ModelChoiceField(
        queryset=DeliveryData.objects.all(),  # Provide a queryset of existing discounts
        required=False,  # Make it optional
        widget=forms.Select(attrs={'class': 'info'}),
    )
    class Meta:
        model = Order
        fields = ('price',
                    'type',
                    'ordered_by',)

        widgets = {
            'price': forms.NumberInput(attrs={
                'class': 'info'
            }),
        }

class NewDeliveryDataForm(forms.ModelForm):
    class Meta:
        model = DeliveryData
        fields = ('address',
                    'type',
                    'order',
                    'user',)

        widgets = {
            'price': forms.NumberInput(attrs={
                'class': 'info'
            }),
        }

class NewUserItemForm(forms.Form):
    users = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'info'}),
    )
    items = forms.ModelChoiceField(
        queryset=Item.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'info'}),
    )