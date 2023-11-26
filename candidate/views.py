from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost, CandidateApplication, Hr
from candidate.models import MyApplyJobList

@login_required
def candidate_dashbordh(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    jobs = JobPost.objects.all()
    return render(request, 'candidate/dashboradh.html',{'jobs':jobs})

@login_required
def myJobListViews(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    myjoblist = MyApplyJobList.objects.filter(user=request.user)
    return render(request, 'candidate/myjoblist.html',{'myjoblist':myjoblist})

@login_required
def applyforjob(request, pk):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hr_dash')
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        if CandidateApplication.objects.filter(user=request.user, job=job).exists():
            return redirect('candidate_dashbordh')
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            college = request.POST.get('college')
            passing_year = request.POST.get('passing_year')
            yearOfExperience = request.POST.get('yearOfExperience')
            resume = request.FILES.get('resume')
            candidate_application = CandidateApplication(user=request.user,job=job,passingYear=passing_year,yearsOfExperience=yearOfExperience,resume=resume)
            candidate_application.save()
            MyApplyJobList(user=request.user, job = candidate_application).save()
            job.applycount +=1
            job.save()
            return redirect('candidate_dashbordh')
        return render(request,'candidate/apply.html')
    return render(request, 'candidate/apply.html')

