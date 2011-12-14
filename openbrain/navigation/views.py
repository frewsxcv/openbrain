from core.models import Category, Topic, Video
from django.shortcuts import HttpResponse

# this only checks 2 nested categories and only checks the
# most nested for loop for videos

def list_all(request):
    r = ""
    for x in Category.objects.filter(parent=None):
        r += "<ul><li>" + str(x) + "</li>"
        for c in Category.objects.filter(parent=x):
            r += "<ul><li>" + str(c) + "</li>"
            for t in Topic.objects.filter(category=c):
                r += "<ul><li>" + str(t) + "</li>"
                r += "<ul>"
                for v in Video.objects.filter(topic=t, next_video=None):
                    r += "<li>" + str(v.get_series()) + "</li>"
                r += "</ul></ul>"
            r += "</ul>"
        r += "</ul>"
    return HttpResponse(r)
