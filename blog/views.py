from django.shortcuts import render
import pymongo

#CONNECTION TO DATABASE
try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["local"]
    mycol = mydb["startup_log"]
    x = mycol.find_one()
    print('Connected !')
    #print(x)

except :
    print('Connection failed !')

def home(request):
    return render(request, 'blog/home.html', {})

def user(request):
    return render(request,'blog/user.html',{})

def dataAnalyst(request):
    return render(request,'blog/dataAnalyst.html',{})

def admin(request):
    return render(request,'blog/admin.html',{})   
    
def executeRequest(request):
    #id_req=request.GET.get("id")
    id_req=request.body
    print('id_req:')
    print(id_req)

    """x=request.body.submit
    if  ==1:
        myquery = ' '
    if id_req ==1:
        myquery = ' '


    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
"""
    return render(request,'blog/admin.html',{})   


    
