# Generated by Django 2.1.4 on 2019-03-16 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_user',
            fields=[
                ('farmer_idno', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='rahul', max_length=400, null=True)),
                ('last_name', models.CharField(default='moorthy', max_length=400, null=True)),
                ('address', models.CharField(default='b302', max_length=100, null=True)),
                ('district', models.CharField(default='pune', max_length=100, null=True)),
                ('state', models.CharField(default='Maharashtra', max_length=100, null=True)),
                ('age', models.IntegerField(default=20, null=True)),
                ('farmer_reg_id', models.CharField(default='abcd', max_length=100, null=True)),
                ('phone_no', models.CharField(default='8805979825', max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rent_hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=100)),
                ('equipment_quantity', models.IntegerField()),
                ('equipment_age', models.IntegerField(blank=True, null=True)),
                ('equipment_renting_price', models.IntegerField(blank=True, null=True)),
                ('owner_phoneno', models.CharField(default='8805979825', max_length=100, null=True)),
                ('status_bit', models.BooleanField(blank=True, default=False)),
                ('owner_district', models.CharField(default='pune', max_length=100, null=True)),
                ('owner_name', models.CharField(default='rahul', max_length=400, null=True)),
                ('farmer_id_rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.farmer_user')),
            ],
        ),
    ]
