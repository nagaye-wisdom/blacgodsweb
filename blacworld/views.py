from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import (DetailView,ListView)
from member.models import Member


def home(request):
    return render(request,'blacworld/home.html')

def about(request):
    return render(request,'blacworld/about.html')


class MembersListView(ListView):
    template_name = 'blacworld/members.html'
    context_object_name = 'members'
    def get_queryset(self):
        return User.objects.all()

class MemberDetailView(DetailView):
    model = Member
    template_name = 'blacworld/members_detail.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


def member_search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submit_button= request.GET.get('submit')

        if query is not None:
            lookups= Q(first_name__icontains=query)| Q(last_name__icontains=query)

            results= User.objects.filter(lookups).distinct()

            context={'results': results,
                     'submit_button': submit_button}

            return render(request, 'blacworld/member_search.html', context)

        else:
            return render(request, 'blacworld/member_search.html')

    else:
        return render(request, 'blacworld/member_search.html')
