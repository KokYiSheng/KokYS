from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Dashboard view
def product_dashboard(request):
    products = Product.objects.all()
    return render(request, 'products/dashboard.html', {'products': products})

# Dashboard view with search functionality
def product_dashboard(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'products/dashboard.html', {'products': products, 'query': query})

# Create product view
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_dashboard')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

# Update product view
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

# Delete product view
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_dashboard')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

# Customer home page with search functionality
def home_view(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        products = Product.objects.filter(name__icontains=query)  # Filter products by name
    else:
        products = Product.objects.all()  # Show all products if no query
    return render(request, 'customer/homePage.html', {'products': products, 'query': query})

# Customer view to display all products
def customer_view(request):
    products = Product.objects.filter(availability=True)  # Show only available products
    return render(request, 'customer/customer.html', {'products': products})

# Customer product detail view 
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'customer/product_detail.html', {'product': product})

# Category view to display products by category
def category_view(request, category):
    products = Product.objects.filter(category=category, availability=True)
    return render(request, 'customer/category.html', {'products': products, 'category': category})


