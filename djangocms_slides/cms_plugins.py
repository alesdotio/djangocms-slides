from django.contrib import admin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_slides.models import Slides, SlidesItem
from django.utils.translation import ugettext_lazy as _


class SlidesItemInline(admin.StackedInline):
    model = SlidesItem
    extra = 0
    fieldsets = (
        ('Main', {
            'fields': (('ordering', 'template'), ('image', 'bg_color'), 'content', 'page', 'url', 'link_blank'),
        }),
    )


class SlidesPlugin(CMSPluginBase):
    name = _('Slides Plugin')
    model = Slides
    admin_preview = False
    inlines = [SlidesItemInline, ]
    fieldsets = (
        ('Main', {
            'fields': ('timeout',),
        }),
    )

    render_template = 'djangocms_slides/slides.html'

    def render(self, context, instance, placeholder):
        context.update({
            'items': instance.items.select_related('image').all(),
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(SlidesPlugin)
