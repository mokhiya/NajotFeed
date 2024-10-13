import django.db.models.deletion
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_usermodel_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='users', validators=[users.models.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usermodel', to=settings.AUTH_USER_MODEL),
        ),
    ]
