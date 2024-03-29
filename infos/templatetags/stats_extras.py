from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()
from django.apps import apps


@register.simple_tag
def create_object_count(app=None):

    """fetches all models of the passed in app and returns a
    dict containg the name of each class and the number of instances"""

    if app:
        models = ContentType.objects.filter(app_label=app)
        result = []
        print(models)
        for x in models:
            modelname = x.model
            try:
                fetched_model = ContentType.objects.get(
                    app_label=app, model=modelname).model_class()
                item = {
                    'name': modelname.title(),
                    'count': fetched_model.objects.count()
                }
            except Exception as e:
                item = {
                    'name': x,
                    'count': e
                }
            try:
                item['link'] = fetched_model.get_listview_url()
            except AttributeError:
                item['link'] = None
            result.append(item)
        return result

    else:
        result = [
            {
                'name': 'no parameter passed in',
                'count': '1'
            }
        ]
        return result
