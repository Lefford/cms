# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WoningObject'
        db.create_table('realestate_woningobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prijs', self.gf('django.db.models.fields.IntegerField')()),
            ('build_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rooms', self.gf('django.db.models.fields.IntegerField')()),
            ('tumbs_pics', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('realestate', ['WoningObject'])


    def backwards(self, orm):
        
        # Deleting model 'WoningObject'
        db.delete_table('realestate_woningobject')


    models = {
        'realestate.woningobject': {
            'Meta': {'object_name': 'WoningObject'},
            'build_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prijs': ('django.db.models.fields.IntegerField', [], {}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tumbs_pics': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['realestate']
