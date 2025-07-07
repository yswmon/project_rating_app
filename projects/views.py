from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Vote
from django.db.models import Avg
from django.http import HttpResponse


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def submit_vote(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        ip = get_client_ip(request)
        Vote.objects.create(project=project, score=score, ip_address=ip)
        return redirect('vote_result', pk=pk)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

def vote_result(request, pk):
    project = get_object_or_404(Project, pk=pk)
    votes = project.vote_set.all()
    total_votes = votes.count()
    avg_score = round(sum(v.score for v in votes) / total_votes, 2) if total_votes > 0 else 0

    context = {
        'project': project,
        'average_score': avg_score,
        'total_votes': total_votes,
    }
    return render(request, 'projects/vote_result.html', context)

def role_selection(request):
    return render(request, 'projects/role_selection.html')


# ✅ 완전히 새로 정리된 project_list
def project_list(request):
    sort = request.GET.get('sort', 'average')  # 기본 정렬: 평균 점수
    projects = Project.objects.annotate(average_score=Avg('vote__score'))

    if sort == 'title':
        projects = projects.order_by('title')
    else:  # 기본 or sort == 'average'
        projects = projects.order_by('-average_score')

    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'sort': sort,
    })
