from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Douala'
    dest1.price = '700'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The City never sleeps'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Yaounde'
    dest2.price = '600'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'The Capital of country Cameroon'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Buea'
    dest3.price = '400'
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'The smallest region in Cameroon'
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests' : dests})