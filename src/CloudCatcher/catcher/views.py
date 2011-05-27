from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def index(request):
    t = loader.get_template('catcher/index.html')
    c = Context({})
    return HttpResponse(t.render(c))


@csrf_exempt
def save_image(request):
    if request.POST:
        # save it somewhere
        f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpg', 'wb')
        f.write(request.raw_post_data)
        f.close()
        # return the URL
        return HttpResponse('http://localhost:8000/site_media/webcamimages/someimage.jpg')
    else:
        return HttpResponse('no data')