import jwt
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth.models import User

class JWTAuth:
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None
        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return User.objects.get(id=decoded['user_id'])
        except jwt.ExpiredSignatureError:
            raise Exception("Token expirado")
        except jwt.InvalidTokenError:
            raise Exception("Token inválido")

def generar_token(user):
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'user_id': user.id,
        'exp': expiration
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

