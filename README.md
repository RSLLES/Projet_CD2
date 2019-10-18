# Projet_CD2
Projet de Maths du cours Calcul Différentiel II

## Amorce
Question : À quelle condition raisonnable portant sur $f(0, 0), f(0, 1)$ et le réel
$c$ est-on certain qu’il existe un $t \in [0, 1]$ tel que $f(0, t) = c$ ? Développer une
fonction qui renvoie un flottant éloigné d’au plus $eps$ d’un tel $t$ ou $None$ si la condition
évoquée ci-dessus n’est pas satisfaite.

Il suffit que la fonction qui a t associe f(0,t) soit continue sur [0,1] (ce qui est le cas car f est continûment différentiable), et que (f(0,0)-c)(f(0,1)-c) <= 0 pour appliquer le TVI.
Voir la fonction `find_seed(g, c=0, eps=2**(-26))`

