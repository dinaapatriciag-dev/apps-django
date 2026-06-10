from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):

    nome = request.GET.get("nome")

    contexto = {
        "nome": nome
    }

    return render(
        request,
        "index.html",
        contexto
    )
def sobre(request):
    return render(request, "sobre.html")

def aluno(request, id_aluno):
    contexto = {
        "id_aluno": id_aluno
    }

    return render(request, "aluno.html", contexto)