from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PageField
from djangocms_slides.settings import TEMPLATE_CHOICES
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField


class Slides(CMSPlugin):
    timeout = models.PositiveIntegerField(_('timeout'), default=8, help_text=_('If greater than 0, the animation will auto-play every X seconds.'))

    def __unicode__(self):
        return 'Slides %s' % self.pk

    class Meta:
        verbose_name = _('Slides')
        verbose_name_plural = _('Slides')

    def copy_relations(self, oldinstance):
        for item in oldinstance.items.all():
            item.pk = None
            item.parent = self
            item.save()


class SlidesItem(models.Model):
    parent = models.ForeignKey(Slides, related_name='items')
    ordering = models.IntegerField(_('ordering'), db_index=True, default=100)
    template = models.CharField(_('template'), max_length=60, choices=TEMPLATE_CHOICES, default=TEMPLATE_CHOICES[0][0])
    image = FilerImageField(verbose_name=_('image'), related_name='slides_image_set', blank=True, null=True)
    bg_color = models.CharField(_('background color'), max_length=20, blank=True, help_text=_('CSS value, for example: #1f49ff'))
    content = HTMLField(_('content'), blank=True)

    # link stuff
    page = PageField(verbose_name=_('Link to Page'), blank=True, null=True)
    url = models.URLField(_('Link to URL'), blank=True, null=True)
    link_blank = models.BooleanField(_('Open the link in a blank window'), max_length=60, blank=True)

    def get_url(self):
        if self.page_id:
            return self.page.get_absolute_url()
        elif self.url:
            return self.url
        return None

    class Meta:
        verbose_name = _('Slides Item')
        verbose_name_plural = _('Slides Items')
        ordering = ('ordering',)