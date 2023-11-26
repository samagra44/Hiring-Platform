from django.shortcuts import render, redirect
from hr.models import JobPost, CandidateApplication, SelectCandidateJob,Hr
from django.contrib.auth.decorators import login_required

@login_required
def hrHome_views(request):
    if Hr.objects.filter(user=request.user).exists():
        jobpost = JobPost.objects.filter(user=request.user)
        return render(request,'hr/hrdashbordh.html',{'jobpost':jobpost})
    else:
        return redirect('candidate_dashbordh')

@login_required
def post_job_views(request):
    msg = None
    if request.method == "POST":
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date = request.POST.get('last-date')
        job_post = JobPost(user=request.user,title=job_title,address=address,companyName=company_name,salaryLow=salary_low,salaryHigh=salary_high,lastToApply=last_date)
        job_post.save()
    return render(request, 'hr/postjob.html',{"msg":"Job Added Successfully !!"})

@login_required
def candidate_view(request,pk):
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        applications = CandidateApplication.objects.filter(job=job)
        selectedapplications = SelectCandidateJob.objects.filter(job=job)
        return render(request, 'hr/candidate.html',{'applications':applications,'selectedapplications':selectedapplications,'job':job})
    return redirect('hr_dash')

@login_required
def selectCandidate(request):
    if request.method == "POST":
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid')
        job = JobPost.objects.get(id=jobpostid)
        candidate = CandidateApplication.objects.get(id=candidateid)
        SelectCandidateJob(job=job, candidate=candidate).save()
    return redirect('hr_dash')

@login_required
def deleteCandidate(request):
    if request.method == "POST":
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid')
        job = JobPost.objects.get(id=jobpostid)
        CandidateApplication.objects.get(id=candidateid).delete()
        job.applycount = job.applycount - 1
    return redirect('hr_dash')
