from django.shortcuts import render

# Create your views here.

from django.http import Http404
from polling.models import Poll


def list_view(request):
    context = {'polls': Poll.objects.all()}

    return render(request, 'polling/list.html', context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)

    except:
        raise Http404

    if request.method == "POST":
        # name identified
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1

        poll.save()
    # the key
    context = {'poll': poll}

    return render(request, 'polling/details.html', context)

    # return render(request, 'polling/list.html', context)
