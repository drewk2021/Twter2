from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Twt, TwtPoster, Reply



def home(request):
    # view sends the request to the home.html template; for sign ups and logins.
    return render(request, 'twts/home.html')

def indexnewuser(request):
    # builds the new TwtPoster object from the sign up form data in request and updates the database
    newUser = TwtPoster(twtposter_text=request.POST['email'],twtposter_password=request.POST['psw'])
    newUser.save()
    # subsequently shows the 5 most recent twts via the index template
    latest_twt_list = Twt.objects.order_by('-pub_date')[:5]
    context = {'latest_twt_list': latest_twt_list, 'user': newUser}
    return render(request, 'twts/index.html', context)


class DetailView(generic.DetailView):
    model = Twt
    template_name = 'twts/detail.html'



def posttwt(request,posteroftwt_id):
    # posting a new twt to the database based on the index.html template form provided
    newTwt = Twt(twt_text=request.POST['newesttwt'],twtposter=get_object_or_404(TwtPoster,id=posteroftwt_id))
    newTwt.save()


    # inefficient implementation below, can functionalize this context builiding later
    latest_twt_list = Twt.objects.order_by('-pub_date')[:5]
    context = {'latest_twt_list': latest_twt_list, 'user': newTwt.twtposter  }
    return render(request, 'twts/index.html', context)


def vote(request, twt_id):
    # This adds a like or dislike to a given twt, and returns a different TwtPoster to theindex.html template.
    twt = get_object_or_404(Twt, pk=twt_id)
    # when both like and dislike options are null (and there's only the crsf_token in the request.POST dictionary), the user didn't choose a choice.
    if  len(request.POST) == 1:
        # Redisplay the twt voting form.
        return render(request, 'twts/detail.html', {
            'twt': twt,
            'error_message': "You didn't select an option.",
        })
    elif ('like' in request.POST.keys()): # when the like can be accessed in the request.POST dictionary, the user voted to like the twt.
        twt.likes += 1
    else:
        twt.dislikes += 1

    twt.save()

    # inefficient implementation below, can functionalize this context builiding later
    latest_twt_list = Twt.objects.order_by('-pub_date')[:5]
    context = {'latest_twt_list': latest_twt_list, 'user': twt.twtposter  } # passing in a new user TwtPoster object for the twt just selected for a vote
    # this is non - ideal, but I thought it would be interesting switching accounts.
    return render(request, 'twts/index.html', context)




def replytotwt(request, twt_id):
    # builds a new reply to the twt, protecting anonymity on the detail.html template
    reply = Reply(reply_text=request.POST['replytext'],twt=get_object_or_404(Twt,id=twt_id),reply_poster=get_object_or_404(TwtPoster,id=1))
    reply.save()

    # inefficient implementation below, can functionalize this context builiding later
    latest_twt_list = Twt.objects.order_by('-pub_date')[:5]
    context = {'latest_twt_list': latest_twt_list, 'user': reply.reply_poster  } # passing in a new user TwtPoster object for the twt just selected for a vote
    # this is non - ideal, but I thought it would be interesting switching accounts.
    return render(request, 'twts/index.html', context)





def authenticate(request):
    # verifies the user's password is correct from the home.html template form
    user = get_object_or_404(TwtPoster,twtposter_text=request.POST['uname']) # TwtPoster based on supplied email in the login form
    try:
        if user.twtposter_password == request.POST['psw']: # password is correct
            # inefficient implementation below, can functionalize this context builiding later
            latest_twt_list = Twt.objects.order_by('-pub_date')[:5]
            context = {'latest_twt_list': latest_twt_list, 'user': user} # passing in the current user TwtPoster object
            return render(request, 'twts/index.html', context)
        else:
            return render(request, 'twts/detail.html', {
                'twt': user,
                'error_message': "No such user",
                })
    except(KeyError,TwtPoster.DoesNotExist):
        return render(request, 'twts/detail.html', {
            'twt': user,
            'error_message': "No such user.",
        })




# Create your views here.
