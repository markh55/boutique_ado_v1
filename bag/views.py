from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ View to renders the shopping bag contents """

    return render(request, 'bag/bag.html')