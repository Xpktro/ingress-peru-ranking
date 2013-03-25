#coding:utf8
from ordereddict import OrderedDict
import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from players.models import Player


class PlayerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(PlayerView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        nick = request.POST.get('nickname')
        faction = request.POST.get('faction')
        level = request.POST.get('level')
        ap = request.POST.get('ap')
        email = request.POST.get('email')

        if not nick and faction and level and ap and email:
            return HttpResponseBadRequest(
                content=json.dumps({'error': 'Bad request. '
                                             'Must include all the necessary '
                                             'fields.'}),
                content_type='application/json'
            )

        try:
            player = Player.objects.get(email=email)
        except Player.DoesNotExist:
            player = Player()

        player.nickname = nick
        if faction == u'RESISTANCE':
            player.faction = player.FACTION_CHOICES.RESISTANCE
        else:
            player.faction = Player.FACTION_CHOICES.ENLIGHTENED

        player.ap = int(ap)
        player.email = email

        player.save()

        response = OrderedDict()
        response['status'] = 'success'
        response['position'] = player.position()

        return HttpResponse(
            content=json.dumps(response),
            content_type='application/json'
        )
