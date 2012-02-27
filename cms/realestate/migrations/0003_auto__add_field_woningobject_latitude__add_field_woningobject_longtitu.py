# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'WoningObject.latitude'
        db.add_column('realestate_woningobject', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'WoningObject.longtitude'
        db.add_column('realestate_woningobject', 'longtitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Changing field 'WoningObject.city'
        db.alter_column('realestate_woningobject', 'city', self.gf('django.db.models.fields.CharField')(max_length=31))

        # Changing field 'WoningObject.number'
        db.alter_column('realestate_woningobject', 'number', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'WoningObject.zip_code'
        db.alter_column('realestate_woningobject', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=6))


    def backwards(self, orm):
        
        # Deleting field 'WoningObject.latitude'
        db.delete_column('realestate_woningobject', 'latitude')

        # Deleting field 'WoningObject.longtitude'
        db.delete_column('realestate_woningobject', 'longtitude')

        # Changing field 'WoningObject.city'
        db.alter_column('realestate_woningobject', 'city', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'WoningObject.number'
        db.alter_column('realestate_woningobject', 'number', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'WoningObject.zip_code'
        db.alter_column('realestate_woningobject', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=8))


    models = {
        'realestate.woningobject': {
            'Meta': {'object_name': 'WoningObject'},
            'build_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'prijs': ('django.db.models.fields.IntegerField', [], {}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tumbs_pics': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        }
    }

    complete_apps = ['realestate']
