from django.conf import settings


TEMPLATE_CHOICES = getattr(settings, 'DJANGOCMS_SLIDES_TEMPLATE_CHOICES', (
    ('default', 'default'),
))