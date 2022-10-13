from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LsOLkDXCg9kKjFnklvBBkv88bLq9V5hd4Fmor89c8UNp8cGzwyeEHgWya4KOLS8Qqn98i1xJZg4HsMpP9uCJFnB00Gxdsudyh',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)