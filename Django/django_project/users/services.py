from typing import Dict
from .models import User
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist


class UserService:
    def create_user(self, user_info: Dict) -> Dict:
        try:
            hash_password = make_password(user_info['password'])
            user = User.objects.create(
                user_id=user_info['uuid'],
                email=user_info['email'],
                password=hash_password,
            )
            return user
        except IntegrityError:
            raise ValueError("Email já cadastrado!")
        
    def get_user_by_id(self, id: str) -> User:
        try:
            user = User.objects.get(user_id=id)
            return user
        except ObjectDoesNotExist:
            raise ValueError('Nenhum usuário encontrado!')
