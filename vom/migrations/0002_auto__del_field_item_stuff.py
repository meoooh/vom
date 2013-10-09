# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Item.stuff'
        db.delete_column(u'vom_item', 'stuff_id')


    def backwards(self, orm):
        # Adding field 'Item.stuff'
        db.add_column(u'vom_item', 'stuff',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['vom.Constellation']),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'vom.answer': {
            'Meta': {'object_name': 'Answer'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.Question']"}),
            'star': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.Constellation']"}),
            'writer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.VomUser']"})
        },
        u'vom.categoryofquestion': {
            'Meta': {'object_name': 'CategoryOfQuestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'writer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.VomUser']"})
        },
        u'vom.constellation': {
            'Meta': {'object_name': 'Constellation'},
            'dot': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'eng': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'vom.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.VomUser']"})
        },
        u'vom.question': {
            'Meta': {'object_name': 'Question'},
            'category': ('django.db.models.fields.CharField', [], {'default': "u'\\ubbf8\\ubd84\\ub958'", 'max_length': '254'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'writer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.VomUser']"})
        },
        u'vom.status': {
            'Meta': {'object_name': 'Status'},
            'count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'star': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.Constellation']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['vom.VomUser']", 'unique': 'True'})
        },
        u'vom.vomuser': {
            'Meta': {'object_name': 'VomUser'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'dateOfRecevingLastQuestion': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'questionOfToday': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.Question']", 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.SmallIntegerField', [], {}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['vom']