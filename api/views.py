import json
import time
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
import logging

from supabase import create_client, Client
from .models import Classes
from .models import Users
from .models import Books
import bcrypt

logger = logging.getLogger('schooladmin')

# Create your views here.
@ensure_csrf_cookie
def csrf_cookie(request):
    return JsonResponse({'cookie': 'set'})

@csrf_protect
def auth_login(request):
    body_unicode = request.body.decode("utf-8")  # bytes -> string
    body_data = json.loads(body_unicode)         # string -> dict
    email = body_data.get('email')
    password = body_data.get('password')
    user = authenticate(request, username=email, password=password)
    logger.info(user)
    if user:
        logger.info('auth')
        login(request, user)
        return JsonResponse({'auth': 'ok'})

    else:
        logger.info('notauth')

        return HttpResponseForbidden('email o password sbagliati')
    
def auth_logout(request):
    logout(request)
    return JsonResponse({'login': 'ok'})
    
def get_users(request):
    students = []
    teachers = []
    users = Users.objects.all()
    if users:
        for user in users:
            if(user.type == 'insegnante'):
                teachers.append(user.name)
            else:
                students.append(user.name)
        return JsonResponse({'teachers': teachers, 'students': students})
    else:
        return HttpResponseServerError('errore connessione database')

    

def set_users(request):
    body_unicode = request.body.decode("utf-8")  # bytes -> string
    body_data = json.loads(body_unicode)         # string -> dict
    name = body_data.get('name')
    email = body_data.get('email')

    
    password = body_data.get('password')
    hashed_password = bcrypt.hashpw(request.body[2].to_bytes(), bcrypt.gensalt())
    type = body_data.get('type').lower()
    user = Users(name = name, email = email, password = hashed_password.decode('utf-8'), type = type)
    if user:
        user.save()
        return JsonResponse({'classes': 'classes'})
    else: 
        return HttpResponseServerError('errore connessione database') 

def get_classes(request):
    classes = []
    db_classes = Classes.objects.all()
    if db_classes:
        for clas in db_classes:
            classes.append(clas.name)
        
        return JsonResponse({'classes': classes})
    else: 
        return HttpResponseServerError('errore connessione database') 


@csrf_protect
def set_classes(request):
    body_unicode = request.body.decode("utf-8")  # bytes -> string
    body_data = json.loads(body_unicode)         # string -> dict
    name = body_data.get('class')
    teacher = body_data.get('teacher')
    student = body_data.get('student')
    try:
        query_teacher = Users.objects.get(name = teacher)
    except ObjectDoesNotExist:
        query_teacher = ''
        logger.info('teacher not found')
    try:
        query_student = Users.objects.get(name = student)
    except ObjectDoesNotExist:
        query_student = ''
        logger.info('student not found')
    if query_teacher == '':
        clas = Classes(name = name, id_student = query_student.id, id_teacher = 0)
    if query_student == '':
        clas = Classes(name = name, id_student = 0, id_teacher = query_teacher.id)
    clas.save()

    return JsonResponse({'classes': 'ok'})

def new_class(request):
    body_unicode = request.body.decode("utf-8")  # bytes -> string
    body_data = json.loads(body_unicode)         # string -> dict
    name = body_data.get('newClass')
    clas = Classes(name = name, id_student = 0, id_teacher = 0)
    clas.save()
    return JsonResponse({})

def upload(request):
    file_obj = request.FILES.get("file")
    logger.info(file_obj)
    filename = f"{int(time.time())}_{file_obj.name}"

    # Leggi i byte del file
    file_bytes = file_obj.read()
    supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
    # Carica nel bucket Supabase
    result = supabase.storage.from_('books').upload(
            path=filename,
            file=file_bytes,
            file_options={"content-type": file_obj.content_type},
        )
    return JsonResponse({})

def get_books(request):
    books = []
    for book in Books.objects.all():
        books.append(book.title)
    return JsonResponse({'books': books})

def download(request):
    body_unicode = request.body.decode("utf-8")  # bytes -> string
    body_data = json.loads(body_unicode)         # string -> dict
    title = body_data.get('title')
    supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

    result = supabase.storage.from_('books').create_signed_url(
        title,
        60
    )

    
    return JsonResponse({'url': result['signedUrl']})

def delete(request):
    body_unicode = request.body.decode("utf-8")  # bytes -> string
    body_data = json.loads(body_unicode)         # string -> dict
    title = body_data.get('title')
    supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))
    
    result = supabase.storage.from_('books').remove([title])
    return JsonResponse({})