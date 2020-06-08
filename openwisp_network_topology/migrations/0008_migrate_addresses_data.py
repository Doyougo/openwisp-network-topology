# Generated by Django 2.2.9 on 2020-01-3 13:58

from django.db import migrations
from openwisp_network_topology.migrations import migrate_addresses

migrate_addresses.__defaults__ = ('topology',)


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0007_create_new_address_field'),
    ]

    operations = [migrations.RunPython(migrate_addresses)]
