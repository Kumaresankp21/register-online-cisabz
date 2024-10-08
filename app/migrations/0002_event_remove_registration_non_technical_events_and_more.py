# Generated by Django 5.1 on 2024-09-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("technical", "Technical"),
                            ("non_technical", "Non-Technical"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="registration",
            name="non_technical_events",
        ),
        migrations.RemoveField(
            model_name="registration",
            name="technical_events",
        ),
        migrations.AddField(
            model_name="registration",
            name="non_technical_events",
            field=models.ManyToManyField(
                blank=True, related_name="non_technical_registrations", to="app.event"
            ),
        ),
        migrations.AddField(
            model_name="registration",
            name="technical_events",
            field=models.ManyToManyField(
                blank=True, related_name="technical_registrations", to="app.event"
            ),
        ),
    ]
