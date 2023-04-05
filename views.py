from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recept(request, name):
    count = int(request.GET.get('servings', 1))

    context = {}
    context['recipe'] = {}

    if name in DATA:
        for item, value in DATA[name].items():
            context['recipe'][item] = float('{:.3f}'.format((value) * count))

    return render(request, 'application/recept.html', context)
