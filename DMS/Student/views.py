

from django.shortcuts import redirect, render
from django.contrib import messages 



# Create your views here.

from .models import *
def aa(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
      
        try:
            user=Account.acc.get(email=email,password=password)
           
            if user is not None:
                request.session['email']=user.email
                
                roleName=user.roleName
                contest={'email':request.session['email']}
              
                if roleName=='Dean':
                            return render(request,'Dean.html',contest)
                elif roleName=='Vice':
                            return render(request,'Vice.html',contest)
                elif roleName=='Admin':
                            return render(request,'index.html',contest)
            else:
                messages.info(request,'Invalid UserName or Password')
                return redirect('aa')

        except Exception as identifier:
            return redirect('aa')
        
 
      
            
        else:

         messages.info(request,('Incorrect Username or Password'))
         return redirect('aa')
    else:
        return render(request,'login.html')

def add_item(request):
   
    if request.method=='POST':
        email=request.POST['email']
        roleName=request.POST['roleName']
        password=request.POST['password']
        password1=request.POST['password1']
        if Account.objects.filter(email=email).exists():
           messages.info(request,"USER Account Aready Exist")
        else: 
         if password==password1:
                Account.objects.create(email=email,password=password,roleName=roleName).save()
                messages.info(request,"USER IS INSERTED")
         else:
            messages.info(request,"Password does not Match")
    else: 
        pass
  
    return render(request,'index.html')

# def delete_item(request,myid):
   
#     b=item.userId
#     item1=Account.objects.get(userId=b)
#     item2=Role.objects.get(userId=b)
#     item.delete()
#     item1.delete()
#     item2.delete()
#     messages.info(request,"USER DELETE SUCCESSFULLY")
#     return redirect('add_item')
# def edit_item(request,myid):
#     sel_item=Account.objects.get(id=myid)
#     item_list=Account.objects.all()
#     context={
#         'sel_item': sel_item,
#         'item_list':item_list
#     }
#     return render(request,'index.html',context)
# def update_item(request,myid):
#     item=user.objects.get(id=myid)
#     item.username=request.POST['username']
#     item.password=request.POST['password']
    
#     item.save()
#     messages.info(request,"USER IS UPDATED")
#     return redirect('add_item')


def Vice(request):
    return render(request,'Vice.html')
def Dean(request):
    return render(request,'Dean.html')
def logout(request):
    return render(request,'login.html')


def profile(request,email):
    sel_item=Account.objects.get(email=email)
    context={
        'sel_item': sel_item
        
            }

    return render(request,'profile.html',context)