# coding=utf-8
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

NETWORKS_CHOICES = (
    ('vk', _('vkontakte')),
    ('fb', _('facebook')),
    ('twitter', _('twitter')),
    ('instagram', _('instagram')),
    ('youtube', _('youtube')),
)


class SocialNetworks(models.Model):
    type = models.CharField(_("Type"), choices=NETWORKS_CHOICES, max_length=16)
    url = models.URLField(_("URL"))
    weight = models.PositiveIntegerField(default=0, blank=False, null=False)

    @property
    def img_path(self):
        ext_name = getattr(settings, 'SOCIALLINKS_ICON_FORMAT', 'png')
        return 'img/sociallinks/{0}.{1}'.format(self.type, ext_name)

    class Meta:
        ordering = ['weight', ]
        verbose_name = _("Social Network")
        verbose_name_plural = _("Social Networks")

    def __unicode__(self):
        return dict(NETWORKS_CHOICES)[self.type]
