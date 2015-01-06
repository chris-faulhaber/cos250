# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attendee'
        db.create_table(u'submit_attendee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Course'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Person'])),
        ))
        db.send_create_signal(u'submit', ['Attendee'])

        # Adding model 'Assignment'
        db.create_table(u'submit_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Course'])),
        ))
        db.send_create_signal(u'submit', ['Assignment'])

        # Adding model 'Person'
        db.create_table(u'submit_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'submit', ['Person'])

        # Adding model 'Submission'
        db.create_table(u'submit_submission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Person'])),
            ('submission_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Assignment'])),
            ('test_results', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal(u'submit', ['Submission'])

        # Adding model 'Course'
        db.create_table(u'submit_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Person'])),
        ))
        db.send_create_signal(u'submit', ['Course'])

        # Adding model 'Line'
        db.create_table(u'submit_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['submit.Submission'])),
            ('line_number', self.gf('django.db.models.fields.IntegerField')()),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'submit', ['Line'])


    def backwards(self, orm):
        # Deleting model 'Attendee'
        db.delete_table(u'submit_attendee')

        # Deleting model 'Assignment'
        db.delete_table(u'submit_assignment')

        # Deleting model 'Person'
        db.delete_table(u'submit_person')

        # Deleting model 'Submission'
        db.delete_table(u'submit_submission')

        # Deleting model 'Course'
        db.delete_table(u'submit_course')

        # Deleting model 'Line'
        db.delete_table(u'submit_line')


    models = {
        u'submit.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Course']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'due_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'submit.attendee': {
            'Meta': {'object_name': 'Attendee'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Person']"})
        },
        u'submit.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Person']"})
        },
        u'submit.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'line_number': ('django.db.models.fields.IntegerField', [], {}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Submission']"})
        },
        u'submit.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'submit.submission': {
            'Meta': {'object_name': 'Submission'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Assignment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['submit.Person']"}),
            'submission_date': ('django.db.models.fields.DateTimeField', [], {}),
            'test_results': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['submit']