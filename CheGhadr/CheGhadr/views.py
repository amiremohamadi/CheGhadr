from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from CheGhadr.forms import ProductForm
from ScrapProduct import product
from Calculate.calculate import calculate

class HomeView(FormView):
    form_class = ProductForm
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ProductView(TemplateView):
    template_name = 'error.html'
    def post(self, request):
        address = request.POST.get('address')
        wage = request.POST.get('wage')
        _product = product.info(address)
        # how many days/housr you must work!
        how_many = calculate(int(wage), int(_product['price']))

        return render(request, 'product.html', 
        {'img': _product['img'], 'title': _product['name'], 
        'price': _product['price'],
        'wage': wage, 'day': round(how_many['day'], 2), 
        'hour': round(how_many['hour'], 2)})