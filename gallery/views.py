from django.shortcuts import render
from django.db.models import Q
from django.views.generic import (DetailView,ListView)
from . models import Video,Picture


class VideoListView(ListView):
    template_name = 'blacworld/video.html'
    context_object_name = 'videos'

    def get_queryset(self):
        return Video.objects.all()


class VideoDetailView(DetailView):
    template_name = 'blacworld/videoDetailView.html'
    context_object_name='videos'

    def get_queryset(self):
        return Video.objects.all()


def video_search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submit_button= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query)

            results= Video.objects.filter(lookups).distinct()

            context={'results': results,
                     'submit_button': submit_button}

            return render(request, 'blacworld/video_search.html', context)

        else:
            return render(request, 'blacworld/video_search.html')

    else:
        return render(request, 'blacworld/video_search.html')


class PictureListView(ListView):
    template_name = 'blacworld/pictures.html'
    context_object_name = 'Pictures'

    def get_queryset(self):
        return Picture.objects.all()

class PictureDetailView(DetailView):
    template_name = 'blacworld/picture_detail.html'
    context_object_name='pictures'

    def get_queryset(self):
        return Picture.objects.all()


def picture_search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submit_button= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query)

            results= Picture.objects.filter(lookups).distinct()

            context={'results': results,
                     'submit_button': submit_button}

            return render(request, 'blacworld/picture_search.html', context)

        else:
            return render(request, 'blacworld/picture_search.html')

    else:
        return render(request, 'blacworld/picture_search.html')