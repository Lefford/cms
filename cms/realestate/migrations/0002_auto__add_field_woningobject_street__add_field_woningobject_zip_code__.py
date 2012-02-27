# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'WoningObject.street'
        db.add_column('realestate_woningobject', 'street', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'WoningObject.zip_code'
        db.add_column('realestate_woningobject', 'zip_code', self.gf('django.db.models.fields.CharField')(default='', max_length=8), keep_default=False)

        # Adding field 'WoningObject.number'
        db.add_column('realestate_woningobject', 'number', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'WoningObject.extension'
        db.add_column('realestate_woningobject', 'extension', self.gf('django.db.models.fields.CharField')(default='', max_length=3), keep_default=False)

        # Adding field 'WoningObject.city'
        db.add_column('realestate_woningobject', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=30), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'WoningObject.street'
        db.delete_column('realestate_woningobject', 'street')

        # Deleting field 'WoningObject.zip_code'
        db.delete_column('realestate_woningobject', 'zip_code')

        # Deleting field 'WoningObject.number'
        db.delete_column('realestate_woningobject', 'number')

        # Deleting field 'WoningObject.extension'
        db.delete_column('realestate_woningobject', 'extension')

        # Deleting field 'WoningObject.city'
        db.delete_column('realestate_woningobject', 'city')


    models = {
        'realestate.woningobject': {
            'Meta': {'object_name': 'WoningObject'},
            'build_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'prijs': ('django.db.models.fields.IntegerField', [], {}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tumbs_pics': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['realestate']
