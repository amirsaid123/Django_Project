import json

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.forms import CarForm
from apps.models import Job, Product, Plan, OnlyProduct, Images


def say_hello(request):
    name = request.GET.get('name')
    return render(request, 'lesson_1/hello.html', {'name': name})

def show_products(request, id):
    with open('datas/products.json', 'r') as f:
        products = json.load(f)

    for product in products.get("products", []):
        if product.get("id") == id:
            return JsonResponse(product)

    return None

def show_username(request, username):
    return render(request, 'lesson_1/username.html', {'username': username})

def show_seach(request):
    name = request.GET.get('search')
    with open('datas/products.json', 'r') as f:
        products = json.load(f)

    for product in products.get("products", []):
        if name.lower() in product.get("title").lower():
            return JsonResponse(product)

def show_prices(request):
    min_price = float(request.GET.get('min_price'))
    max_price = float(request.GET.get('max_price'))
    with open('datas/products.json', 'r') as f:
        products = json.load(f)

    for product in products.get("products", []):
        if product.get("price") > min_price and product.get("price") > max_price:
            return JsonResponse(product)

    return None

def show_books(request, id):
    name = request.GET.get('author')
    with open('datas/books.json', 'r') as f:
        products = json.load(f)

    for product in products.get("books", []):
        if product.get("id") == id and name.lower() in product.get("author").lower():
            return JsonResponse(product)

    return None

def hello_django(request):
    return render(request, 'lesson_1/django.html')

def django_info(request):
    context = {
        'text': '''
            <h2>Django: The Web Framework for Perfectionists with Deadlines</h2>
            <p>Django is a high-level Python web framework that allows you to quickly create robust and scalable web applications. It emphasizes the "don't repeat yourself" (DRY) principle, helping developers write clean and maintainable code.</p>
            <p>Django was designed to make common web development tasks easier, such as user authentication, database management, routing, and more. It comes with built-in admin interfaces, support for multiple databases, and extensive libraries and tools to facilitate rapid development.</p>
            <p>One of Django's strongest features is its modularity, which allows you to use various components, such as templates, views, and models, to structure your application effectively.</p>
            <h3>Some notable features of Django include:</h3>
            <ul>
                <li><strong>Fast Development:</strong> Django's simple yet powerful components allow developers to create applications quickly.</li>
                <li><strong>Security:</strong> Django includes protection against various security threats, including SQL injection, cross-site scripting, and cross-site request forgery.</li>
                <li><strong>Scalability:</strong> Django is built to scale and is used by large applications and websites.</li>
                <li><strong>Community:</strong> With an active community, Django ensures constant improvements and a wealth of resources for developers.</li>
            </ul>
        '''
    }
    return render(request, 'lesson_1/django_info.html', context)

def product_list(request):
    products = [
        {
            "id": 1,
            "name": "Appple",
            "description": "Juicy red apple",
            "price": 19.99,
        },
        {
            "id": 2,
            "name": "Banana",
            "description": "Yellow Banana",
            "price": 29.99,
        },
        {
            "id": 3,
            "name": "Chicken Meat",
            "description": "Nutritious chicken meat",
            "price": 39.99,
        },
        {
            "id": 4,
            "name": "Coco Cola",
            "description": "The first cola ever produced",
            "price": 49.99,
        },
    ]
    context = {'products': products}
    return render(request, 'lesson_1/products_list.html', context)

def show_category(request, category):
    with open('datas/products.json', 'r') as f:
        products = json.load(f)

    filtered_products = []

    for product in products.get("products", []):
        if 'category' in product and category.lower() in product.get("category", "").lower():
            filtered_products.append(product)

    return render(request, 'lesson_1/show_category.html', {'products': filtered_products, 'name': category})

def users(request):
    users = User.objects.all()
    return render(request, 'lesson_2/users_list.html', {'users': users})

def send_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'lesson_2/jobs.html', {'jobs': jobs})

def send_products(request):
    products = Product.objects.all()
    return render(request, 'lesson_2/products.html', {'products': products})

def show_plans(request):
    plans = Plan.objects.all()
    return render(request, 'lesson_2/plans.html', {'plans': plans})

def send_products_list(request):
    products = Product.objects.all()
    return render(request, 'lesson_2/products_list.html', {'products': products})


def home(request):
    return render(request, 'lesson_3/home.html')

def home_page(request):
    return render(request, 'lesson_3/home-page.html')

def only_products(request):
    products = OnlyProduct.objects.all()
    return render(request, 'lesson_3/only_products_images.html', {'products': products})


def to_product(request, pk):
    product = OnlyProduct.objects.get(pk=pk)
    images = product.images.all()
    return render(request, 'lesson_3/one_product.html', {'product': product, 'images': images})




class CarFormView(FormView):
    template_name = 'lesson_8/car.html'
    form_class = CarForm
    success_url = reverse_lazy('car')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for message in form.errors.values():
            messages.error(self.request, message)
        return super().form_invalid(form)