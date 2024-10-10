from django import template

register = template.Library()


@register.simple_tag
def get_full_url(request, lang_code):
    url = request.path.split('/')
    url[1] = lang_code
    return '/'.join(url)