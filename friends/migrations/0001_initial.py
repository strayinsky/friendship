# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Demographic'
        db.create_table(u'friends_demographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('age', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('rstatus', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('personality', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('blurb', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'friends', ['Demographic'])

        # Adding model 'Location'
        db.create_table(u'friends_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homezip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('workzip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'friends', ['Location'])

        # Adding model 'Activity'
        db.create_table(u'friends_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'friends', ['Activity'])

        # Adding model 'Like'
        db.create_table(u'friends_like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userA', self.gf('django.db.models.fields.related.ForeignKey')(related_name='like_userA', to=orm['auth.User'])),
            ('userB', self.gf('django.db.models.fields.related.ForeignKey')(related_name='like_userB', to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'friends', ['Like'])

        # Adding model 'UserActivity'
        db.create_table(u'friends_useractivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['friends.Activity'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'friends', ['UserActivity'])


    def backwards(self, orm):
        # Deleting model 'Demographic'
        db.delete_table(u'friends_demographic')

        # Deleting model 'Location'
        db.delete_table(u'friends_location')

        # Deleting model 'Activity'
        db.delete_table(u'friends_activity')

        # Deleting model 'Like'
        db.delete_table(u'friends_like')

        # Deleting model 'UserActivity'
        db.delete_table(u'friends_useractivity')


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
        u'friends.demographic': {
            'Meta': {'object_name': 'Demographic'},
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'blurb': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personality': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'rstatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'friends.like': {
            'Meta': {'object_name': 'Like'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userA': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'like_userA'", 'to': u"orm['auth.User']"}),
            'userB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'like_userB'", 'to': u"orm['auth.User']"})
        },
        u'friends.location': {
            'Meta': {'object_name': 'Location'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'homezip': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workzip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'friends.useractivity': {
            'Meta': {'object_name': 'UserActivity'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['friends.Activity']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['friends']