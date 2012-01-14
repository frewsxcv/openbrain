from django.http import HttpResponse
from core.models import Category, Topic, Video
import json
import urllib


def json_api(req, group, name):
    http_res = HttpResponse(mimetype="application/json")
    if group.lower() == "category":
        res = _category_info(name) if name else {}
        res.update(_subcategories(name))
    elif group.lower() == "topic":
        res = _topic_info(name)
        #res.update(_subtopics(name))
    #elif group.lower() == "video":
        #res = _video_res(name)
    else:
        res = {"msg": "'{0}' is not a valid group".format(group),
               "type": "error"}
    http_res.write(json.dumps(res))
    return http_res


def _category_info(cat, subcat=False):
    """
    Retrieve info for an inputted Category object or name
    """
    res = {}
    try:
        if isinstance(cat, unicode):
            cat = Category.objects.get(name=cat)
    except:
        res["msg"] = "Category '{0}' not found".format(cat)
        res["type"] = "error"
    else:
        res["name"] = cat.name
        if not subcat:
            res["type"] = "category"
            res["parent"] = None if not cat.parent else cat.parent.name
            res["topics"] = []
            for t in Topic.objects.filter(category__name=cat):
                res["topics"].append(_topic_info(t.name))
        else:
            res["type"] = "subcategory"
    return res


def _subcategories(name):
    if name:
        sub_cats = Category.objects.filter(parent__name=name)
        key = "subcategories"
    else:
        sub_cats = Category.objects.filter(parent=None)
        key = "categories"
    res = {key: []}
    for c in sub_cats:
        res[key].append(_category_info(c, True))
    return res


def _topic_info(name):
    res = {}
    try:
        topic = Topic.objects.get(name=name)
    except:
        res["msg"] = "Category '{0}' not found".format(name)
        res["type"] = "error"
    else:
        res["name"] = topic.name
        res["category"] = topic.category.name
        #res["name"] = urllib.quote(topic.name)
        #for t in Topic.objects.filter(name=name):
            #res.append({"name": t.name})
    return res
