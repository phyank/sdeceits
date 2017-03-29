from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserAndPass

# Create your views here.

USER_KEYWORD="user"
PASS_KEYWORD="pass"

def home(request):
	if request.method == "POST" :
		try:
			uname = request.POST[USER_KEYWORD]
			upass = request.POST[PASS_KEYWORD]
			newRecord=UserAndPass(user_name=uname, user_pass=upass)
			newRecord.save()
			return HttpResponseRedirect("/")
		except:
			return HttpResponseRedirect("/")
	else:
		return render(request,"index.html")


def errorHandler(request):
	return HttpResponseRedirect("/")
