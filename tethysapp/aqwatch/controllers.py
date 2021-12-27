from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from rest_framework.decorators import api_view, authentication_classes


# @login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {
    }

    return render(request, 'aqwatch/Created_emission.html', context)
