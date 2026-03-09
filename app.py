from flask import Flask, render_template

app = Flask(__name__)

NOTICIAS = [
    {
        "titulo": "Pogačar arrasa en la cima del Tourmalet y sentencia el Tour de Francia 2026",
        "extracto": (
            "El esloveno Tadej Pogačar (UAE Team Emirates) firmó una exhibición antológica "
            "en la decimocuarta etapa del Tour de Francia, atacando a 60 km de meta y llegando "
            "en solitario con más de cuatro minutos de ventaja sobre el segundo clasificado. "
            "La carrera parece ya sentenciada a falta de cinco etapas para París."
        ),
        "categoria": "Grand Tours",
        "autor": "Carlos Vega",
        "fecha": "9 mar 2026",
        "lectura": 4,
        "emoji": "🚴",
        "color": "linear-gradient(135deg,#922b21,#1a1a1a)",
    },
    {
        "titulo": "Van der Poel bate el récord de la hora con 56,1 km en el velódromo de Aguascalientes",
        "extracto": (
            "El neerlandés pulverizó la plusmarca mundial que él mismo estableció en 2024, "
            "completando 56,1 km en 60 minutos en la pista más rápida del mundo."
        ),
        "categoria": "Pista",
        "autor": "Laura Méndez",
        "fecha": "8 mar 2026",
        "lectura": 3,
        "emoji": "⚡",
        "color": "linear-gradient(135deg,#1a5276,#1a1a1a)",
    },
    {
        "titulo": "Vingegaard confirma su vuelta al máximo nivel con la victoria en la Tirreno-Adriático",
        "extracto": (
            "El danés Jonas Vingegaard demostró que su recuperación es total al ganar la etapa "
            "reina con final en Terminillo y asegurarse la victoria final en la carrera italiana."
        ),
        "categoria": "Carreras por etapas",
        "autor": "Marta Ruiz",
        "fecha": "8 mar 2026",
        "lectura": 3,
        "emoji": "🏔️",
        "color": "linear-gradient(135deg,#1e8449,#1a1a1a)",
    },
    {
        "titulo": "Remco Evenepoel gana la Milán-San Remo en un sprint reducido a diez corredores",
        "extracto": (
            "El belga se impuso al sprint sobre Paris-Nice tras una etapa durísima marcada "
            "por el viento de cara que desintegró el pelotón antes de La Cipressa."
        ),
        "categoria": "Clásicas",
        "autor": "Sergio Palomo",
        "fecha": "7 mar 2026",
        "lectura": 4,
        "emoji": "🌹",
        "color": "linear-gradient(135deg,#7d6608,#1a1a1a)",
    },
    {
        "titulo": "El equipo Visma-Lease a Bike invertirá 120 millones en el presupuesto de 2027",
        "extracto": (
            "La escuadra neerlandesa anunció un acuerdo histórico que la convertirá en el "
            "equipo con mayor presupuesto del pelotón internacional a partir de la próxima temporada."
        ),
        "categoria": "Equipos",
        "autor": "Ana Torres",
        "fecha": "6 mar 2026",
        "lectura": 2,
        "emoji": "💰",
        "color": "linear-gradient(135deg,#4a235a,#1a1a1a)",
    },
    {
        "titulo": "Nemo Delacroix gana el Campeonato del Mundo de MTB Cross-Country en Andorra",
        "extracto": (
            "El francés sorprendió al mundo del mountain bike con una remontada espectacular "
            "en los últimos 500 metros del circuito andorrano."
        ),
        "categoria": "MTB",
        "autor": "Pedro Iglesias",
        "fecha": "5 mar 2026",
        "lectura": 3,
        "emoji": "🌲",
        "color": "linear-gradient(135deg,#1a5c1a,#1a1a1a)",
    },
]

RANKING = [
    {"nombre": "T. Pogačar",   "bandera": "🇸🇮", "puntos": "4820"},
    {"nombre": "J. Vingegaard","bandera": "🇩🇰", "puntos": "4105"},
    {"nombre": "R. Evenepoel", "bandera": "🇧🇪", "puntos": "3870"},
    {"nombre": "M. van der Poel","bandera": "🇳🇱","puntos": "3640"},
    {"nombre": "P. Roglič",    "bandera": "🇸🇮", "puntos": "3510"},
    {"nombre": "C. Rodríguez", "bandera": "🇪🇸", "puntos": "2990"},
    {"nombre": "A. Yates",     "bandera": "🇬🇧", "puntos": "2745"},
]

PROXIMAS_CARRERAS = [
    {"dia": "15", "mes": "Mar", "nombre": "Milán-San Remo",       "categoria": "Monument – WorldTour"},
    {"dia": "22", "mes": "Mar", "nombre": "E3 Saxo Classic",      "categoria": "WorldTour"},
    {"dia": "30", "mes": "Mar", "nombre": "Gante-Wevelgem",       "categoria": "WorldTour"},
    {"dia": "06", "mes": "Abr", "nombre": "París-Roubaix",        "categoria": "Monument – WorldTour"},
    {"dia": "20", "mes": "Abr", "nombre": "Lieja-Bastogne-Lieja", "categoria": "Monument – WorldTour"},
]

BREVES = [
    {"emoji": "🩺", "texto": "Carapaz se recupera bien de la fractura y no descarta el Giro",        "fecha": "9 mar 2026"},
    {"emoji": "📝", "texto": "Bernal renueva con INEOS Grenadiers hasta 2028",                       "fecha": "8 mar 2026"},
    {"emoji": "🌡️", "texto": "Altas temperaturas ponen en duda el recorrido de la Vuelta a Burgos",  "fecha": "7 mar 2026"},
    {"emoji": "🚀", "texto": "Nuevo fichaje bomba en el UAE: firma el joven Luca Bianchi",            "fecha": "6 mar 2026"},
    {"emoji": "🎙️", "texto": "Contador lanza su podcast semanal de análisis ciclista",               "fecha": "5 mar 2026"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        noticias=NOTICIAS,
        ranking=RANKING,
        proximas_carreras=PROXIMAS_CARRERAS,
        breves=BREVES,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

