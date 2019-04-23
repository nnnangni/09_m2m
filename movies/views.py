from django.shortcuts import render,redirect
from .models import Movie,Score
from .forms import ScoreForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST


# Create your views here.
def list(request):
    movie = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies':movie})
    
def detail(request, id):
    movie = Movie.objects.get(id=id)
    form = ScoreForm()
    return render(request, 'movies/detail.html', {'movie':movie, 'form':form})
    
@login_required
def scores_new(request,id):
    movie=Movie.objects.get(id=id)
    if request.method=="POST":
        form=ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.movie=movie
            score.user=request.user
            score.save()
            return redirect('movies:detail', id)
            
@login_required
@require_POST
def score_delete(request, id, score_id):
    score=Score.objects.get(id=score_id)
    if request.user==score.user:
        score.delete()
    return redirect('movies:detail', id)