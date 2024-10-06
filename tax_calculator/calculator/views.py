from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

tax_rate = 0.15

def default():
    return HttpResponse("<h1>This is a site to calculate tax</h1>")

def cal_tax(request, amount):
    try:
        amount=float(amount)
        total_price=amount+(amount*tax_rate)
        return HttpResponse(f"<h1>the total with tax: {total_price:.2f}</h1>")
    except ValueError:
        return HttpResponse("<h1>invalide amount . please enter a number</h1>")
    
def tax_rate(request):
    return HttpResponse(f"<h1>the current tax rate is : {tax_rate*100}%</h1>")
