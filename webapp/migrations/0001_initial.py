# Generated by Django 3.0.7 on 2020-06-24 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('live', models.BooleanField(default=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.Page')),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('body', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('webapp.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.Page')),
                ('intro', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('webapp.page',),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Page')),
            ],
        ),
    ]
