from django.shortcuts import render
generos = [
        {
            "nombre": "Crimen y Suspenso",
            "descripcion": "Escapes imposibles, mentes maestras y misterios atrapantes.",
            "imagen_fondo": "suspenso.jpg",
            "peliculas": [
                {"nombre": "El Club de la Pelea", "año": 1999, "imagen": "club.jpg"},
                {"nombre": "Sueños de Fuga (The Shawshank Redemption)", "año": 1994, "imagen": "suenos_fuga.jpg"},
                {"nombre": "El Caballero de la Noche", "año": 2008, "imagen": "batman.jpg"},
                {"nombre": "Atrápame si puedes", "año": 2002, "imagen": "atrapame.jpg"},
                {"nombre": "Fuga de Alcatraz", "año": 1979, "imagen": "alcatraz.jpg"},
                {"nombre": "Guasón (Joker)", "año": 2019, "imagen": "joker.jpg"},
                {"nombre": "Plan de Escape", "año": 2013, "imagen": "plan_escape.jpg"},
                {"nombre": "Tiempos Violentos (Pulp Fiction)", "año": 1994, "imagen": "pulp.jpg"},
                {"nombre": "El Padrino", "año": 1972, "imagen": "padrino.jpg"},
                {"nombre": "El Silencio de los Inocentes", "año": 1991, "imagen": "silencio.jpg"}
            ]
        },
        {
            "nombre": "Acción y Ciencia Ficción",
            "descripcion": "Adrenalina pura, tecnología avanzada y futuros distópicos.",
            "imagen_fondo": "accion.jpg",
            "peliculas": [
                {"nombre": "Interestelar", "año": 2014, "imagen": "interestelar.jpg"},
                {"nombre": "Matrix", "año": 1999, "imagen": "matrix.jpg"},
                {"nombre": "Terminator 2", "año": 1991, "imagen": "terminator2.jpg"},
                {"nombre": "Mad Max: Furia en el Camino", "año": 2015, "imagen": "madmax.jpg"},
                {"nombre": "Alien", "año": 1979, "imagen": "alien.jpg"},
                {"nombre": "Blade Runner 2049", "año": 2017, "imagen": "bladerunner.jpg"},
                {"nombre": "John Wick", "año": 2014, "imagen": "johnwick.jpg"},
                {"nombre": "Al Filo del Mañana", "año": 2014, "imagen": "alfilo.jpg"},
                {"nombre": "RoboCop", "año": 1987, "imagen": "robocop.jpg"},
                {"nombre": "Duna", "año": 2021, "imagen": "duna.jpg"}
            ]
        }
    ]

def inicio(request):
    context = {
        'lista_generos': generos
    }

    return render(request, 'home_agustin/inicio.html', context)

def detalle_genero(request, nombre_genero):
    genero_seleccionado = None
    for g in generos:
        if g['nombre'] == nombre_genero:
            genero_seleccionado = g
            break

    context = {
        'genero': genero_seleccionado,
        'lista_generos': generos
    }
    return render(request, 'home_agustin/detalle.html', context)