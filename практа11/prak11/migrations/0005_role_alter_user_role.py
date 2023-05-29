# Generated by Django 4.2 on 2023-05-28 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prak11', '0004_user_role_alter_item_teacher_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='prak11.role'),
        ),
    ]
