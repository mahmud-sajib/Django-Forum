# Generated by Django 2.2 on 2020-04-14 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20200414_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='downvote',
            new_name='downvotes',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='upvote',
            new_name='upvotes',
        ),
    ]
