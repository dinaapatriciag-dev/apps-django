from django.shortcuts import render

obras = [
    {
        "id": 1,
        "titulo": "Interestelar",
        "tipo": "Filme",
        "ano": 2014,
        "genero": "Ficção científica",
        "descricao": "Um grupo de exploradores viaja através de um buraco de minhoca no espaço."
    },
    {
        "id": 2,
        "titulo": "Stranger Things",
        "tipo": "Série",
        "ano": 2016,
        "genero": "Suspense",
        "descricao": "Um grupo de amigos enfrenta acontecimentos sobrenaturais em sua cidade."
    },
]

def index(request):

    context = {
        "obras": obras,
    }

    return render(
        request,
        "catalogo/index.html",
        context
    )

def detalhes(request, id):
    obras_encontradas = None

    for obra in obras:
        if obra["id"] == id:
            obras_encontradas = obra
    context = {
        "obra": obras_encontradas,
    }
    return render(request, "catalogo/detalhes.html", context)