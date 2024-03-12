

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from gym.models import Items,ItemDetails
# Create your views here.
@api_view(['GET'])
def getallitems_list(request):
    phone=Items.objects.all() # Get All Items
    phonelist=list(phone.values())
    return JsonResponse({
        'phone':phonelist
    })

def list_item_details(request):
    phone=ItemDetails.objects.select_related('itemsid').all()
    list1=[]
    for item in phone:
        getitems=({
            'id':item.id,
            'name':item.itemsid.name,
            'color':item.color,
            'price':item.price,
            'qty':item.qty,
            'tax':item.tax,
            'total':item.total
        })
        list1.append(getitems)
   
    return JsonResponse({
        'phone':list1
    })


def list_item_detailsbyid(request,id):
    phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
    list1=[]
    for item in phone:
        getitems=({
            'id':item.id,
            'name':item.itemsid.name,
            'color':item.color,
            'price':item.price,
            'qty':item.qty,
            'tax':item.tax,
            'total':item.total
        })
        list1.append(getitems)
   
    return JsonResponse({
        'phone':list1
    })


# Create your views here.
