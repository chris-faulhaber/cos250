# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Attendee'
        db.delete_table(u'submit_attendee')

        # Deleting model 'Person'
        db.delete_table(u'submit_person')

        # Adding field 'Submission.awarded_points'
        db.add_column(u'submit_submission', 'awarded_points',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Submission.output'
        db.add_column(u'submit_submission', 'output',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4096),
                      keep_default=False)


        # Changing field 'Submission.owner'
        db.alter_column(u'submit_submission', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Adding field 'Part.extra_files'
        db.add_column(u'submit_part', 'extra_files',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Part.submit_filename'
        db.add_column(u'submit_part', 'submit_filename',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Part.output_file'
        db.add_column(u'submit_part', 'output_file',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)

        # Adding field 'Part.order'
        db.add_column(u'submit_part', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Attendee'
        db.create_table(u'submit_attendee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Person'])),
        ))
        db.send_create_signal(u'submit', ['Attendee'])

        # Adding model 'Person'
        db.create_table(u'submit_person', (
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'submit', ['Person'])

        # Deleting field 'Submission.awarded_points'
        db.delete_column(u'submit_submission', 'awarded_points')

        # Deleting field 'Submission.output'
        db.delete_column(u'submit_submission', 'output')


        # Changing field 'Submission.owner'
        db.alter_column(u'submit_submission', 'owner_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Person']))
        # Deleting field 'Part.extra_files'
        db.delete_column(u'submit_part', 'extra_files')

        # Deleting field 'Part.submit_filename'
        db.delete_column(u'submit_part', 'submit_filename')

        # Deleting field 'Part.output_file'
        db.delete_column(u'submit_part', 'output_file')

        # Deleting field 'Part.order'
        db.delete_column(u'submit_part', 'order')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'submit.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'submit.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'line_number': ('django.db.models.fields.IntegerField', [], {}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Submission']"})
        },
        u'submit.part': {
            'Meta': {'object_name': 'Part'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Assignment']"}),
            'expected_result': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'extra_files': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'output_file': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'submit_filename': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'test_script': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'tester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.TestRunner']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'submit.submission': {
            'Meta': {'object_name': 'Submission'},
            'awarded_points': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'output': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Part']"}),
            'submission_date': ('django.db.models.fields.DateTimeField', [], {}),
            'test_results': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        u'submit.testrunner': {
            'Meta': {'object_name': 'TestRunner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'script': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['submit']