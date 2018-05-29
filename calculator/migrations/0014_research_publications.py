# Generated by Django 2.0.1 on 2018-02-25 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calculator', '0013_delete_research_publications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research_Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_journals', models.IntegerField()),
                ('impact_factor', models.IntegerField(blank=True, default=1)),
                ('single_author', models.BooleanField(default=False)),
                ('two_author', models.BooleanField(default=False)),
                ('three_author', models.BooleanField(default=False)),
                ('first_corresponding_author', models.BooleanField(default=False)),
                ('no_of_authors', models.IntegerField(blank=True, default=0)),
                ('no_of_papers_sci_journal', models.IntegerField()),
                ('no_of_papers_scopus_journal', models.IntegerField()),
                ('no_of_conference_papers', models.IntegerField()),
                ('no_of_books_published', models.IntegerField()),
                ('no_of_short_courses', models.IntegerField()),
                ('no_of_seminars', models.IntegerField()),
                ('no_of_professional_training_received', models.IntegerField()),
                ('no_of_sponsored_research_project', models.IntegerField()),
                ('score', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]