#coding:utf8
from collections import OrderedDict
import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from players.models import Player


class RankingView(View):
    def get(self, request, *args, **kwargs):
        ranking = Player.objects.ranking(0, 20)
        return render(request, 'ranking.html', {'ranking': ranking})
