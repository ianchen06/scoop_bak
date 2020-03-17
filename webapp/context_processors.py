from django.conf import settings

def site_meta(request):
    return {'SITE_TITLE': settings.SITE_TITLE}
