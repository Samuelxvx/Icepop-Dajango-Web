from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Icepop

# Create your views here.
def icepops(request):
    all_icepops = Icepop.objects.order_by('-is_premium')
    context = { 'icepops': all_icepops  }
    return render(request,'app_icepops/icepops.html', context)

def icepop(request, icepop_id):
    one_icepop = None
    try:
           one_icepop = Icepop.objects.get(id=icepop_id)
    except:
        print('ERROR')
    context = { 'icepop': one_icepop }
    return render(request, 'app_icepops/icepop.html', context)