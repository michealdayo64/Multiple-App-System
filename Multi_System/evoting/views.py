from django.shortcuts import render, redirect
from .models import CandidateCategory
from django.contrib import messages
from account.models import CustomUser

# Create your views here.

# CANDIDATE HOMEPAGE
def cHome_page(request):
    return render(request, 'evoting/candidate/index.html')

# VOTERS HOMEPAGE
def vHome_page(request):
    candidData = CandidateCategory.objects.all()
    context = {
        'candidData': candidData
    }
    return render(request, 'evoting/voter/index.html', context)

def vDetail_page(request, id):
    candidDetail = CandidateCategory.objects.get(id = id)
    voted = []
    for i in candidDetail.user_voted.all():
        #print(i.username)
        voted.append(i.username)
    print(voted)
    #candid = CandidateName.objects.filter(pk = candidDetail)
    context = {
        'candidDetail': candidDetail,
        'voted': voted
    }
    return render(request, 'evoting/voter/vote.html', context)

def voteCandidate(request, id):
    if request.user.is_authenticated:
        user = request.user

        can = CandidateCategory.objects.get(user = id)
        print(can.pk)
        voted = []
        for ca in can.user_voted.all():
            voted.append(ca.username)
        custom_user = CustomUser.objects.get(pk = id)
        #print(cust.pk) 
        if not user.username in voted:
            custom_user.vote_count += 1
            custom_user.save()
            user.save()
            messages.warning(request, f"You voted successfully for {can.name} category")
        else:
            messages.warning(request, f"You have already voted for someone for {can.name} candidate")
        can.user_voted.add(user)
        
        return redirect("evoting:vHome-page")

def admimDashboard(request):
    total_users = CustomUser.objects.all().count()
    registered_candidate = CustomUser.objects.filter(user_type = "2").count()
    registered_voters = CustomUser.objects.filter(user_type = "3").count()
    users = CustomUser.objects.all()
    aall = []
    for i in users:
        aall.append(i.id)
    
    voters = CandidateCategory.objects.filter(user_voted__in = aall).count()

    context = {
        'total_users': total_users,
        'registered_candidate': registered_candidate,
        'registered_voters': registered_voters,
        'total_voters': voters
    }
    return render(request, "evoting/voter/result.html", context)


