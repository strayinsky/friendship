# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Profile.sex'
        db.delete_column(u'friends_profile', 'sex')

        # Deleting field 'Profile.date'
        db.delete_column(u'friends_profile', 'date')

        # Deleting field 'Profile.education'
        db.delete_column(u'friends_profile', 'education')

        # Deleting field 'Profile.age'
        db.delete_column(u'friends_profile', 'age')

        # Deleting field 'Profile.personality'
        db.delete_column(u'friends_profile', 'personality')

        # Deleting field 'Profile.blurb'
        db.delete_column(u'friends_profile', 'blurb')

        # Deleting field 'Profile.rstatus'
        db.delete_column(u'friends_profile', 'rstatus')


    def backwards(self, orm):
        # Adding field 'Profile.sex'
        db.add_column(u'friends_profile', 'sex',
                      self.gf('django.db.models.fields.CharField')(default='foo', max_length=1),
                      keep_default=False)

        # Adding field 'Profile.date'
        db.add_column(u'friends_profile', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default='foo'),
                      keep_default=False)

        # Adding field 'Profile.education'
        db.add_column(u'friends_profile', 'education',
                      self.gf('django.db.models.fields.CharField')(default='bar', max_length=1),
                      keep_default=False)

        # Adding field 'Profile.age'
        db.add_column(u'friends_profile', 'age',
                      self.gf('django.db.models.fields.IntegerField')(default='noodles', max_length=2),
                      keep_default=False)

        # Adding field 'Profile.personality'
        db.add_column(u'friends_profile', 'personality',
                      self.gf('django.db.models.fields.CharField')(default='noodles', max_length=1),
                      keep_default=False)

        # Adding field 'Profile.blurb'
        db.add_column(u'friends_profile', 'blurb',
                      self.gf('django.db.models.fields.CharField')(default='noodles', max_length=200),
                      keep_default=False)

        # Adding field 'Profile.rstatus'
        db.add_column(u'friends_profile', 'rstatus',
                      self.gf('django.db.models.fields.CharField')(default='noodles', max_length=1),
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'friends.activity': {
            'Meta': {'object_name': 'Activity'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'friends.location': {
            'Meta': {'object_name': 'Location'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'homezip': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workzip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'friends.profile': {
            'Meta': {'object_name': 'Profile'},
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['friends.Activity']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'likes_rel_+'", 'to': u"orm['friends.Profile']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['friends']