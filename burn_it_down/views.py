import datetime
import os
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.expressions import RawSQL
from django.db import connection
import sqlite3

from burn_it_down.models import User
# import burn_it_down.User as User
# Create your views here.


def index(request : HttpRequest) -> HttpResponse:
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.datetime.now().year,
        }
    )


@csrf_exempt
def ping(request):
    url = request.body
    t = os.popen(f"ping {str(url, 'utf-8')}").read()
    return JsonResponse({'body':t})

@csrf_exempt
def sql(request):
    data = request.body
    try:
        q = f"SELECT id, username FROM auth_user WHERE id = '{str(data, 'utf-8')}'"
        print(q)
        x = User.objects.raw(q)
        for i in x:
            print(i)
        return JsonResponse({'body':list(x.query)})
        
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': 'An error occurred'})

    
    