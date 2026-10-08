from django.shortcuts import render

def inicio(request):
    generos = [
        {
            "nombre": "Crimen y Suspenso",
            "descripcion": "Misterios insondables, mentes criminales y escapes al límite.",
            "peliculas": [
                {"nombre": "El Silencio de los Inocentes", "año": 1991, "imagen": "silencio.jpg"},
                {"nombre": "Zodiaco", "año": 2007, "imagen": "zodiaco.jpg"},
                {"nombre": "Se7en", "año": 1995, "imagen": "seven.jpg"},
                {"nombre": "Prisoners", "año": 2013, "imagen": "prisoners.jpg"},
                {"nombre": "Perdida", "año": 2014, "imagen": "perdida.jpg"},
                {"nombre": "El Origen", "año": 2010, "imagen": "origen.jpg"},
                {"nombre": "La Isla Siniestra", "año": 2010, "imagen": "isla.jpg"},
                {"nombre": "El Club de la Pelea", "año": 1999, "imagen": "club.jpg"},
                {"nombre": "Los Infiltrados", "año": 2006, "imagen": "infiltrados.jpg"},
                {"nombre": "Fuego contra Fuego", "año": 1995, "imagen": "fuego.jpg"}
            ]
        },
        {
            "nombre": "Acción y Ciencia Ficción",
            "descripcion": "Adrenalina pura, demonios, tecnología avanzada y futuros distópicos.",
            "peliculas": [
                {"nombre": "Doom: La Puerta del Infierno", "año": 2005, "imagen": "doom.jpg"},
                {"nombre": "Matrix", "año": 1999, "imagen": "matrix.jpg"},
                {"nombre": "Terminator 2", "año": 1991, "imagen": "terminator2.jpg"},
                {"nombre": "Mad Max: Furia en el Camino", "año": 2015, "imagen": "madmax.jpg"},
                {"nombre": "Alien", "año": 1979, "imagen": "alien.jpg"},
                {"nombre": "Blade Runner 2049", "año": 2017, "imagen": "bladerunner.jpg"},
                {"nombre": "John Wick", "año": 2014, "imagen": "johnwick.jpg"},
                {"nombre": "Al Filo del Mañana", "año": 2014, "imagen": "alfilo.jpg"},
                {"nombre": "RoboCop", "año": 1987, "imagen": "robocop.jpg"},
                {"nombre": "Dredd", "año": 2012, "imagen": "dredd.jpg"}
            ]
        }
    ]

    context = {
        'lista_generos': generos
    }

    return render(request, 'home_agustin/inicio.html', context)