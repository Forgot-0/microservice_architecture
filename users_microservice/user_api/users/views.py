from djoser.views import UserViewSet
from django.shortcuts import render


def activation(request, uid, token):
    context = {
        'uid': uid,
        'token': token,
    }
    return render(request, 'activation_email.html', context=context)



