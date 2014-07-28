# coding=utf-8
from django import template
from sociallinks.models import SocialNetworks

register = template.Library()

@register.inclusion_tag('sociallinks/icons.html')
def social_icons():
    icons = SocialNetworks.objects.all()

    return {
        "objects": icons,
    }
