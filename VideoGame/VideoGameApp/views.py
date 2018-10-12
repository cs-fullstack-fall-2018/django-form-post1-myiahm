from django.shortcuts import render, get_object_or_404, redirect
from .forms import GameForm
from .models import VideoGame


def index(request):
    game = VideoGame.objects.all()
    context = {'game': game}
    return render(request, 'VideoGameApp/index.html', context)


def details(request, pk):
    post = get_object_or_404(VideoGame, pk=pk)
    return render(request, 'VideoGameApp/details.html', {'post': post})


def new_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = GameForm()
    return render(request, 'VideoGameApp/edit.html', {'form': form})

def edit_game(request, pk):
    post = get_object_or_404(VideoGame, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = GameForm(instance=post)
    return render(request, 'VideoGameApp/edit.html', {'form': form})
