from django.shortcuts import render,redirect
from .forms import FunctionReview,FunctionOrder
from .models import Reviews,Order

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def review(request):
    context={}
    form = FunctionReview()
    view=Reviews.objects.all()
    if request.method == 'POST':
        form = FunctionReview(request.POST)
        if form.is_valid():
            Reviews.objects.create(**form.cleaned_data)
            view=Reviews.objects.all()
            form = FunctionReview()
    context['form']=form
    context['view']=view
    return render(request, 'review.html',context)

def order(request):
    form=FunctionOrder()
    if request.method=='POST':
        form=FunctionOrder(request.POST)
        if form.is_valid():
            Order.objects.create(**form.cleaned_data)
            return redirect('success-func')
    context={'form':form}
    return  render(request, 'order.html',context)

def success(request):
    return render(request,'success.html')
