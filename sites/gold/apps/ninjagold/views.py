from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
import random, datetime, json

class building(object):
    def __init__(self,name,title,description,low,high):
        self.reward = 0
        self.title = title
        self.description = description
        self.earn_min = low
        self.earn_max = high
        self.path = 'earn'
        self.hidden = name
    def earn(self):
        self.reward = random.randint(self.earn_min,self.earn_max)
        return self.reward
    def json_description(self):
        return {'name':self.hidden,'title':self.title, 'description':self.description, 'path':self.path, 'hidden':self.hidden}


farm = building('farm',"Farming for Cash Crops","Earn 10-20 Coins",10,20)
cave = building('cave',"Spelunking for Pirate Treasure","Earn 5-10 Coins",5,10)
raid = building('raid',"Raiding a Castle","Earn 2-5 Coins",2,5)
casino = building('casino',"Gamble at the Casino","Win or Lose upto 50 Coins",-50,51)


def addLine(lines,message,reward,score):
    now = [datetime.datetime.now()]
    nowj = json.dumps(now, cls=DjangoJSONEncoder)

    line={}
    line['activity'] = message
    line['reward'] = reward
    line['balance'] = score
    # line['time'] = now
    line['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # insert the most recent activity at the top of the ledger
    lines.append(line)
    return(lines)


# Create your views here.
def index(request):
    if not 'score' in request.session:
        request.session['score'] = 0
        request.session['lines'] = []

    context = { 'locations':[
                farm.json_description(),
                cave.json_description(),
                raid.json_description(),
                casino.json_description()
                ]
            }

    return render(request,'ninjagold/index.html', context)


def earn(request, *args):

    if not 'score' in request.session:
        return redirect(index)

    activity = request.POST['hidden']
# set rewards for farming
    if activity == 'farm':
        reward = farm.earn()
        message = "Earned {r} gold coins for farming.\n".format(r=reward)
# set rewards for spelunking
    if activity == 'cave':
        reward = cave.earn()
        message = "Earned {r} gold coins while spelunking in a pirate cave.\n".format(r=reward)
# set rewards for raiding a castle
    if activity == 'raid':
        reward = raid.earn()
        message = "Stole {r} gold coins while raiding a castle.\n".format(r=reward)
    if activity == 'casino':
        reward = casino.earn()
        message = "Won {r} gold coins gambling at a casino.".format(r=reward)
        if reward < 0:
            message = "Lost {r} gold coins gambling at a casino.".format(r=-reward)

    request.session['score'] += reward
    # build the line {} for insertion into the lines []
    request.session['lines'] = addLine(request.session['lines'],message,reward,request.session['score'])

    return redirect(index)
