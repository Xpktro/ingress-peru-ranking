# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'players_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('ap', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'players', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'players_player')


    models = {
        u'players.player': {
            'Meta': {'object_name': 'Player'},
            'ap': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['players']