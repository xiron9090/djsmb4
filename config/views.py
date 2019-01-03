from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home(request):
	ctx = {}
	return render(request, "login/login.html", ctx)

#@login_required
def admin_view(request):
	title = "Admin page"
	ctx = {"title": title}
	return render(request,'admin/admin.html', ctx)

#Logout
#@login_required
def logout_view(request):
	username = password = ''
	logout(request)
	return HttpResponseRedirect('/login/')
