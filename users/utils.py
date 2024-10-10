from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5MB in bytes
    if image.size > max_size:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")