"""
views
"""

# pylint: disable=E1101
# pylint: disable=W0707

from django.shortcuts import render

# Create your views here.

from django.http import Http404
from polling.models import Poll


def list_view(request):
    """
    List View
    """

    # gets all the poll objects

    context = {'polls': Poll.objects.all()}

    return render(request, 'polling/list.html', context)


def detail_view(request, poll_id):
    """
    Detail View
    """
    try:

        # gets the poll for a particular primary key
        # so is this reading from the sqlite3 database?

        poll = Poll.objects.get(pk=poll_id)

    except:

        raise Http404

    if request.method == "POST":
        # name identified
        # "vote" is the name of the input button in details.html
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1

        poll.save()

    # the key used in details.html

    context = {'poll': poll}

    # not to be confused with the url address in the browser
    # this represents the html file in the polling directory

    return render(request, 'polling/details.html', context)

    # return render(request, 'polling/list.html', context)
