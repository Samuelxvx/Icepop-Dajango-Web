from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render

all_icepops = [
    {'id': 1, 'title':'Dark Choco', 'price': 299, 'is_premium': True,'promo_end_at': datetime(2023,12,25)},
    {'id': 2, 'title':'Red Wine', 'price': 499, 'is_premium': True,'promo_end_at': datetime(2023,12,25)},
    {'id': 3, 'title':'Blue Choco', 'price': 349, 'is_premium': False,'promo_end_at': datetime(2023,10,15)},
]
# Create your views here.
def icepops(request):
    context = { 'icepops': all_icepops  }
    return render(request,'app_icepops/icepops.html', context)

def icepop(request, icepop_id):
    one_icepop = None
    try:
        one_icepop = [f for f in all_icepops if f ['id'] == icepop_id][0]
    except IndexError:
        print("This item doesn't exit")
    context = { 'icepop': one_icepop }
    return render(request, 'app_icepops/icepop.html', context)