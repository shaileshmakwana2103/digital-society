# Generated by Django 4.1.7 on 2023-03-22 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verify', models.BooleanField(default=False)),
                ('otp', models.IntegerField(default=456)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Societymember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=30, null=True)),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('block_no', models.CharField(blank=True, max_length=10, null=True)),
                ('No_of_familymembers', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, max_length=20, null=True)),
                ('vehical_details', models.CharField(blank=True, max_length=30, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('House_ownership', models.CharField(blank=True, max_length=20, null=True)),
                ('City', models.CharField(blank=True, max_length=20, null=True)),
                ('pic', models.FileField(default='media/default.png', upload_to='media/upload')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=30, null=True)),
                ('subject', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.notice')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='notice',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36)),
                ('amount', models.CharField(max_length=36)),
                ('duedate', models.DateField(max_length=36)),
                ('status', models.CharField(default='PENDING', max_length=36)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.societymember')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='EventsViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
        migrations.CreateModel(
            name='ComplaintsViewDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.complaints')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='complaints',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=30)),
                ('pic', models.FileField(default='media/chairman.png', upload_to='media/upload')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user')),
            ],
        ),
    ]
