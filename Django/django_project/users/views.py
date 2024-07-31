import uuid
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .services import UserService

# Create your views here.


from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    return render(request, 'users/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(View):
    def post(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        user_info = {
            'email': body.get('email'),
            'password': body.get('password'),
            'nickname': body.get('nickname'),
            'uuid': str(uuid.uuid4())
        }
    
        user_service = UserService()
        
        try:
            user_service.create_user(user_info)
            return JsonResponse({'message': 'User created successfully', 'user_id': user_info['uuid']}, status=201)
        except ValueError as e:
            return render(request, 'error.html', {'error_message': str(e)}, status=400)
       
class GetUserView(View):
    def get(self, request):
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
        except json.JSONDecodeError:
            return render(request, 'error.html', {'error_message': 'Invalid JSON'}, status=400)
        
        user_service = UserService()
        
        try:
            user = user_service.get_user_by_id(body.get('user_id'))
            return render(request, 'users/view_get_user_by_id.html', {'user_by_id': user.email}, status=200)
        except Exception as e:
            return render(request, 'error.html', {'error_message': str(e)}, status=400)
        