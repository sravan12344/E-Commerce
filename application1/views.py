from django.shortcuts import render, redirect
from .models import *
from .form import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# To view all the product in the showproduct.html
# @login_required(login_url="accounts/login/")
def ShowAllProduct(request):
    category = request.GET.get("category")  # Get the clicked category name

    if category is None:
        # Retrieve all products from the Product model in the database
        products = Product.objects.order_by("-price").filter(is_published=True)
    else:
        # Checks category name matches with the clicked category
        products = Product.objects.filter(category__name=category)

    # Count the total number of products in the database
    number_of_products = Product.objects.all().count()

    # Get the page number from the query parameters in the URL
    page_number = request.GET.get("page")

    # Create a Paginator object with 2 products per page
    paginator = Paginator(products, 6)

    # Try to get the requested page, handle exceptions for invalid page numbers
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)  # If the page is not an integer, deliver the first page
    except EmptyPage:
        products = paginator.page(
            paginator.num_pages
        )  # If the page is out of range (e.g., 9999), deliver the last page of results

    categories = Category.objects.all()

    # Prepare a context dictionary with products and the total number of products, categories
    context = {
        "products": products,
        "number_of_products": number_of_products,
        "categories": categories,
    }

    return render(request, "showProduct.html", context)


# To view the single product details in the productdetail.html
# @login_required(login_url="show")
def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)

    context = {"eachProduct": eachProduct}

    return render(request, "productdetail.html", context)


# To add new product from the html template page


@login_required(login_url="show")
def addProduct(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(
            request.POST, request.FILES
        )  # Create a ProductForm instance with the data from the POST request
        # and the files uploaded (request.FILES)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect("show")
    context = {"form": form}

    return render(request, "addProduct.html", context)


# Updating the data
@login_required(login_url="show")
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(
        instance=product
    )  # Create a ProductForm instance and populate it with the data from the retrieved product
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("show")
    context = {"form": form}

    return render(request, "updateProduct.html", context)


# Deleting the Data
@login_required(login_url="show")
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return redirect("show")


# Search Function
@login_required(login_url="show")
def searchBar(request):
    if request.method == "GET":
        query = request.GET.get("query") # Get the value of the "query" parameter from the GET parameters
        products = []
        if query:
                search_filter = (
                    Q(name__icontains=query)
                    | Q(price__icontains=query)
                    | Q(description__icontains=query)
                )
                products = Product.objects.filter(search_filter)
                return render(request, "searchBar.html", {"products": products})# Render the search results in the "searchBar.html" template
    else:
        print("*****Details Not Found******")
        return render(request, "searchBar.html", {})# Render the "searchBar.html" template with an empty context

# views.py
from django.shortcuts import render, redirect
from .models import ck
from django.http import HttpResponse

def cke(request):
    # Assuming you want to retrieve all instances of ck
    geeks_objects = ck.objects.all()

    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        des = request.POST.get('des')

        # Save the form data to the database
        ck.objects.create(name=name, des=des)
        return redirect('ck')  # Redirect to the same page after saving

    return render(request, 'ck.html', {'geeks_objects': geeks_objects})

# views.py
from django.shortcuts import render, redirect
from .models import WishlistItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# @login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

# @login_required
def add_to_wishlist(request, course_name):
    WishlistItem.objects.create(user=request.user, course_name=course_name)
    return JsonResponse({'message': 'Course added to wishlist successfully'})


