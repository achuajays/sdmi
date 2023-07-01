from django.shortcuts import render , redirect , get_object_or_404
from .models import  notifc , log , et , logteam   , reffun   , food  , waste  , es  
from .forms import logf , logteamf ,  alertf  , foodf , wastef 
from django.conf import settings
import requests

from django.core.mail import send_mail

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def alert(request):
    form = notifc.objects.all()
    return render (request , 'app/alert.html' , {'form':form})



def logr(request):
    
    if (request.method == 'POST'):
        form = logf(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            p = form.cleaned_data['password']
            ph = form.cleaned_data['ph_no']
            em = form.cleaned_data['email']
            loc = form.cleaned_data['location']
            request.session['loc'] = loc
            reg=log(name = n , password = p , ph_no = ph , email = em , location = loc)
            reg.save()
            form= logf()
            return redirect(index)
    else:
        form = logf()

      

    return render (request , 'app/reg.html' ,{'form':form})


def update(request , id):
    form = get_object_or_404(notifc  , id= id)
    return render (request , 'app/alertdetails.html' , {'form' : form})



def em(request):
    if(request.method == "POST"):
        l = request.session['loc']
        reg = et(loc = l)
        reg.save()
        return redirect(index)
    return render (request , 'app/em.html',{})


def team(request):
    form  =   et.objects.all()
    return render (request , 'app/team.html' ,{'form':form})





def logteamr(request):
    
    if (request.method == 'POST'):
        form = logteamf(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            p = form.cleaned_data['password']
            ph = form.cleaned_data['ph_no']
            em = form.cleaned_data['email']
            loc = form.cleaned_data['location']
            request.session['locteam'] = loc
            reg=logteam(name = n , password = p , ph_no = ph , email = em , location = loc)
            reg.save()
            form= logteamf()
            return redirect(team)
    else:
        form = logteamf()
            

    return render (request , 'app/teaml.html' ,{'form':form})



def alertr(request):
    
    form = alertf()
    if (request.method == 'POST'):
        form = alertf(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['title']
            p = form.cleaned_data['loc']
            ph = form.cleaned_data['ph']
            em = form.cleaned_data['dis']

            
            message = f"{em} you can contact as {ph}"
            reg=notifc(title = n , loc = p , ph = ph , dis = em)
            list = log.objects.all()
            for i in list:
                if(p == i.location ):
                    send_mail(n, em, settings.EMAIL_HOST_USER, [i.email], fail_silently=False)
            reg.save()
            form= alertf()
            
    else:
        form = alertf()
    

    return render (request , 'app/alertr.html',{'form':form})


def reffunn(request):
    form = reffun.objects.all()

    return render (request , 'app/refundform.html' ,{'form':form})





def updatereffun(request , id):
    form = get_object_or_404(reffun  , id= id)
    return render (request , 'app/refundformup.html' , {'form' : form})



def foodr(request):
    
    if (request.method == 'POST'):
        form = foodf(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            p = form.cleaned_data['loc']
            ph = form.cleaned_data['p']

            reg=food(name = n ,loc = p ,  p = ph )
            reg.save()
            form= foodf()
            
    else:
        form = foodf()
            

    return render  (request , 'app/foodr.html' ,{'form':form})




def foodu(request):
    form   = food.objects.all()
    return render (request , 'app/foodu.html',{'form':form})





import requests
from django.shortcuts import render

def news_catcher(request):
    url = "https://api.newscatcherapi.com/v2/top-headlines"
    querystring = {"country":"us"}
    headers = {
        "x-api-key": "dS5RwgkfPpXtKOZcU9VX2D_ZLbuCpsXCmu0_WUJk93g"
    }
    response = requests.get(url, headers=headers, params=querystring)
    articles = response.json()["articles"]
    return render(request, "news_catcher.html", {"articles": articles})


def wastee(request):
    if (request.method == 'POST'):
        form = wastef(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            p = form.cleaned_data['loc']
            ph = form.cleaned_data['ton']

            reg=waste(name = n ,loc = p ,  ton = ph )
            reg.save()
            form= wastef()
            
    else:
        form = wastef()
            



    return render(request ,'app/waist.html' ,{'form':form})


def wasteview(request):
    form = waste.objects.all()
    return   render (request , 'app/updatewaste.html' , {'form':form}) 





def index(request):
    return render (request , 'app/index.html' , {})





# importing api
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def indexx(request):
	
	newsapi = NewsApiClient(api_key ='2032a48f4efe4423b261c59442a02a31')
	top = newsapi.get_top_headlines(sources ='techcrunch')

	l = top['articles']
	desc =[]
	news =[]
	img =[]

	for i in range(len(l)):
		f = l[i]
		news.append(f['title'])
		desc.append(f['description'])
		img.append(f['urlToImage'])
	mylist = zip(news, desc, img)

	return render(request, 'app/indexx.html', context ={"mylist":mylist})


def esr(request):
    form = es.objects.all()
    return render (request , 'app/es.html' ,{'form':form})
