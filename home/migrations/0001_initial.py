# Generated by Django 5.0.7 on 2025-03-20 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('bio', models.TextField()),
                ('long_bio', models.TextField()),
                ('years_of_experience', models.CharField(max_length=200)),
                ('completed_projects', models.CharField(max_length=200)),
                ('awards', models.CharField(max_length=200)),
                ('happy_clients', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('cv', models.FileField(upload_to='cv/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('live_link', models.URLField(default='none')),
                ('github_link', models.URLField(default='none')),
                ('category', models.CharField(choices=[('web', 'Web Development'), ('mobile', 'Mobile Apps'), ('ui', 'UI/UX Design'), ('backend', 'Backend')], default='web', max_length=20)),
                ('year', models.IntegerField(default=2023)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnichalExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percent', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('front-end', 'Front-End'), ('back-end', 'Back-End')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_overview', models.TextField()),
                ('key_features', models.TextField()),
                ('what_ilearned', models.TextField(blank=True, null=True)),
                ('diagram_file', models.FileField(blank=True, null=True, upload_to='diagram/')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
                ('PojTechnology', models.ManyToManyField(blank=True, related_name='project_technologies', to='home.technology')),
            ],
        ),
        migrations.CreateModel(
            name='DevelopmentStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('week', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='home.projectdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to='home.projectdetail')),
            ],
            options={
                'verbose_name_plural': 'Challenges',
            },
        ),
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_gallery/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='home.project')),
            ],
            options={
                'ordering': ['order', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProjectMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_name', models.CharField(max_length=200)),
                ('metric_value', models.CharField(max_length=200)),
                ('project_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='home.projectdetail')),
            ],
            options={
                'verbose_name': 'Project Metric',
                'verbose_name_plural': 'Project Metrics',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.ManyToManyField(to='home.technology'),
        ),
        migrations.CreateModel(
            name='ProjectTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.technology')),
            ],
            options={
                'unique_together': {('project', 'technology')},
            },
        ),
    ]
