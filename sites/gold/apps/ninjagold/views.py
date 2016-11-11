from django.shortcuts import render, redirect
import random
def addLine(lines,message,reward,score):
    line={}
    line['activity'] = message
    line['reward'] = reward
    line['balance'] = score
    # insert the most recent activity at the top of the ledger
    lines.insert(0,line)
    return(lines)
# Create your views here.
def index(request):
    context={}
    print "index()"
    if 'score' in request.session:
        print "-"*40
        print "playing"
        print "-"*40
        score = request.session['score']
        lines = request.session['lines']
    else:
        print "*"*40
        print "starting"
        print "*"*40
        request.session['score'] = 0
        request.session['lines'] = []
        score = 0
        lines = []
    return render(request,'ninjagold/index.html',context)
def earn(request, *args):
    print "-"*40
    print "earn"
    print "-"*40
    if 'score' in request.session:
        score = int(request.session['score'])
    else:
        print "CRAP! no score ?!"
        return redirect(index)

    lines = request.session['lines']

    activity = request.POST['hidden']
# set rewards for farming
    if activity == 'farm':
        reward = random.randrange(10,20)
        message = "Earned {r} gold coins for farming.\n".format(r=reward)
# set rewards for spelunking
    if activity == 'cave':
        reward = random.randrange(5,10)
        message = "Earned {r} gold coins while spelunking in a pirate cave.\n".format(r=reward)
# set rewards for raiding a castle
    if activity == 'raid':
        reward = random.randrange(2,5)
        message = "Stole {r} gold coins while raiding a castle.\n".format(r=reward)

    request.session['score'] += reward
    # build the line {} for insertion into the lines []
    request.session['lines'] = addLine(request.session['lines'],message,reward,request.session['score'])

    return redirect(index)
def gamble(request):
    if 'score' in request.session:
        score = request.session['score']
    else:
        print "CRAP! no score ?!"
        return redirect(index)

    reward = random.randrange(0,50)
    message = "Won {r} gold coins gambling at a casino.".format(r=reward)
    if random.randrange(0,2) >= 1:
        message = "Lost {r} gold coins gambling at a casino.".format(r=reward)
        reward= -reward

    request.session['score'] += reward
    # build the line {} for insertion into the lines []
    request.session['lines'] = addLine(request.session['lines'],message,reward,request.session['score'])

    return redirect(index)
