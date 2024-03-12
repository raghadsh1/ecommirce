from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from gyms.models import Items,ItemDetails,Cart
from gym.forms  import CreateUserForm,LoginUserForm
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

#Create your views here.
def showgym(request):
        template=loader.get_template('showgym.html')
        phone=ItemDetails.objects.select_related('itemsid')
        print(phone.query)
        return HttpResponse(template.render({'phone':phone}))




def showdetails(request , id):
 template=loader.get_template('showdetails.html')
 phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
 print(phone.query)
 context={
      'phone':phone
 }
 
 return HttpResponse(template.render(context))

@login_required(login_url='/auth_login/')
def showcheck(request):
       template=loader.get_template('showcheck.html')
       current_user = request.user.id
       cart=Cart.objects.all().filter(Id_user=current_user).first()
       product=Items.objects.get(id=cart.Id_product)
       context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
       return HttpResponse(template.render(context=context)) 

def addtocart(requset,id):
     currentuser=requset.user
     discount=2
     state=False
     phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
     count=0
    
     for item in phone:
           net=item.total-discount
        
     cart = Cart(
      Id_product=item.id,
      Id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      net=net,
      status=state
)
     

     currentuser=requset.user.id
     count=Cart.objects.filter(Id_user=currentuser).count()
     print(count)
     cart.save()
     requset.session['countcart']=count
     return redirect("/showgym")

     