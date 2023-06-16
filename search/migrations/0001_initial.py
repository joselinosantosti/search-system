# Generated by Django 3.0.3 on 2020-05-31 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PalavraLocalizacao',
            fields=[
                ('idpalavra_localizacao', models.AutoField(primary_key=True, serialize=False)),
                ('localizacao', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'palavra_localizacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Palavras',
            fields=[
                ('idpalavra', models.AutoField(primary_key=True, serialize=False)),
                ('palavra', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'palavras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UrlLigacao',
            fields=[
                ('idurl_ligacao', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'url_ligacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UrlPalavra',
            fields=[
                ('idurl_palavra', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'url_palavra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('idurl', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'urls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PageRank',
            fields=[
                ('idurl', models.OneToOneField(db_column='idurl', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='search.Urls')),
                ('nota', models.FloatField()),
            ],
            options={
                'db_table': 'page_rank',
                'managed': False,
            },
        ),
    ]
