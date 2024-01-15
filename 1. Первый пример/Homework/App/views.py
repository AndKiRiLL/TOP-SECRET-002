from django.shortcuts import render
from .models import Company, Product
from .forms import FormCreate, FormEdit
from django.http import HttpResponseRedirect, HttpResponseNotFound

# получение данных из бд
def index(request):
    products = Product.objects.all()
    return render(request, "app/index.html", {"products": products})

# добавление данных из бд
def create(request):
    create_companies() # добавляем начальные данные для компаний

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/")
    # передаём данные в шаблон
    companies = Company.objects.all()
    form_add = FormCreate()
    return render(request, "app/create.html", {"companies": companies, "form_add": form_add})

# зменение данных бд
def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.company_id = request.POST.get("company")
            product.save()
            return HttpResponseRedirect("/")
        else:
            companies = Company.objects.all()
            form_edit = FormEdit(instance=product)
            return render(request, "app/edit.html", {"product": product, "companies": companies, "form_edit": form_edit})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

# удаление данных из бд
def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

# добавление начальных данных в таблицу компаний
def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name = "Apple")
        Company.objects.create(name = "Asus")
        Company.objects.create(name = "MSI")

