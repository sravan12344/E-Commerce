from django.shortcuts import render

from application1.models import Product
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
def show_products(request):
    products=Product.objects.all()


    context={"products":products}

    return render(request,"showinfo.html",context)

def pdf_report_create(request):
    products=Product.objects.all()
    template_path = 'pdfreport.html'
    context={"products":products}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='pdf_convert/pdf')
    response['Content-Disposition'] = 'attachment; filename="products_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# Create your views here.
