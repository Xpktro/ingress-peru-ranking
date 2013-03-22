# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Player', fields ['email']
        db.create_unique(u'players_player', ['email'])

        # Adding unique constraint on 'Player', fields ['nickname']
        db.create_unique(u'players_player', ['nickname'])


    def backwards(self, orm):
        # Removing unique constraint on 'Player', fields ['nickname']
        db.delete_unique(u'players_player', ['nickname'])

        # Removing unique constraint on 'Player', fields ['email']
        db.delete_unique(u'players_player', ['email'])


    models = {
        u'players.player': {
            'Meta': {'object_name': 'Player'},
            'ap': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'nickname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['players']