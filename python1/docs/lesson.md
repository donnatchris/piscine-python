# Python 1 — Leçon de synthèse

**École 42 · Piscine Python for Data Science · Array**

Cette leçon présente les connaissances nécessaires aux six exercices du
[sujet fourni, version 2.0](en.subject.pdf), dans la continuité de la
[leçon de Python 0](../../python0/docs/lesson.md). Elle décrit les concepts,
les bibliothèques et leurs principales fonctions ou classes.

Chaque chapitre donne les notions à étudier et les outils à comprendre pour
aborder un exercice. Les exemples courts illustrent une propriété générale
sur des données indépendantes du sujet. Les algorithmes, les implémentations
et les résultats des exercices restent à construire par l'apprenant.

## Sommaire

1. [Parcours et règles du projet](#1-parcours-et-règles-du-projet)
2. [Bibliothèques et environnement](#2-bibliothèques-et-environnement)
3. [Bases communes : les tableaux NumPy](#3-bases-communes--les-tableaux-numpy)
4. [Calcul numérique et validation — ex00](#4-calcul-numérique-et-validation--ex00)
5. [Structure 2D et slicing — ex01](#5-structure-2d-et-slicing--ex01)
6. [Fichiers image, Pillow et RGB — ex02](#6-fichiers-image-pillow-et-rgb--ex02)
7. [Recadrage et affichage — ex03](#7-recadrage-et-affichage--ex03)
8. [Axes et transposition — ex04](#8-axes-et-transposition--ex04)
9. [Couleurs, canaux et contraintes — ex05](#9-couleurs-canaux-et-contraintes--ex05)
10. [Erreurs, documentation et vérifications](#10-erreurs-documentation-et-vérifications)
11. [Révision et vocabulaire](#11-révision-et-vocabulaire)
12. [Documentation de référence](#12-documentation-de-référence)

## 1. Parcours et règles du projet

### Ce que chaque exercice mobilise

| Exercice | Fichiers à rendre | Concepts à étudier |
|---|---|---|
| `ex00` | `give_bmi.py` | Types numériques, opérations sur des tableaux, comparaisons et validation |
| `ex01` | `array2D.py` | Tableaux rectangulaires, axes, forme et slicing |
| `ex02` | `load_image.py` | Fichiers, décodage d'image, formats, modes et pixels |
| `ex03` | `load_image.py`, `zoom.py` | Coordonnées, recadrage, représentation monochrome et affichage |
| `ex04` | `load_image.py`, `rotate.py` | Transposition, organisation des axes et parcours de structures imbriquées |
| `ex05` | `load_image.py`, `pimp_image.py` | Canaux RGB, types de pixels, transformations et effets de bord |

NumPy, Pillow et Matplotlib forment un choix cohérent pour ce module. Le sujet
permet aussi d'autres bibliothèques dans les limites précisées par exercice.
Les outils présentés ici sont une sélection pédagogique, pas une obligation
d'utiliser chaque fonction citée.

### Règles communes

Le sujet demande Python **3.10 ou supérieur**, des imports explicites et
l'absence de variables globales. Les imports avec `*` sont interdits.
Il demande également :

- Une logique placée dans des fonctions et un `main()` pour les programmes.
- Une garde `if __name__ == "__main__":` pour lancer ce point d'entrée.
- Une docstring pour toutes les fonctions.
- Une gestion des erreurs évitant les exceptions non interceptées.
- Un code respectant les règles contrôlées avec Flake8.

Importer un module ne doit pas lancer sa démonstration, charger un fichier
ou ouvrir une fenêtre. Les imports et les définitions de fonctions restent
au niveau du module ; les traitements se placent dans les fonctions.

### Restrictions particulières

| Exercice | Point du sujet à retenir |
|---|---|
| `ex00`, `ex01` | NumPy ou une bibliothèque de manipulation de tableaux est autorisée |
| `ex01` | Le slicing est imposé |
| `ex02` | Les formats JPG et JPEG doivent au minimum être pris en charge |
| `ex03` | L'affichage doit comporter une échelle sur les axes X et Y |
| `ex04` | La transposition doit être réalisée sans fonction de bibliothèque pour cette opération |
| `ex05` | La forme de l'image doit être conservée et les opérateurs sont restreints par filtre |

Le sujet reste la référence pour les signatures, les noms de fichiers et les
sorties demandées. Distinguer ses exigences des choix de conception, comme
une politique sur les entrées vides ou sur la modification des arguments.

## 2. Bibliothèques et environnement

### Les rôles des trois bibliothèques

| Bibliothèque | Nom à installer | Import courant | Rôle |
|---|---|---|---|
| NumPy | `numpy` | `import numpy as np` | Stockage et calcul sur des tableaux numériques |
| Pillow | `Pillow` | `from PIL import Image` | Lecture des fichiers image et gestion des modes de couleur |
| Matplotlib | `matplotlib` | `import matplotlib.pyplot as plt` | Représentation graphique de tableaux avec des axes |

Pillow conserve le nom historique `PIL` pour ses imports. `np` et `plt` sont
seulement des alias conventionnels. Ces paquets sont externes à la bibliothèque
standard de Python.

### Installer dans un environnement isolé

Depuis la racine `python_data_science/`, avec `venv` et `pip` disponibles :

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install numpy Pillow matplotlib flake8
```

Un environnement virtuel isole les dépendances du projet. `python -m pip`
utilise le même interpréteur que `python`. La commande `deactivate` permet
de quitter l'environnement.

Pour identifier les versions utilisées :

```bash
python -c "import numpy, PIL, matplotlib; print(numpy.__version__, PIL.__version__, matplotlib.__version__)"
```

### Lire une fiche d'API

Une **classe** définit un type d'objet, comme `numpy.ndarray`. Une **fonction**
est appelée dans un module, comme `np.array(...)`. Une **méthode** est appelée
sur un objet, comme `data.copy()`. Un **attribut** expose une propriété,
comme `data.shape`, sans parenthèses.

Pour chaque outil, identifier ses paramètres, son résultat et ses effets :
modifie-t-il l'objet reçu ? Crée-t-il une copie ? Lit-il un fichier ? Prépare-t-il
un affichage ? Ces questions comptent autant que le nom de la fonction.

## 3. Bases communes : les tableaux NumPy

### La classe `numpy.ndarray`

Une liste Python stocke des références vers des objets éventuellement de types
différents. Un `ndarray` possède des axes, une forme et un type de stockage
commun à ses éléments, appelé `dtype`.

| Outil | Nature | Ce qu'il faut comprendre |
|---|---|---|
| `np.ndarray` | Classe | Représentation multidimensionnelle des données |
| `np.array(data, dtype=...)` | Fonction | Création d'un tableau à partir de données |
| `data.ndim` | Attribut | Nombre d'axes |
| `data.shape` | Attribut | Tuple des longueurs des axes |
| `data.size` | Attribut | Nombre total d'éléments |
| `data.dtype` | Attribut | Type de stockage des éléments |
| `data.astype(dtype)` | Méthode | Conversion du type des éléments |
| `data.tolist()` | Méthode | Conversion en objets et listes Python |
| `data.copy()` | Méthode | Copie des données du tableau |

Exemple de lecture des métadonnées d'un tableau :

```python
import numpy as np

readings = np.array([[4, 7, 9], [3, 8, 6]], dtype=float)
print(readings.ndim)   # 2.
print(readings.shape)  # (2, 3).
print(readings.size)   # 6.
```

`ndim`, `shape` et `size` répondent à trois questions différentes : combien
d'axes, quelle longueur pour chacun, et combien de valeurs au total ?
Un tableau de forme `(3,)` et un tableau de forme `(1, 3)` ont autant de
valeurs, mais pas le même nombre d'axes.

### Vectorisation

La **vectorisation** consiste à exprimer un calcul sur un tableau entier
plutôt qu'à écrire une boucle Python sur chaque valeur. Les opérateurs
arithmétiques usuels travaillent alors élément par élément.

```python
samples = [3, 5, 8]
measurements = np.array(samples)

print(samples * 3)       # Répète la liste.
print(measurements * 3)  # Multiplie les valeurs.
```

Les symboles n'ont donc pas toujours le même comportement selon le type des
objets. En Python, `**` représente une puissance ; `^` est un XOR binaire.
Les règles de priorité et les parenthèses restent importantes dans les calculs.

### Broadcasting

Le **broadcasting**, ou diffusion, rend certaines formes différentes compatibles
pour une opération. Un scalaire peut notamment être combiné avec un tableau.
NumPy compare les axes en partant de la droite : leurs longueurs doivent être
égales, ou l'une des deux doit valoir `1`. Un axe absent se comporte comme un
axe de longueur `1`.

Le broadcasting ne valide pas le sens des données. Une opération peut être
mathématiquement acceptée par NumPy alors que ses entrées ne respectent pas
le contrat d'une fonction. Il peut aussi produire un résultat plus grand
que prévu. Voir les [règles de diffusion](https://numpy.org/doc/stable/user/basics.broadcasting.html).

### Comparaisons et booléens

Une comparaison sur un tableau produit généralement un tableau de booléens.
Ce résultat peut servir de **masque**, c'est-à-dire de sélection logique.
Il faut distinguer une condition par valeur et une décision sur tout le tableau.

| Outil | Rôle |
|---|---|
| Opérateurs de comparaison | Comparer les valeurs correspondantes |
| `mask.all()` | Déterminer si toutes les valeurs du masque sont vraies |
| `mask.any()` | Déterminer si au moins une valeur du masque est vraie |
| `&`, `\|` avec parenthèses | Combiner des conditions élément par élément |

Les opérateurs Python `and` et `or` ne remplacent pas les opérations logiques
élément par élément sur des tableaux. De même, la valeur de vérité d'un tableau
à plusieurs éléments est ambiguë : une condition doit exprimer la décision
souhaitée explicitement.

### Indexation et slicing

Un **indice** désigne une position ; un **slice** décrit une tranche.
La syntaxe générale est `sequence[start:stop:step]`. Le début est inclus,
la fin est exclue et le pas vaut `1` par défaut. Les indices négatifs comptent
depuis la fin ; un pas nul est interdit.

```python
labels = ["A", "B", "C", "D", "E", "F"]
print(labels[2:5])  # ['C', 'D', 'E'].
print(labels[-1])   # 'F'.
print(labels[::2])  # ['A', 'C', 'E'].
```

Sur un tableau multidimensionnel, les sélections des différents axes peuvent
être séparées par des virgules dans les mêmes crochets. Un indice entier
retire l'axe sélectionné du résultat ; un slice le conserve.
Voir la [documentation sur l'indexation](https://numpy.org/doc/stable/user/basics.indexing.html).

### Vues, copies et effets de bord

Une affectation peut créer un autre nom pour le même objet. Une **vue** NumPy
partage les données d'un tableau ; une **copie** possède ses propres données.
Le slicing NumPy de base produit une vue, alors qu'un slicing de liste crée
une nouvelle liste au premier niveau.

```python
source = np.array([5, 8, 12])
view = source[:2]
independent = source.copy()

view[0] = 99
print(source[0])       # 99 : les données sont partagées.
print(independent[0])  # 5 : la copie est indépendante.
```

Modifier un argument reçu par une fonction constitue un **effet de bord**.
Il faut pouvoir reconnaître et expliquer ce comportement lorsqu'un objet
est réutilisé. Pour les tableaux numériques du module, `.copy()` duplique
les valeurs ; avec des tableaux d'objets, les références internes demanderaient
une attention supplémentaire. Voir les
[copies et vues](https://numpy.org/doc/stable/user/basics.copies.html).

### Types numériques et conversion

| Type | Propriété à retenir |
|---|---|
| `int` Python | Entier de précision arbitraire, dans les limites de mémoire |
| `float` Python | Nombre flottant à précision limitée |
| `np.uint8` | Entier non signé sur huit bits, entre 0 et 255 |
| Types entiers NumPy | Capacité limitée par leur taille de stockage |
| Types flottants NumPy | Précision et capacité dépendant du type |

Un calcul sur des entiers de capacité limitée peut dépasser l'intervalle
représentable. Une conversion de type peut aussi perdre de la précision.
Il faut comprendre l'échelle et le type des données avant d'effectuer un calcul.

La conversion n'est pas une validation : une chaîne peut être convertible en
nombre sans être un argument numérique conforme au contrat. Une collection
hétérogène peut également être convertie vers un type commun inattendu.
Voir les [types numériques NumPy](https://numpy.org/doc/stable/user/basics.types.html).

## 4. Calcul numérique et validation — ex00

### Concepts à connaître

L'exercice mobilise des fonctions recevant des listes numériques et des
calculs portant sur des valeurs correspondantes. Il faut comprendre le lien
entre un calcul scalaire et son expression sur un tableau, ainsi que la
production de résultats booléens.

| Notion | Ce qu'il faut étudier |
|---|---|
| Annotations de type | Sens de `list[int \| float]` et de `list[bool]` |
| Typage dynamique | Une annotation ne contrôle pas les valeurs à l'exécution |
| Correspondance des données | Rôle de l'ordre et de la longueur des collections |
| Arithmétique | Division, puissance, priorité et précision flottante |
| Comparaisons | Différence entre relation stricte et relation inclusive |
| Domaine d'un calcul | Valeurs pour lesquelles l'opération a un sens |
| Conversion du retour | Différence entre liste Python et tableau NumPy |

### Fonctions et méthodes utiles

| Outil | Usage général à comprendre |
|---|---|
| `len()` | Mesurer la longueur d'une collection |
| `type()` | Identifier le type exact d'un objet |
| `isinstance()` | Tester l'appartenance à un type, sous-classes comprises |
| `all()`, `any()` | Résumer des conditions sur un itérable Python |
| `np.array()` | Représenter des données sous forme de tableau |
| `np.isfinite()` | Repérer les valeurs finies, par opposition à NaN et aux infinis |
| `ndarray.tolist()` | Revenir à une représentation Python |

Les booléens sont des sous-classes des entiers en Python. Il faut connaître
cette particularité pour interpréter un contrôle de type. Les valeurs NaN
et les infinis sont des flottants, mais ne se comportent pas comme des
mesures ordinaires.

Une opération NumPy invalide peut émettre un avertissement et produire une
valeur spéciale plutôt que lever une exception Python. Validation et gestion
d'exceptions sont donc deux notions complémentaires.

### Questions pour vérifier sa compréhension

- Quelle différence y a-t-il entre type annoncé et type vérifié ?
- Le broadcasting garantit-il que deux collections décrivent les mêmes données ?
- Pourquoi la conversion en nombres ne suffit-elle pas à valider une entrée ?
- Quel effet le choix d'une comparaison a-t-il sur une valeur située à la frontière ?
- Comment distinguer une erreur de contrat d'un problème de précision numérique ?

## 5. Structure 2D et slicing — ex01

### Tableaux rectangulaires

Une structure 2D rectangulaire possède des lignes de même longueur. Une liste
de listes peut être irrégulière ; sa syntaxe seule ne garantit ni la présence
de deux axes, ni la régularité de ses lignes.

La profondeur d'imbrication et la longueur des lignes sont deux propriétés
différentes. Un tableau contenant des sous-tableaux supplémentaires peut
avoir plus de deux dimensions. Un tableau d'objets ne transforme pas une
structure irrégulière en matrice numérique rectangulaire.

### Sélection et forme

Le slicing peut sélectionner une partie d'un axe tout en conservant les autres.
La sélection d'un seul élément et celle d'une tranche d'un élément ne produisent
pas nécessairement la même forme.

Les bornes d'un slice sont ajustées à la longueur de la séquence. Un indice
simple hors limites provoque en revanche une `IndexError`. Une sélection
peut être vide tout en conservant des informations sur ses autres axes.

La conversion vers une liste ne préserve pas toujours ces informations :
une liste vide ne suffit pas à décrire le nombre de colonnes d'un tableau
sans ligne. La forme doit donc être comprise comme une propriété du tableau.

### Outils à connaître

| Outil | Rôle dans l'étude de la structure |
|---|---|
| `list` | Représentation Python des collections et sous-collections |
| `len()` | Longueur d'une collection ou d'une ligne |
| `np.array()` | Construction d'un tableau à partir de données régulières |
| `ndarray.ndim` | Nombre d'axes réellement obtenus |
| `ndarray.shape` | Longueurs des axes |
| Syntaxe `start:stop:step` | Sélection d'une tranche |
| `ndarray.tolist()` | Conversion vers des listes Python |

Le sujet impose le slicing. Comprendre cette syntaxe est donc nécessaire,
même si d'autres outils savent sélectionner des données.

### Questions pour vérifier sa compréhension

- Une liste de listes est-elle toujours un tableau 2D rectangulaire ?
- Quelle différence y a-t-il entre dimension, nombre de lignes et nombre de valeurs ?
- Comment une borne négative est-elle interprétée ?
- Quelles informations une conversion en liste peut-elle faire perdre ?
- Comment expliquer la forme d'une sélection vide ?

## 6. Fichiers image, Pillow et RGB — ex02

### Distinguer fichier, format, mode et pixels

| Notion | Sens |
|---|---|
| Chemin | Emplacement du fichier dans le système de fichiers |
| Format de fichier | Encodage des données, par exemple JPEG ou PNG |
| Mode de couleur | Organisation des composantes d'un pixel |
| Taille de l'image | Largeur et hauteur en pixels |
| Tableau de pixels | Valeurs numériques issues du décodage |

Les extensions `.jpg` et `.jpeg` désignent couramment le format JPEG.
L'extension ne garantit pas que le fichier soit une image valide. Le décodage
interprète son contenu ; un fichier existant peut encore être illisible.

Un chemin relatif dépend du **répertoire de travail courant**. Il n'est pas
automatiquement interprété depuis le dossier du programme Python.

### Les principales API de Pillow

L'import `from PIL import Image` donne accès au module `Image`. Les objets
image sont des instances de la classe `Image.Image` ou de classes dérivées.

| Outil | Nature | Rôle |
|---|---|---|
| `Image.open(path)` | Fonction | Ouvrir et identifier un fichier image |
| `Image.Image` | Classe | Représenter une image avec ses pixels et propriétés |
| `image.format` | Attribut | Format reconnu lors de l'ouverture |
| `image.mode` | Attribut | Mode de couleur de l'image |
| `image.size` | Attribut | Couple `(largeur, hauteur)` |
| `image.convert(mode)` | Méthode | Produire une image dans un autre mode |
| `image.load()` | Méthode | Demander le chargement des données de pixels |
| `image.close()` | Méthode | Libérer les ressources de l'image |
| `UnidentifiedImageError` | Exception | Signaler un contenu non reconnu comme image |

`Image.open()` peut différer le décodage des pixels. L'identification du fichier
et la lecture de toutes ses données ne sont donc pas nécessairement simultanées.
Le gestionnaire de contexte `with` sert à gérer la durée de vie des ressources.

Les propriétés du fichier ouvert et celles d'une image issue d'une conversion
ne sont pas interchangeables : les métadonnées ne suivent pas toutes les
transformations. Voir la [référence de Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html).

### Modes de couleur et organisation des données

| Mode | Représentation usuelle |
|---|---|
| `RGB` | Trois composantes : rouge, vert et bleu |
| `RGBA` | RGB avec une composante alpha de transparence |
| `L` | Une intensité de gris sur huit bits |

Dans un tableau RGB d'image, les axes usuels sont la hauteur, la largeur,
puis les canaux. Les coordonnées horizontales désignent des colonnes et les
coordonnées verticales des lignes. L'ordre est donc différent de celui du
couple `image.size` fourni par Pillow.

Un **pixel** regroupe les composantes à une position. Un **canal** désigne
une composante sur l'ensemble de l'image. Le tableau ne contient pas directement
les octets compressés du fichier et ne conserve pas toutes ses métadonnées.

### Passage entre Pillow et NumPy

`np.array(image)` permet de représenter les pixels d'une image par un tableau.
L'objet Pillow et le tableau NumPy proposent des interfaces différentes :
le premier décrit une image et ses propriétés, le second expose des axes,
un type de stockage et des opérations numériques.

Une forme, un format de fichier et un mode de couleur donnent des informations
distinctes. De même, afficher un tableau avec `print()` et afficher une image
dans une fenêtre sont deux opérations différentes. Les points de suspension
d'un affichage NumPy peuvent simplement indiquer une représentation abrégée.

### Questions pour vérifier sa compréhension

- Pourquoi la présence d'une extension ne garantit-elle pas le chargement ?
- Quelle différence y a-t-il entre `format`, `mode`, `size` et `shape` ?
- Pourquoi la lecture des pixels peut-elle encore échouer après l'ouverture ?
- Quelles propriétés d'un fichier disparaissent quand on ne conserve que ses pixels ?
- Comment le répertoire de travail influence-t-il un chemin relatif ?

## 7. Recadrage et affichage — ex03

### Géométrie d'une image

Un **recadrage** sélectionne une zone de pixels existants. Un
**redimensionnement** calcule une image d'une nouvelle taille, généralement
avec interpolation. L'agrandissement visuel d'une zone ne crée pas à lui seul
de nouveaux détails dans les données.

Il faut relier les coordonnées X et Y aux axes du tableau et distinguer
les coordonnées de l'image d'origine de celles d'une zone affichée.
La taille d'une fenêtre graphique n'est pas non plus la forme du tableau.

### Représentation monochrome

Une image monochrome peut être stockée dans un tableau 2D ou dans un tableau
à trois axes dont un axe a une longueur de un. Ces représentations contiennent
une intensité par pixel, mais ne possèdent pas la même forme.

Un canal de couleur affiché en gris et une conversion combinant plusieurs
composantes ne représentent pas nécessairement la même intensité. Une colormap
modifie la correspondance entre valeurs et couleurs affichées ; elle ne
réécrit pas les valeurs du tableau.

### Classes et fonctions d'affichage

| Outil | Rôle |
|---|---|
| `matplotlib.figure.Figure` | Représenter la figure complète |
| `matplotlib.axes.Axes` | Représenter la zone de tracé, ses axes et annotations |
| `plt.subplots()` | Créer une figure et un ou plusieurs objets `Axes` |
| `ax.imshow(data, ...)` | Représenter un tableau sous forme d'image |
| `ax.set_title(text)` | Définir le titre du tracé |
| `ax.set_xlabel(text)` | Nommer l'axe horizontal |
| `ax.set_ylabel(text)` | Nommer l'axe vertical |
| `plt.show()` | Demander l'affichage des figures |
| `plt.close(fig)` | Fermer une figure et libérer ses ressources |

Le module `pyplot` expose aussi `plt.imshow()`. L'interface avec un objet
`Axes` rend explicite la zone de tracé que l'on configure.
Voir la [création de figures et d'axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html).

### Paramètres importants de `imshow()`

| Paramètre | Notion à comprendre |
|---|---|
| `cmap` | Palette associant des couleurs à des valeurs scalaires |
| `vmin`, `vmax` | Bornes utilisées pour la correspondance des valeurs scalaires |
| `origin` | Placement de l'origine en haut ou en bas |
| `interpolation` | Méthode de rendu lors de l'adaptation à la taille d'affichage |

Une image 2D fournit des valeurs scalaires à une palette. Une image RGB
fournit déjà des composantes de couleur : `cmap` ne lui applique pas une
conversion en gris. Les données RGB entières utilisent usuellement l'échelle
0 à 255 ; les données RGB flottantes doivent être dans l'intervalle 0 à 1.
Voir la [référence de `imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).

### Autres API utiles à étudier

| Outil | Rôle général |
|---|---|
| `ndarray.shape` | Connaître la géométrie des données |
| Indexation et slicing NumPy | Comprendre la sélection selon les axes |
| `ndarray.copy()` | Distinguer une sélection partagée d'une copie indépendante |
| `Image.fromarray(data)` | Construire une image Pillow depuis un tableau compatible |
| `image.convert(mode)` | Étudier les représentations de couleur disponibles |

### Questions pour vérifier sa compréhension

- Qu'est-ce qui change entre recadrage et redimensionnement ?
- Une image à un seul canal est-elle obligatoirement stockée dans un tableau 2D ?
- Quel lien y a-t-il entre les coordonnées du tracé et celles du tableau ?
- Une palette peut-elle changer l'interprétation visuelle de données identiques ?
- Quelle différence y a-t-il entre construire un résultat et l'afficher ?

## 8. Axes et transposition — ex04

### Définition de la transposition

La **transposition** échange le rôle des lignes et des colonnes d'une matrice.
Une forme `(hauteur, largeur)` devient `(largeur, hauteur)`. Sur une matrice
carrée, la forme reste identique bien que les positions des valeurs puissent
changer.

Géométriquement, cette opération correspond à une réflexion par rapport à la
diagonale principale. Une rotation et une transposition sont des transformations
différentes. Le nom `rotate.py` ne doit donc pas remplacer la lecture de
l'opération demandée par le sujet.

### Structures et parcours à comprendre

| Notion ou outil Python | Ce qu'il faut savoir expliquer |
|---|---|
| Listes imbriquées | Différence entre une ligne et un élément |
| `len()` | Longueur d'une structure |
| `range()` | Parcours d'indices |
| Boucles imbriquées | Parcours de plusieurs axes |
| `list.append()` | Construction progressive d'une collection |
| Alias et mutabilité | Risque de partager involontairement des sous-listes |

Ces notions permettent de raisonner sur une transformation de structure.
Le choix des parcours et la construction de l'algorithme font partie du travail
de l'exercice.

### API à connaître et restriction du sujet

NumPy propose `.T`, `np.transpose()` et `swapaxes()` pour modifier l'ordre des
axes. Elles peuvent être étudiées dans la documentation afin de comprendre
le vocabulaire, mais **ne doivent pas réaliser la transposition d'ex04**.
Le sujet impose de construire cette opération soi-même.

Les outils de chargement, de représentation des données et d'affichage restent
utilisables dans le cadre des autorisations du sujet. Connaître une API ne
signifie pas qu'elle soit autorisée pour toutes les opérations du projet.

### Questions pour vérifier sa compréhension

- Que signifie « échanger le rôle des lignes et des colonnes » ?
- Pourquoi une forme carrée peut-elle cacher une transformation des positions ?
- Dans une image à plusieurs canaux, quels axes décrivent l'espace ?
- Pourquoi transposition et rotation ne doivent-elles pas être confondues ?
- Quel problème une sous-liste partagée peut-elle poser dans une nouvelle structure ?

## 9. Couleurs, canaux et contraintes — ex05

### Concepts de couleur

La représentation RGB décrit une couleur par trois intensités. Une image en
niveaux de gris décrit une intensité sans teinte ; elle peut avoir plusieurs
représentations de stockage. Le nombre de composantes et la forme sont donc
des propriétés à distinguer de l'apparence visuelle.

Une transformation de couleur peut changer les valeurs sans changer la forme.
À l'inverse, sélectionner un canal peut changer le nombre d'axes du tableau.
Il faut comprendre ces effets avant de choisir une représentation du résultat.

### Propriétés à étudier

| Notion | Question technique associée |
|---|---|
| Canaux RGB | Quelle composante décrit quelle information ? |
| Intensité et échelle | Que représente une valeur dans le type choisi ? |
| Transformations de couleur | Quels aspects de la couleur sont modifiés ? |
| Représentation du gris | Quel lien y a-t-il entre intensité, teinte et canaux ? |
| Conservation de forme | Comment distinguer changement de valeurs et changement de structure ? |
| Effets de bord | Une modification est-elle visible par d'autres utilisateurs du tableau ? |
| Réutilisation des données | Que se passe-t-il lorsque plusieurs fonctions reçoivent la même source ? |

### Fonctions, méthodes et syntaxe utiles

| Outil | Rôle général à connaître |
|---|---|
| `np.ndarray` | Structure contenant les valeurs de couleur |
| `ndarray.shape`, `ndarray.ndim` | Description des axes |
| `ndarray.dtype` | Type de stockage des intensités |
| Indexation et slicing | Accès aux données selon les axes |
| Affectation NumPy | Modification des valeurs sélectionnées |
| `ndarray.copy()` | Construction d'un tableau indépendant |
| Opérateurs arithmétiques | Calculs élément par élément selon les autorisations |
| `Axes.imshow()`, `plt.show()` | Représentation et affichage du résultat |

La validation du type, du nombre d'axes, du nombre de canaux et de l'échelle
fait partie du raisonnement sur une transformation. Une image RGB, RGBA et une
image monochrome ne présentent pas la même structure.

### Restrictions à connaître

Le sujet fixe les ensembles suivants ; il n'impose pas de tous les employer :

| Fonction demandée | Opérateurs autorisés |
|---|---|
| `ft_invert` | `=`, `+`, `-`, `*` |
| `ft_red` | `=`, `*` |
| `ft_green` | `=`, `-` |
| `ft_blue` | `=` |
| `ft_grey` | `=`, `/` |

Une méthode de bibliothèque peut réaliser un calcul complexe même si son appel
semble simple. Il faut comprendre son comportement pour déterminer si elle
respecte les restrictions. Une conversion disponible dans Pillow n'est donc
pas automatiquement utilisable comme calcul d'un filtre.

L'affichage des images transformées, les docstrings et la conservation de la
forme restent des exigences distinctes du calcul des couleurs.

### Questions pour vérifier sa compréhension

- Quelle différence y a-t-il entre modifier les valeurs d'un canal et retirer un axe ?
- Pourquoi l'échelle des intensités intervient-elle dans un calcul de couleur ?
- La même apparence peut-elle être obtenue avec des formes de tableaux différentes ?
- Quels effets un tableau partagé peut-il avoir lors d'appels successifs ?
- Comment vérifier les opérateurs réellement employés par une fonction auxiliaire ?

## 10. Erreurs, documentation et vérifications

### Contrat d'une fonction

Un **contrat** décrit les entrées admises, le résultat et les effets observables.
Il comprend notamment les types, les structures, la modification éventuelle
des arguments, les affichages et la façon de signaler un échec.

Une fonction qui retourne une valeur et une fonction qui l'affiche ont des
contrats différents. `print()` et `plt.show()` ne remplacent pas `return`.
Les annotations expriment des intentions ; elles n'imposent pas le contrat
à l'exécution.

### Validation et exceptions

La validation porte sur les préconditions d'une opération. Une exception
signale une situation qui empêche son exécution normale. L'interception
permet au programme de gérer cet échec.

| Outil ou exception | Notion à retenir |
|---|---|
| `raise` | Signaler une erreur par une exception |
| `try` / `except` | Intercepter les erreurs des types indiqués |
| `TypeError` | Type d'argument incompatible |
| `ValueError` | Valeur ou structure incompatible avec l'opération |
| `IndexError` | Position absente dans une séquence ou un axe |
| `OSError` | Famille d'erreurs liées notamment aux fichiers |
| `FileNotFoundError` | Fichier absent ; sous-classe de `OSError` |
| `PermissionError` | Accès refusé ; sous-classe de `OSError` |
| `UnidentifiedImageError` | Image non reconnue par Pillow |
| `AssertionError` | Assertion non satisfaite |

Les assertions peuvent être désactivées avec `python -O`. Elles ne remplacent
pas automatiquement une validation qui doit toujours s'exécuter. Une exception
interceptée très largement peut aussi masquer un défaut de programmation.

Un contrat d'échec doit être cohérent entre la fonction et son appelant.
Le sujet exige que les erreurs soient traitées sans exception non interceptée.

### Documentation et style

Une **docstring** est une chaîne placée en première instruction d'une fonction.
Elle documente son rôle et ses propriétés utiles à l'appelant. Elle est accessible
avec `help()` et `__doc__`.

Flake8 analyse le style et certaines erreurs probables sans exécuter le programme.
Il ne prouve ni la correction d'un calcul, ni la qualité de l'affichage, ni le
respect de toutes les restrictions particulières.

Depuis la racine du dépôt, avec Flake8 installé :

```bash
python -m flake8 python1
```

### Outils de vérification à comprendre

| Outil | Rôle |
|---|---|
| `type()`, `isinstance()` | Examiner les types |
| `ndarray.shape`, `ndarray.dtype` | Examiner structure et stockage |
| `np.array_equal(a, b)` | Comparer exactement formes et valeurs |
| `np.allclose(a, b)` | Comparer des valeurs numériques avec des tolérances |
| Observation des figures | Contrôler rendu, axes et interprétation des couleurs |

`np.allclose()` peut appliquer le broadcasting : une proximité numérique
ne garantit donc pas à elle seule l'identité des formes. Il faut savoir
quelle propriété une vérification mesure.

Des exemples du sujet, des entrées limites et des entrées invalides servent
à explorer des comportements différents. L'apprenant choisit ses cas et
construit ses résultats de référence à partir du contrat.

## 11. Révision et vocabulaire

### Les distinctions à savoir expliquer

| Notions | Différence essentielle |
|---|---|
| Liste / `ndarray` | Collection Python / tableau avec forme et type de stockage |
| `ndim` / `shape` / `size` | Nombre d'axes / longueurs des axes / nombre de valeurs |
| Classe / fonction / méthode / attribut | Type d'objet / appel de module / appel sur un objet / propriété |
| Vectorisation / broadcasting | Expression d'un calcul sur des tableaux / compatibilité de formes |
| Validation / conversion | Contrôle du contrat / changement de représentation |
| Vue / copie | Données partagées / données indépendantes |
| Format / mode | Encodage du fichier / organisation des composantes |
| Taille Pillow / forme NumPy | Largeur puis hauteur / axes du tableau |
| Pixel / canal | Composantes à une position / composante sur l'image |
| Recadrage / redimensionnement | Sélection d'une zone / calcul d'une nouvelle taille |
| Données / rendu | Valeurs stockées / représentation affichée |
| Transposition / rotation | Échange des rôles des axes / transformation par rotation |
| Affichage / retour | Effet observable / valeur transmise à l'appelant |

### Questions de révision transversales

1. Comment reconnaître qu'une API est une classe, une méthode ou un attribut ?
2. Pourquoi une conversion réussie ne prouve-t-elle pas la validité d'une entrée ?
3. Quelles propriétés faut-il lire pour comprendre un tableau inconnu ?
4. Quand un calcul NumPy peut-il être accepté malgré un contrat de données incorrect ?
5. Comment une vue explique-t-elle une modification inattendue de la source ?
6. Que faut-il connaître d'un type numérique avant d'effectuer un calcul ?
7. Pourquoi la forme d'un tableau ne suffit-elle pas à définir son interprétation ?
8. Quels éléments dépendent du fichier, des pixels et de l'affichage ?
9. Pourquoi les restrictions d'un exercice restent-elles importantes lorsqu'une
   bibliothèque propose déjà une fonction adaptée ?
10. Quelles propriétés une vérification numérique ne permet-elle pas d'observer ?

### Glossaire bref

| Terme | Sens dans le module |
|---|---|
| Array / tableau | Données indexées selon un ou plusieurs axes |
| Axis / axe | Dimension selon laquelle les positions sont organisées |
| Shape / forme | Tuple des longueurs des axes |
| `dtype` | Type de stockage des éléments |
| Scalaire | Valeur unique |
| Vectorisation | Expression d'un calcul sur des tableaux |
| Broadcasting / diffusion | Compatibilité entre certaines formes différentes |
| Masque | Tableau booléen utilisé pour une sélection logique |
| Slice / tranche | Sélection définie par début, fin exclue et pas |
| Vue | Objet partageant les données d'un tableau |
| Copie | Objet possédant des données indépendantes |
| Effet de bord | Modification observable au-delà de la valeur retournée |
| Pixel | Élément d'image situé à une ligne et une colonne |
| Canal | Composante des pixels, comme le rouge |
| RGB | Organisation rouge, vert, bleu |
| Alpha | Composante représentant la transparence |
| Monochrome | Représentation par intensités sans teinte |
| Colormap / palette | Correspondance entre valeurs scalaires et couleurs |
| Interpolation | Méthode de calcul ou de rendu entre des positions |
| Contrat | Entrées, résultat et effets annoncés d'une fonction |
| API | Interface proposée par un module, une bibliothèque ou un objet |

## 12. Documentation de référence

Le [sujet local](en.subject.pdf) définit les fichiers, signatures et restrictions.
Pour approfondir les concepts et les interfaces :

- [Premiers pas avec NumPy](https://numpy.org/doc/stable/user/quickstart.html) : tableaux, axes et opérations.
- [Indexation NumPy](https://numpy.org/doc/stable/user/basics.indexing.html) : indices et slices.
- [Broadcasting NumPy](https://numpy.org/doc/stable/user/basics.broadcasting.html) : compatibilité des formes.
- [Copies et vues NumPy](https://numpy.org/doc/stable/user/basics.copies.html) : partage des données.
- [Types numériques NumPy](https://numpy.org/doc/stable/user/basics.types.html) : représentation et conversions.
- [Module `Image` de Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html) : classes, propriétés et méthodes des images.
- [`subplots` de Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html) : création de figures et d'axes.
- [`imshow` de Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) : données et paramètres d'affichage.
