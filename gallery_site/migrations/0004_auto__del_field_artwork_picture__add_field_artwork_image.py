# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Artwork.picture'
        db.delete_column(u'gallery_site_artwork', 'picture')

        # Adding field 'Artwork.image'
        db.add_column(u'gallery_site_artwork', 'image',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Artwork.picture'
        db.add_column(u'gallery_site_artwork', 'picture',
                      self.gf('django.db.models.fields.files.FileField')(default='image', max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'Artwork.image'
        db.delete_column(u'gallery_site_artwork', 'image')


    models = {
        u'gallery_site.artist': {
            'Meta': {'object_name': 'Artist'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profile_pic': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'gallery_site.artwork': {
            'Meta': {'object_name': 'Artwork'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery_site.Artist']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'gallery_site.benoitimage': {
            'Meta': {'object_name': 'BenoitImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'gallery_site.maincontent': {
            'Meta': {'object_name': 'MainContent'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gallery_site']