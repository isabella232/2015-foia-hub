# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.text import slugify
import localflavor.us.models

def change_office_slugs(apps, schema_editor):
    """ Make the Office slugs unique. """
    Office = apps.get_model("foia_hub", "Office")
    db_alias = schema_editor.connection.alias

    for office in Office.objects.using(db_alias).all():
        office_slug = slugify(office.name)[:50]
        office.slug = ('%s--%s' % (office.agency.slug, office_slug))[:100]
        office.save()

class Migration(migrations.Migration):
    dependencies = [
        ('foia_hub', '0003_auto_20141001_1633')
    ]

    operations = [
        migrations.RunPython(
            change_office_slugs,
        )
    ]
