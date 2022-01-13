from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    swear = ['хуй', 'мартышлюшка', 'ебоклаус']
    for word in swear:
        clean_text = value.replace(str(word), '***')
        value = clean_text
    return clean_text
