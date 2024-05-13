import datetime
from django import template
from ..models import *

register = template.Library()

@register.simple_tag
def todays_date():
    return datetime.datetime.now().strftime("%d %b, %Y")

@register.simple_tag
def my_name():
    name="Diana Hurtado"
    return name

@register.simple_tag
def no_songs():
    songs=Songs.objects.all()
    number=0
    for i in songs:
        number+=1
    return number