import json
import bcrypt
import jwt

from django.views    import View
from django.http     import JsonResponse

from .models         import User

from naweki.settings import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body) 

        try :
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message" : "EXISTS_EMAIL"}, status = 400) 

            hashed_password = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt())

            User.objects.create( 
                name         = data['name'],
                email        = data['email'],
                password     = hashed_password.decode('utf-8'),
                phone_number = data['phone_number'],
            )
            return JsonResponse({"message" : "SIGN_UP SUCCESS"} , status = 200)

        except KeyError:
          return JsonResponse({"message" : "INVALID_KEYS"} , status = 400) 

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
     
        try:
            if User.objects.filter(email = data['email']).exists() :
                user = User.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) :
                    token = jwt.encode({'id' : user.id} , SECRET_KEY , algorithm = ALGORITHM).decode('utf-8')
                    return JsonResponse({"Authorization" : token , "message" : "LOGIN_SUCCESS"} , status = 200 )             
                return JsonResponse({"message" : "WORNG_PASSWORD" } , status = 401) 

            return JsonResponse({"message" : "WORNG_EMAIL"} , status = 401)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"} , status = 400) 
