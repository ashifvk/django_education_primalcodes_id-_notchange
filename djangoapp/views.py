from django.shortcuts import render,redirect
from .models import Candidate,Education
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'form.html')

def addeducation(request):
    success = False
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        dict=zip(
            request.POST.getlist('course'),
            request.POST.getlist('university'),
            request.POST.getlist('year'),
        )
        data_dict=[{'course':course,
                    'university':university,
                    'year':year,}
                    for course,university,year in dict]
        print(data_dict)
        print(name)
        print(email)
        if Candidate.objects.filter(email=email).exists():
             return HttpResponse("duplicate Email found", status=400)
        add=Candidate(name=name,email=email)
        add.save()
        r_id=add.id
        for i in data_dict:
            course = i.get('course')
            university = i.get('university')
            year = i.get('year')
            candidate_instance = Candidate.objects.get(id=r_id)

            data1=Education(reg_id=candidate_instance,course=course,university=university,year=year)
            data1.save()
        success = True   
    return render(request,'form.html',{'success': success})


def alluser(request):
    users=Candidate.objects.all()
    # for i in users:
    #    name= i.name
    #    print(name)
    context={'user':users}
    #    return HttpResponse("ok", status=200)
    return render(request,'alluser.html',context)


def editData(request,id):
    userdata=Candidate.objects.get(id=id)
    ed_data=Education.objects.filter(reg_id=userdata).all()
    context={'userdata':userdata}
    context2={'ed_data':ed_data}
    print(ed_data.values_list())
    print(ed_data.values())
    print(userdata)
    print(userdata.name)
    print(userdata.email)
    # return HttpResponse("ok", status=200)
    return render(request,'edit.html',locals())




def updateData(request,id):
    success = False

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        print(name)
        print(email)
        Candidate.objects.filter(id=id).update(name=name,email=email)

        course_values = request.POST.getlist('course')
        print(course_values)
        # print(len(course_values))
        university_values = request.POST.getlist('university')
        print(university_values)
        year_values = request.POST.getlist('year')
        print(year_values)
        hid_values = request.POST.getlist('hid')
        print(hid_values)
        temp=hid_values
        # print(len(hid_values))
        l=(len(course_values)-len(hid_values))
        print(l)
        for i in range(0,l):
            hid_values.append('0')
      
        print(hid_values)
        
        # Now, you can zip the values
        dict_data = zip(course_values, university_values, year_values, hid_values)
        # res=list(dict_data) 
        # print(res)
      
        data=[{
            'course':course,
            'university':university,
            'year':year,
            'hid':hid,
        } for course,university,year,hid in dict_data]
        print(data)
        existing_education_ids = Education.objects.filter(reg_id=id).values_list('id', flat=True)
        print(existing_education_ids)
        difference = [x for x in existing_education_ids if x not in [int(y) for y in temp]]
        print(difference)
        for i in difference:
        # differene is a list so i want all item in the list to iterate to delete each item

           deldata=Education.objects.get(id=i)
           print(deldata)
           deldata.delete()
        for j in data:
            course = j.get('course')
            university = j.get('university')
            year = j.get('year')
            hid = j.get('hid')
            # print(course)
            # print(university)
            # print(year)
            # print(hid)
            if hid=='0':
                print(hid)
                candidate_instance = Candidate.objects.get(id=id)
                data1=Education(reg_id=candidate_instance,course=course,university=university,year=year)
                data1.save()
            else:
                UpDAta=Education.objects.get(id=hid)
                UpDAta.course=course
                UpDAta.university=university
                UpDAta.year=year
                UpDAta.save()
                # print(UpDAta.course)
        print('success')
        success = True   
    # return render(request,'edit.html',{'success': success})
    
    return HttpResponse("ok", status=200)


