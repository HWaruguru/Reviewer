from django.shortcuts import render,redirect

def index(request):
    projects = [{"image":"lamb.jpeg","title": "github", "description": "an angular app", "link": "https://github.com/HWaruguru/Photo-Album/blob/main/photoalbum/templates/index.html","posted_by":"Hannah","date": "21/102021"}, {"image":"lamb.jpeg","title": "github", "description": "an angular app", "link": "https://github.com/HWaruguru/Photo-Album/blob/main/photoalbum/templates/index.html","posted_by":"Hannah","date": "21/102021"}, {"image":"lamb.jpeg","title": "github", "description": "an angular app", "link": "https://github.com/HWaruguru/Photo-Album/blob/main/photoalbum/templates/index.html","posted_by":"Hannah","date": "21/102021"}]
    return render(request, 'index.html', {"projects":projects})