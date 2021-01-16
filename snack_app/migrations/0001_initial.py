# Generated by Django 2.2 on 2021-01-14 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='login_app.User')),
                ('user_dislikes', models.ManyToManyField(related_name='disliked_ideas', to='login_app.User')),
                ('user_likes', models.ManyToManyField(related_name='liked_ideas', to='login_app.User')),
            ],
        ),
    ]