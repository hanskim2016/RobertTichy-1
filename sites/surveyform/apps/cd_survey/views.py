from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    locations = [
    "San Jose", "Seattle", "Chicago", "New York City", "Dallas", "online"
    ]
    locations.sort()
    langs = ["Python","Javascript","HTML","CSS","C++","Swift"]
    langs.sort()
    passed_in = {   'locations':locations,
                    'languages':langs
    }
    try:
        a = request.session['errors']
        print "a=",a
    except:
        request.session['errors'] = False
        print request.session['errors']


    print passed_in
    # it implicitly assumes that I am already looking inside the templates folder of
    # the app path...
    return render(request,'cd_survey/index.html',passed_in)

def post(request):
    print "Got Post Info"

    name = request.POST['name']
    comments = request.POST['comments'].strip()
    lang_choice = request.POST['language']
    location = request.POST['location']

    request.session['errors'] = False

    request.session['comments'] = comments.strip()
    request.session['name'] = name
    request.session['language'] = lang_choice
    request.session['location'] = location

    errors=[]
    if len(name) < 1:
        #error name too short
        errors.append("Name cannot be empty.")
        request.session['errors'] = True
    if len(comments) < 1:
        #comments too short
        errors.append("Comments are required.  Thank you.")
        request.session['errors'] = True
    if len(comments) > 120:
        #comments too long
        errors.append("Comments need to be kept under 120 characters.  Yours are {l}.".format(l=len(comments)))
        request.session['errors'] = True

    #If no errors in form then proceed to write the data to the session or DB.
    #Otherwise let everything fall down to the return redirect
    if request.session['errors'] == False:
        print "No Errors, show success page"

        try:
            request.session['submits'] +=1
        except:
            request.session['submits'] =1

        passed_in = {   'location': request.session['location'],
                        'language': request.session['language'],
                        'name':request.session['name'],
                        'comments':request.session['comments']
        }
        del request.session['comments'], request.session['name'], request.session['language'], request.session['location'], request.session['errors']
        return render(request,'cd_survey/result.html', passed_in)

    # redirects back to the '/' route

    request.session['err_list'] = errors

    return redirect(index)
