from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_post_options_post_published_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="built",
            new_name="solution",
        ),
    ]
