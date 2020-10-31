from django.shortcuts import render


def index(request):
    receitas = {
        1:'Lasanha',
        2:'Sopa de Legumas',
        3:'Sorvete',
        4:'Bolo de Chocolate'
    }

    dados = {
        'nome_da_receitas' : receitas
    }


    return render(request,'index.html', dados)

def receita(request):
    return render(request,'receita.html')

