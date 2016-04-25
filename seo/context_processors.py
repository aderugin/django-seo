# -*- coding: utf-8 -*-
from .models import Metatags

def metatags(request):
    return {'metatags': Metatags.get_metatags(request.path)}
