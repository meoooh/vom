# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'vom_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.VomUser'])),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(default=u'\ubbf8\ubd84\ub958', max_length=254)),
        ))
        db.send_create_signal(u'vom', ['Question'])

        # Adding model 'CategoryOfQuestion'
        db.create_table(u'vom_categoryofquestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.VomUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'vom', ['CategoryOfQuestion'])

        # Adding model 'Constellation'
        db.create_table(u'vom_constellation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('eng', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('image', self.gf('django.db.models.fields.TextField')()),
            ('dot', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'vom', ['Constellation'])

        # Adding model 'Answer'
        db.create_table(u'vom_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('writer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.VomUser'])),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.Question'])),
            ('star', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.Constellation'])),
        ))
        db.send_create_signal(u'vom', ['Answer'])

        # Adding model 'Status'
        db.create_table(u'vom_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vom.VomUser'], unique=True)),
            ('star', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.Constellation'])),
            ('count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'vom', ['Status'])

        # Adding model 'Item'
        db.create_table(u'vom_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.VomUser'])),
            ('stuff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.Constellation'])),
        ))
        db.send_create_signal(u'vom', ['Item'])

        # Adding model 'VomUser'
        db.create_table(u'vom_vomuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('sex', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('dateOfRecevingLastQuestion', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('questionOfToday', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vom.Question'], null=True, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'vom', ['VomUser'])

        # Adding M2M table for field groups on 'VomUser'
        m2m_table_name = db.shorten_name(u'vom_vomuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vomuser', models.ForeignKey(orm[u'vom.vomuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vomuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'VomUser'
        m2m_table_name = db.shorten_name(u'vom_vomuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vomuser', models.ForeignKey(orm[u'vom.vomuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vomuser_id', 'permission_id'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'vom_question')

        # Deleting model 'CategoryOfQuestion'
        db.delete_table(u'vom_categoryofquestion')

        # Deleting model 'Constellation'
        db.delete_table(u'vom_constellation')

        # Deleting model 'Answer'
        db.delete_table(u'vom_answer')

        # Deleting model 'Status'
        db.delete_table(u'vom_status')

        # Deleting model 'Item'
        db.delete_table(u'vom_item')

        # Deleting model 'VomUser'
        db.delete_table(u'vom_vomuser')

        # Removing M2M table for field groups on 'VomUser'
        db.delete_table(db.shorten_name(u'vom_vomuser_groups'))

        # Removing M2M table for field user_permissions on 'VomUser'
        db.delete_table(db.shorten_name(u'vom_vomuser_user_permissions'))


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
            'stuff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vom.Constellation']"}),
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