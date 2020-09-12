from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense,Token,User,Income
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_expense(request):
    #TODO user set datetime .
    print ('khoda',request.POST)
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user,text=request.POST['text'],amount=request.POST['amount'],date=datetime.now())
    
    return JsonResponse({
        'status':'ok'
    },encoder=json.JSONEncoder)
@csrf_exempt
def submit_income(request):
    this_token=request.POST['token']
    if request.POST['date']== '':
        now=datetime.now()
    this_user=User.objects.filter(token__token=this_token).get()
    Income.objects.create(user=this_user,text=request.POST['text'],amount=request.POST['amount'],date=now)
    return JsonResponse({
        'status':'ok'
    },encoder=json.JSONEncoder)

    
