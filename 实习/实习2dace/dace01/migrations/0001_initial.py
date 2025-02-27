from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='姓名')),
                ('num', models.CharField(max_length=16, verbose_name='学号')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('mobile', models.CharField(max_length=16, verbose_name='手机号码')),
                ('hobbit', models.CharField(max_length=32, verbose_name='爱好')),
            ],
        ),
    ]
