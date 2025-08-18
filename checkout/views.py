from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RxZrIJDNpQfwITIBNzdHHtSpMiKd1j704EBaWx8dTlLQLY9DfaVWUJYLEZFegHT1s5ovLo7wcUXAv0TlrjDmIZL00Ekdcxt6M',
        'client_secret': 'test_client_secret',  # Replace with actual client secret from Stripe
    }

    return render(request, template, context)