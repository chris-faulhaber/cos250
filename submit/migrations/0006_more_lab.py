# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.v2 import DataMigration


class Migration(DataMigration):

    def forwards(self, orm):
        runner = orm.TestRunner.objects.get(
            script='nand2tetris/HardwareSimulator.sh'
        )

        lab1, v = orm.Assignment.objects.get_or_create(
            description='Lab 1',
            due_date=datetime.date(2015, 1, 28),
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='And',
            tester=runner,
            test_script='labs/01/And.tst',
            extra_files='labs/01/And.cmp',
            submit_filename='And.hdl',
            output_file='And.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='And16',
            tester=runner,
            test_script='labs/01/And16.tst',
            extra_files='labs/01/And16.cmp',
            submit_filename='And16.hdl',
            output_file='And16.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='DMux',
            tester=runner,
            test_script='labs/01/DMux.tst',
            extra_files='labs/01/DMux.cmp',
            submit_filename='DMux.hdl',
            output_file='DMux.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )


        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='DMux4Way',
            tester=runner,
            test_script='labs/01/DMux4Way.tst',
            extra_files='labs/01/DMux4Way.cmp',
            submit_filename='DMux4Way.hdl',
            output_file='DMux4Way.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='DMux8Way',
            tester=runner,
            test_script='labs/01/DMux8Way.tst',
            extra_files='labs/01/DMux8Way.cmp',
            submit_filename='DMux8Way.hdl',
            output_file='DMux8Way.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Mux',
            tester=runner,
            test_script='labs/01/Mux.tst',
            extra_files='labs/01/Mux.cmp',
            submit_filename='Mux.hdl',
            output_file='Mux.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Mux4Way16',
            tester=runner,
            test_script='labs/01/Mux4Way16.tst',
            extra_files='labs/01/Mux4Way16.cmp',
            submit_filename='Mux4Way16.hdl',
            output_file='Mux4Way16.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Mux8Way16',
            tester=runner,
            test_script='labs/01/Mux8Way16.tst',
            extra_files='labs/01/Mux8Way16.cmp',
            submit_filename='Mux8Way16.hdl',
            output_file='Mux8Way16.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Mux16',
            tester=runner,
            test_script='labs/01/Mux16.tst',
            extra_files='labs/01/Mux16.cmp',
            submit_filename='Mux16.hdl',
            output_file='Mux16.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Not',
            tester=runner,
            test_script='labs/01/Not.tst',
            extra_files='labs/01/Not.cmp',
            submit_filename='Not.hdl',
            output_file='Not.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Not16',
            tester=runner,
            test_script='labs/01/Not16.tst',
            extra_files='labs/01/Not16.cmp',
            submit_filename='Not16.hdl',
            output_file='Not16.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Or',
            tester=runner,
            test_script='labs/01/Or.tst',
            extra_files='labs/01/Or.cmp',
            submit_filename='Or.hdl',
            output_file='Or.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Or8Way',
            tester=runner,
            test_script='labs/01/Or8Way.tst',
            extra_files='labs/01/Or8Way.cmp',
            submit_filename='Or8Way.hdl',
            output_file='Or8Way.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Or16',
            tester=runner,
            test_script='labs/01/Or16.tst',
            extra_files='labs/01/Or16.cmp',
            submit_filename='Or16.hdl',
            output_file='Or16.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        orm.Part.objects.get_or_create(
            assignment=lab1,
            name='Xor',
            tester=runner,
            test_script='labs/01/Xor.tst',
            extra_files='labs/01/Xor.cmp',
            submit_filename='Xor.hdl',
            output_file='Xor.out',
            expected_result='End of script - Comparison ended successfully',
            weight=10,
        )

        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
