#### Fonctions secondaires
"""
Module pour générer et analyser la suite de Syracuse d'un nombre donné.

Fonctions principales :
- syracuse_l(n) : Génère la suite de Syracuse à partir du nombre n.
- temps_de_vol(l) : Calcule le temps de vol (nombre d'itérations jusqu'à 1).
- temps_de_vol_en_altitude(l) : Calcule le temps de vol en altitude (jusqu'à ce 
que la suite redescende sous le nombre de départ).
- altitude_maximale(l) : Retourne l'altitude maximale de la suite.
- syr_plot(lsyr) : Affiche un graphique de la suite de Syracuse.

Fonction principale :
- main() : Génère la suite pour n=15, affiche le graphique et imprime les propriétés 
(temps de vol, temps de vol en altitude, altitude maximale).
"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche un graphique interactif de la suite de Syracuse.

    Args:
    lsyr (list): Liste représentant la suite de Syracuse à afficher.

    Cette fonction utilise Plotly pour afficher un graphique avec 
    les valeurs de la suite sur l'axe des y et
    les indices des éléments de la suite sur l'axe des x.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    l = []
    l.append(n)
    while n != 1 :
        if n%2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici

    return len(l)-1

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    n = l[0]
    for i, elt in enumerate(l):
        if elt<n:
            return i-1
    return None


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici

    n=0
    for elt in l:
        n = max(n,elt)
    return n


#### Fonction principale


def main():
    """
    Fonction principale qui exécute le programme.

    Elle génère la suite de Syracuse pour le nombre de départ n = 15, puis :
    - Affiche un graphique interactif de la suite à l'aide de la fonction `syr_plot`.
    - Affiche le temps de vol (nombre d'itérations nécessaires pour atteindre 1) 
    via la fonction `temps_de_vol`.
    - Affiche le temps de vol en altitude (nombre d'itérations jusqu'à ce que la suite
     redescende sous le nombre de départ) via la fonction `temps_de_vol_en_altitude`.
    - Affiche l'altitude maximale atteinte dans la suite de Syracuse via la fonction
     `altitude_maximale`.

    Elle ne prend aucun argument et n'a pas de valeur de retour.
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
