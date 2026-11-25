# Python 0 — Leçon de synthèse

**École 42 · Piscine Python for Data Science · Starting**

Cette leçon reprend les notions des dix exercices du dépôt, à partir du
[sujet fourni, version 2.0](en.subject.pdf) et des implémentations présentes.
Elle explique les mécanismes à savoir utiliser et justifier en soutenance.
Les exemples courts sont des fragments pédagogiques ; les fichiers à rendre
restent soumis aux règles de structure du sujet.

## Sommaire

1. [Parcours et règles du projet](#1-parcours-et-règles-du-projet)
2. [Syntaxe, fonctions et modules](#2-syntaxe-fonctions-et-modules)
3. [Collections et mutabilité — ex00](#3-collections-et-mutabilité--ex00)
4. [Dates et formatage — ex01](#4-dates-et-formatage--ex01)
5. [Objets et types — ex02](#5-objets-et-types--ex02)
6. [Valeurs nulles, vérité et identité — ex03](#6-valeurs-nulles-vérité-et-identité--ex03)
7. [Arguments, conditions et exceptions — ex04](#7-arguments-conditions-et-exceptions--ex04)
8. [Chaînes et entrées standard — ex05](#8-chaînes-et-entrées-standard--ex05)
9. [Dictionnaire de correspondance et Morse — ex06](#9-dictionnaire-de-correspondance-et-morse--ex06)
10. [Compréhensions, lambda et validation — ex07](#10-compréhensions-lambda-et-validation--ex07)
11. [Itération, générateurs et filtrage — ex08](#11-itération-générateurs-et-filtrage--ex08)
12. [Créer et installer un paquet — ex09](#12-créer-et-installer-un-paquet--ex09)
13. [Qualité du code et vérifications](#13-qualité-du-code-et-vérifications)
14. [Révision et vocabulaire](#14-révision-et-vocabulaire)

## 1. Parcours et règles du projet

### Ce que chaque exercice apprend

| Exercice | Fichier principal | Concepts à retenir |
|---|---|---|
| `ex00` | [Hello.py](../ex00/Hello.py) | `list`, `tuple`, `set`, `dict`, mutation et réaffectation |
| `ex01` | [format_ft_time.py](../ex01/format_ft_time.py) | Timestamp, `time`, `datetime`, f-strings et formats numériques |
| `ex02` | [find_ft_type.py](../ex02/find_ft_type.py) | Fonction, `Any`, annotations, `type`, `isinstance`, affichage et retour |
| `ex03` | [NULL_not_found.py](../ex03/NULL_not_found.py) | `None`, NaN, zéro, chaîne vide, `False`, égalité et identité |
| `ex04` | [whatis.py](../ex04/whatis.py) | `sys.argv`, conversion entière, modulo, conditions et erreurs |
| `ex05` | [building.py](../ex05/building.py) | `main`, entrée standard, parcours et classification des caractères |
| `ex06` | [sos.py](../ex06/sos.py) | Table de correspondance, normalisation, validation et assemblage |
| `ex07` | [filterstring.py](../ex07/filterstring.py) | Découpage en mots, compréhension de liste, lambda et `all` |
| `ex08` | [ft_filter.py](../ex08/ft_filter.py) | Prédicat, itérable, itérateur, `yield`, évaluation paresseuse |
| `ex09` | [ft_package](../ex09/src/ft_package/) | API publique, imports, métadonnées, construction et installation |

### Les contraintes font partie de l'apprentissage

Le sujet demande Python **3.10 ou supérieur**, des imports explicites et interdit
les variables globales. Les autorisations propres à chaque exercice priment :
par exemple, `ex02` et `ex03` n'autorisent que `typing` comme bibliothèque,
et `ex08` interdit d'utiliser le `filter` natif pour réaliser `ft_filter`.

À partir d'`ex05`, le sujet ajoute les exigences suivantes :

- Placer la logique dans des fonctions et structurer les programmes avec `main()`.
- Protéger l'appel à `main()` avec `if __name__ == "__main__":`.
- Intercepter les exceptions attendues pour éviter une traceback non gérée.
- Documenter toutes les fonctions avec une docstring.
- Respecter les règles de style contrôlées par Flake8.

Les fonctions à importer, comme `ft_filter`, doivent rester utilisables sans
lancer de démonstration à l'import. Leurs éventuels tests se placent dans un
programme de test ou derrière la garde `__main__`.

La fiche décrit les notions ; elle ne certifie pas la conformité de chaque
fichier. Les noms de fichiers, messages, espaces et retours à la ligne demandés
par le sujet restent à vérifier lors de l'évaluation.

## 2. Syntaxe, fonctions et modules

### Indentation et noms

Python délimite les blocs par l'indentation, avec quatre espaces par niveau.
Une instruction `if`, `for`, `def` ou `try` introduit son bloc avec `:`.

```python
def describe(number: int) -> str:
    """Describe whether a number is positive."""
    if number > 0:
        return "positive"
    return "zero or negative"
```

Les noms de variables et de fonctions suivent généralement `snake_case` ; les
classes, `PascalCase` ; les constantes, `UPPER_SNAKE_CASE`. Les noms imposés par
le sujet, comme `NULL_not_found`, doivent cependant être conservés.

Un commentaire commence par `#`. Une docstring est une chaîne placée comme
première instruction d'une fonction, d'une classe ou d'un module : elle devient
sa documentation accessible avec `help(objet)` ou `objet.__doc__`.

### Paramètres, arguments et retour

```python
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

result = add(20, 22)
```

`a` et `b` sont des **paramètres** ; `20` et `22` sont les **arguments** de
l'appel. `return` termine la fonction et transmet une valeur à l'appelant.
Sans `return` explicite, une fonction ordinaire renvoie `None`.

`print()` produit un affichage et renvoie `None`. Afficher un résultat et le
retourner sont donc deux opérations différentes, distinction centrale d'`ex02`.

### Annotations et typage dynamique

Les annotations `a: int` et `-> int` décrivent les types attendus. Elles servent
à la lecture et aux outils d'analyse ; Python ne les impose pas à l'exécution.

```python
def double(value: int) -> int:
    """Return twice the supplied value."""
    return value * 2

double("Hi")  # Produit "HiHi" malgré l'annotation.
```

`typing.Any`, utilisé dans `ex02` et `ex03`, indique qu'un paramètre peut recevoir
n'importe quel type. Il n'effectue ni conversion ni validation.

Le typage est **dynamique** : les objets ont un type, et un nom peut être
réaffecté à un objet d'un autre type.

```python
value = 42
value = "Hello"
```

### Portée des noms

Python recherche les noms dans l'ordre **LEGB** : local, fonctions englobantes,
module global, puis noms natifs (*built-ins*). Un nom affecté dans une fonction
est normalement local à cette fonction.

Les blocs `if`, `for` et `try` ne créent pas leur propre portée. En revanche,
la variable d'itération d'une compréhension de liste reste dans sa portée.

Éviter de masquer des noms natifs comme `list`, `str`, `filter` ou `object` rend
le code plus facile à lire. La signature imposée d'`ex02` utilise néanmoins
`object` comme nom de paramètre.

En complément, Python possède `global` pour réaffecter un nom du module et
`nonlocal` pour réaffecter un nom d'une fonction englobante. Le projet interdit
les variables globales : transmettre les données par paramètres et retours.

### Module, import et point d'entrée

Un **module** est notamment un fichier Python importable. L'import exécute son
code de premier niveau lors de son premier chargement dans le processus.

```python
import sys
from datetime import datetime
```

Les imports explicites permettent d'identifier l'origine des noms. Les imports
avec `*` sont interdits dans le sujet.

```python
def main() -> None:
    """Run the program."""
    print("Hello")


if __name__ == "__main__":
    main()
```

Lors d'une exécution directe, `__name__` vaut `"__main__"`. Lors d'un import,
il contient le nom du module : la garde empêche alors l'appel à `main()`.
Définir une fonction ne lance pas son corps. Cela explique pourquoi les modules
`find_ft_type.py` et `NULL_not_found.py` n'affichent rien exécutés seuls.

## 3. Collections et mutabilité — ex00

### Choisir une structure

| Type | Syntaxe | Ordre | Mutable | Particularité |
|---|---|---|---|---|
| `list` | `["Hello"]` | Ordre des éléments | Oui | Indices et doublons |
| `tuple` | `("Hello", "toto!")` | Ordre des éléments | Non | Séquence immuable |
| `set` | `{"Hello", "tutu!"}` | Aucun ordre garanti | Oui | Éléments uniques et hachables |
| `dict` | `{"Hello": "titi!"}` | Ordre d'insertion | Oui | Clés uniques et hachables |

Un objet **mutable** peut changer de contenu en conservant son identité.
Un objet **immuable** ne peut pas être modifié ; on construit un autre objet et
on réaffecte le nom. Les chaînes sont également immuables.

### Les quatre opérations de l'exercice

```python
ft_list = ["Hello"]
ft_list.append("World!")

ft_tuple = ("Hello", "toto!")
ft_tuple = ft_tuple[:1] + ("France!",)

ft_set = {"Hello", "Hello", "tutu!"}
ft_set.discard("tutu!")
ft_set.add("Paris!")

ft_dict = {"Hello": "titi!"}
ft_dict["Hello"] = "42Paris!"
```

- `append()` modifie la liste en place et retourne `None`.
- Le slicing et la concaténation construisent un nouveau tuple. La virgule de
  `("France!",)` est nécessaire pour créer un tuple à un élément.
- Le set supprime les doublons dès sa création. `discard()` retire un élément
  s'il existe ; `remove()` lève une `KeyError` s'il est absent.
- L'affectation par clé remplace la valeur associée dans le dictionnaire.

`{}` crée un dictionnaire vide ; `set()` crée un ensemble vide. Une liste ne
peut pas servir de clé de dictionnaire ou d'élément de set, car elle n'est pas
hachable. Un tuple n'est hachable que si tous ses éléments le sont.

### Références et alias

```python
first = [1, 2]
second = first
second.append(3)
print(first)  # [1, 2, 3]
```

L'affectation ne copie pas la liste : les deux noms désignent le même objet.
Un tuple peut contenir une liste mutable ; son immutabilité empêche de remplacer
ses éléments, mais ne rend pas immuables les objets qu'il contient.

L'ordre d'affichage d'un set peut varier d'une exécution à l'autre. Un test qui
compare exactement la ligne imprimée par `ex00` peut donc échouer malgré un
contenu correct ; il faut comparer les ensembles sans dépendre de leur ordre.

## 4. Dates et formatage — ex01

### Timestamp et calendrier

```python
import time
from datetime import datetime

now = time.time()
local_date = datetime.fromtimestamp(now)
```

`time.time()` fournit un timestamp exprimé en secondes depuis l'époque Unix,
le **1er janvier 1970 à 00:00:00 UTC**. La partie décimale représente une
fraction de seconde.

`datetime.fromtimestamp(now)` convertit ce timestamp en date et heure locales
selon le fuseau de l'environnement. Sans argument de fuseau, l'objet obtenu ne
porte pas d'information de fuseau explicite.

Le script prélève le timestamp une seule fois, puis l'utilise pour les deux
lignes : les représentations numérique et calendaire décrivent le même instant.

### F-strings et spécificateurs de format

```python
value = 1666355857.3622
print(f"{value:,.4f}")  # 1,666,355,857.3622
print(f"{value:.2e}")   # 1.67e+09
```

Une f-string insère les expressions entre `{}`. Après `:`, le format précise
la représentation souhaitée :

| Élément | Effet |
|---|---|
| `,` | Sépare les milliers avec des virgules |
| `.4f` | Affiche quatre décimales en notation fixe |
| `.2e` | Affiche deux décimales en notation scientifique |

Le formatage arrondit l'affichage sans changer la valeur numérique d'origine.
`1.67e+09` signifie `1.67 × 10⁹`.

### Formater la date avec `strftime()`

```python
date = datetime.fromtimestamp(now).strftime("%b %d %Y")
```

| Directive | Signification | Exemple |
|---|---|---|
| `%b` | Mois abrégé selon la locale | `Oct` |
| `%d` | Jour sur deux chiffres | `21` |
| `%Y` | Année sur quatre chiffres | `2022` |

La date dépend de l'instant et du fuseau ; le nom du mois dépend aussi de la
locale. Le test doit vérifier le format, sans figer la date du sujet comme
résultat attendu.

## 5. Objets et types — ex02

Les principaux types rencontrés sont `int`, `float`, `str`, `bool`, `NoneType`
et les quatre collections d'`ex00`. Python représente ces valeurs par des objets.

### `type()` et `isinstance()`

```python
type(42)                    # <class 'int'>
type("Hello")               # <class 'str'>
isinstance([1, 2], list)     # True
isinstance(42, (int, float)) # True
```

`type(value)` renvoie le type exact. `isinstance(value, Class)` accepte aussi
les instances des sous-classes. Le choix dépend du contrat de la fonction.

```python
isinstance(True, int)  # True : bool est une sous-classe de int.
type(True) is int      # False : son type exact est bool.
```

### Affichage et valeur de retour

`all_thing_is_obj()` identifie les collections et chaînes, affiche le message
correspondant, puis **retourne toujours `42`**, y compris pour un type inconnu.

```python
from find_ft_type import all_thing_is_obj

result = all_thing_is_obj(10)  # Affiche "Type not found".
print(result)                 # Affiche 42.
```

Ce fragment s'exécute depuis `ex02/`. Le nombre retourné par une fonction n'est
pas automatiquement le code de sortie du processus : cela demanderait par
exemple de le transmettre à `sys.exit()`.

## 6. Valeurs nulles, vérité et identité — ex03

### Cinq cas différents

| Valeur | Type | Sens | Test adapté à l'exercice |
|---|---|---|---|
| `None` | `NoneType` | Absence de valeur | `value is None` |
| `float("nan")` | `float` | Not a Number | `isinstance(value, float) and value != value` |
| `0` | `int` | Zéro entier | `type(value) is int and value == 0` |
| `""` | `str` | Chaîne vide | `isinstance(value, str) and value == ""` |
| `False` | `bool` | Booléen faux | `value is False` |

`NULL_not_found()` retourne `0` pour un cas reconnu et `1` sinon. Une condition
unique `if not value:` ne suffit pas à distinguer ces cinq valeurs.

### Égalité et identité

```python
left = [1, 2]
right = [1, 2]

left == right  # True : même contenu.
left is right  # False : objets distincts.

False == 0     # True.
type(False) is int  # False.
```

`==` compare les valeurs ; `is` compare l'identité des objets. `None` est un
singleton : on le teste avec `is None`. On n'utilise pas `is` pour comparer la
valeur de nombres ou de chaînes.

Pour reconnaître zéro sans absorber `False`, le code d'`ex03` vérifie le type
exact `int`. Cela exclut aussi `0.0`, qui est un `float`.

### NaN et valeur de vérité

```python
nan = float("nan")
nan == nan  # False.
nan != nan  # True.
bool(nan)   # True.
```

NaN n'est pas égal à lui-même. Le test du dépôt vérifie d'abord qu'il s'agit
d'un flottant, puis exploite cette propriété. Hors restriction d'import,
`math.isnan()` permet aussi de détecter NaN.

Dans une condition, les valeurs suivantes sont **falsy** : `None`, `False`, les
zéros numériques et les collections vides (`""`, `[]`, `()`, `{}`, `set()`).
Les autres valeurs ordinaires présentées ici sont **truthy** :

```python
bool("False")  # True : la chaîne n'est pas vide.
bool(-5)       # True.
```

## 7. Arguments, conditions et exceptions — ex04

### Lire `sys.argv`

```bash
python3 ex04/whatis.py -5
```

`sys.argv` contient alors le nom ou chemin du script en position `0`, puis
`"-5"` en position `1`. **Tous ses éléments sont des chaînes**. Il faut vérifier
sa longueur avant d'accéder aux positions attendues.

Pour transmettre une phrase comme un seul argument, on utilise les guillemets
du shell : `python3 ex05/building.py "Hello World!"`.

### Convertir et calculer la parité

```python
number = int("-5")
parity = "I'm Even." if number % 2 == 0 else "I'm Odd."
```

`int()` convertit une représentation entière. `int("3.14")` et `int("hello")`
lèvent une `ValueError`. Tester seulement `.isdigit()` rejetterait des entiers
signés valides, comme `"-5"`.

Le **modulo** `%` fournit le reste : un entier est pair si `number % 2 == 0`.
Le test fonctionne aussi pour zéro et les entiers négatifs.

L'expression `a if condition else b` choisit une valeur. Pour plusieurs branches,
on utilise `if`, `elif`, `else`. Python n'a pas d'opérateur d'incrémentation
`++` : on écrit `count += 1`.

### Lever et intercepter une erreur

```python
try:
    number = int(text)
except ValueError:
    raise AssertionError("argument is not an integer") from None
```

`raise` lève une exception. `try` / `except` intercepte les types d'exceptions
indiqués. `from None` masque l'affichage du contexte de l'exception précédente ;
il ne dispense pas d'intercepter la nouvelle exception.

```python
try:
    main()
except AssertionError as error:
    print(f"AssertionError: {error}")
```

Ce dernier bloc transforme l'exception en message affiché sans traceback.
Un simple `print("AssertionError: ...")` ne lève aucune exception.

| Exception | Cause typique dans le projet |
|---|---|
| `ValueError` | Conversion `int()` impossible |
| `AssertionError` | Validation échouée avec `assert` ou erreur levée explicitement |
| `IndexError` | Position absente dans `sys.argv` ou une séquence |
| `KeyError` | Clé absente lors d'un accès `mapping[key]` |
| `TypeError` | Opération ou argument d'un type incompatible |
| `StopIteration` | Fin d'un itérateur demandé avec `next()` |

### Assertions et ordre des contrôles

```python
assert len(sys.argv) == 2, "more than one argument is provided"
```

Une assertion fausse lève `AssertionError` avec le message donné. Les assertions
peuvent être supprimées avec `python -O`. Une validation qui doit toujours
s'exécuter peut utiliser `if ...: raise ...` ; le sujet impose surtout le
comportement et les messages observables.

Une instruction située avant le `try` n'est pas protégée par son `except`.
Intercepter plusieurs erreurs est possible avec
`except (ValueError, AssertionError):`.

Pour `whatis.py`, aucun argument signifie une sortie silencieuse. Un argument
supplémentaire et une valeur non entière produisent deux messages distincts.

## 8. Chaînes et entrées standard — ex05

### Parcourir et classifier les caractères

```python
import string

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    elif char in string.punctuation:
        punctuation += 1
```

Les compteurs doivent être initialisés avant la boucle. La chaîne
`if` / `elif` compte chaque caractère dans au plus une catégorie.

| Outil | Usage |
|---|---|
| `len(text)` | Nombre total de points de code Unicode dans la chaîne |
| `.isupper()` / `.islower()` | Détecter la casse |
| `.isspace()` | Reconnaître espace, tabulation, retour à la ligne, etc. |
| `.isdigit()` | Reconnaître des chiffres, y compris certains caractères Unicode |
| `.isalpha()` / `.isalnum()` | Reconnaître lettres / lettres et caractères numériques |
| `string.punctuation` | Ensemble des caractères de ponctuation ASCII, sous forme de chaîne |
| `.isprintable()` | Déterminer si les caractères sont imprimables ; `""` donne `True` |

Les méthodes de classification telles que `.isalnum()` exigent une chaîne non
vide pour donner `True`. Les tests Unicode ne se limitent pas à `A-Z` ou `0-9`.
La ponctuation Unicode n'est pas entièrement contenue dans `string.punctuation`.
Certains caractères peuvent donc être inclus dans `len(text)` sans appartenir
aux catégories comptées. La somme des compteurs n'est pas toujours le total
pour un texte Unicode quelconque.

### `input()` et `readline()`

Dans `building.py`, l'absence d'argument ou un argument vide déclenche une
lecture avec `sys.stdin.readline()` après affichage de la question.

| Lecture | Retour à la ligne final | Fin de fichier sans texte |
|---|---|---|
| `input()` | Retiré | Lève `EOFError` |
| `sys.stdin.readline()` | Conservé s'il est présent | Renvoie `""` |

Ainsi, `"Hello World!"` compte 12 caractères et un espace, tandis que
`"Hello World!\n"` compte 13 caractères et deux espaces blancs. Cette différence
est explicitement attendue par le sujet.

### Indexation, slicing et immutabilité

```python
text = "Python"
text[0]     # "P"
text[-1]    # "n"
text[:3]    # "Pyt"
text[2:]    # "thon"
text[::-1]  # "nohtyP"
```

La forme générale est `sequence[start:stop:step]` ; la borne `stop` est exclue.
Un indice absent provoque `IndexError`, tandis qu'un slicing tolère des bornes
hors limites. Un pas nul n'est pas valide.

Une chaîne ne permet pas `text[0] = "J"`. Concaténer, découper ou changer la
casse produit une chaîne résultante sans modifier l'original.

```python
"Hello".upper()       # "HELLO"
"HELLO".lower()       # "hello"
"  Hello  ".strip()   # "Hello"
"  Hello  ".lstrip()  # "Hello  "
"  Hello  ".rstrip()  # "  Hello"
```

`text[:-1]` retire exactement le dernier caractère, s'il existe ; `rstrip()`
retire tous les espaces blancs finaux par défaut. Ils ne sont pas
interchangeables pour un compteur de caractères.

Une chaîne entre triples guillemets peut contenir plusieurs lignes. Dans le
résultat d'`ex05`, les retours à la ligne de la f-string font partie du rapport.

## 9. Dictionnaire de correspondance et Morse — ex06

### Associer une clé à une valeur

Un dictionnaire représente une **table de correspondance** : ici, un caractère
vers son code Morse. Dans le dépôt, `NESTED_MORSE` est un dictionnaire simple,
malgré son nom. Il contient l'espace, les lettres `A-Z` et les chiffres `0-9`.

```python
mapping = {"S": "...", "O": "---", " ": "/"}
mapping["S"]       # "..."
mapping.get("?")  # None
"S" in mapping    # True : teste les clés.
```

`mapping[key]` lève `KeyError` si la clé est absente. `.get(key, default)`
renvoie une valeur par défaut, `None` si elle n'est pas précisée. Ici, aucun
code valide ne vaut `None`, ce qui permet d'utiliser cette valeur pour détecter
un caractère non pris en charge.

### Normaliser, valider et assembler

Le traitement du dépôt suit ces étapes :

1. Vérifier qu'un seul argument utilisateur est fourni.
2. Parcourir le texte et normaliser chaque caractère avec `.upper()`.
3. Chercher son code dans le dictionnaire ; rejeter une clé absente.
4. Accumuler les codes avec `append()` puis les assembler avec `join()`.

Chaque valeur du dictionnaire contient un espace final. Le code effectue donc
`"".join(morse)[:-1]` pour retirer le dernier séparateur. Une variante consiste
à stocker les codes sans espace final et à utiliser `" ".join(codes)`.

`join()` appartient au séparateur, qui est une chaîne ; les éléments à
assembler doivent eux aussi être des chaînes.

```python
" ".join(["...", "---", "..."])  # "... --- ..."
"-".join(["Hello", "World"])    # "Hello-World"
```

Accumuler les fragments puis les joindre évite de multiplier les concaténations
de chaînes immuables.

Un espace du texte devient `/` ; les codes restent séparés par un seul espace :

```text
SOS 42 → ... --- ... / ....- ..---
```

Le dictionnaire définit les caractères réellement acceptés. `"é".isalnum()`
vaut `True`, mais `é` n'a pas de clé dans cette table : un test alphanumérique
seul ne suffit donc pas pour valider le Morse.

## 10. Compréhensions, lambda et validation — ex07

### Découper les mots

```python
"Hello  the World".split()  # ["Hello", "the", "World"]
"a,b,c".split(",")         # ["a", "b", "c"]
```

Sans séparateur explicite, `split()` regroupe les suites d'espaces blancs et
ignore ceux du début et de la fin. Avec `split(" ")`, les espaces consécutifs
peuvent créer des éléments vides. Dans `ex07`, la validation rejette les
caractères invisibles comme les tabulations avant le découpage.

### Construire une liste avec une compréhension

```python
text = "Hello the World"
number = 4
result = [word for word in text.split() if len(word) > number]
# ["Hello", "World"]
```

La syntaxe générale est `[expression for element in iterable if condition]`.
La condition sélectionne les éléments ; l'expression détermine les valeurs
stockées. La liste est construite immédiatement, dans l'ordre du parcours.

Le seuil est **strictement supérieur** : un mot de longueur égale à `number`
est exclu. Une chaîne vide ou un seuil trop grand donne `[]`.

Pour transformer et filtrer :

```python
[n * n for n in range(6) if n % 2 == 0]  # [0, 4, 16]
```

Une compréhension peut aussi produire un set (`{expression for ...}`) ou un
dictionnaire (`{key: value for ...}`), notions complémentaires à cet exercice.

### Lambda et fonctions de première classe

Une fonction est un objet : on peut la passer à une autre fonction. Une
**lambda** crée une fonction anonyme limitée à une expression ; le résultat
est retourné implicitement.

```python
lambda word: len(word) > number
```

Le sujet exige une compréhension et une lambda. Le dépôt les combine ainsi :

```python
result = [
    word for word in text.split()
    if (lambda w: len(w) > number)(word)
]
```

La lambda reçoit le mot et calcule le prédicat. Sans contrainte pédagogique,
la condition directe `if len(word) > number` suffirait.

Une lambda peut aussi fournir une clé de tri :
`sorted(["Python", "Hi"], key=lambda word: len(word))`.
Si une fonction doit être nommée, préférer `def` : l'affectation
`double = lambda x: x * 2` est signalée par la règle Flake8 E731.

### `all()`, `any()` et court-circuit

```python
valid = all(char.isalnum() or char == " " for char in text)
```

Ce test autorise les caractères alphanumériques Unicode et l'espace classique,
mais rejette ponctuation, tabulations et retours à la ligne.

- `all(iterable)` renvoie `True` si chaque élément est truthy ; `all([])` vaut
  `True`. Il s'arrête au premier élément falsy.
- `any(iterable)` renvoie `True` dès qu'un élément est truthy ; `any([])` vaut
  `False`.

L'expression entre parenthèses est un générateur : les tests sont produits à la
demande. Pour interdire aussi un texte vide, il faudrait une condition séparée ;
le test du dépôt accepte la chaîne vide.

`and` et `or` court-circuitent aussi l'évaluation et renvoient l'un de leurs
opérandes, pas nécessairement un booléen :

```python
0 or 42        # 42
"Hello" and 5  # 5
```

La condition `value is not None and value > 0` évite d'évaluer la comparaison
numérique quand `value` est `None`.

## 11. Itération, générateurs et filtrage — ex08

### Itérable et itérateur

Un **itérable** fournit un itérateur : liste, tuple, chaîne, set, dictionnaire,
`range`, etc. Un **itérateur** fournit les valeurs successives et conserve sa
position de parcours.

```python
numbers = [10, 20]
iterator = iter(numbers)
next(iterator)        # 10
next(iterator)        # 20
next(iterator, None)  # None : valeur par défaut après épuisement.
```

Sans valeur par défaut, `next()` lève `StopIteration` à l'épuisement. Une boucle
`for` gère cette fin automatiquement. Le protocole d'un itérateur repose sur
`__iter__()`, qui renvoie l'itérateur lui-même, et `__next__()`.

Une liste peut fournir un nouvel itérateur pour un nouveau parcours. Un
itérateur épuisé ne recommence pas au début :

```python
iterator = iter([1, 2])
list(iterator)  # [1, 2]
list(iterator)  # []
```

Quelques outils de parcours complémentaires :

| Outil | Effet |
|---|---|
| `range(2, 8, 2)` | Itérable produisant `2`, `4`, `6` ; borne finale exclue |
| `enumerate("AB")` | Fournit les couples `(0, "A")`, `(1, "B")` |
| `break` | Termine la boucle |
| `continue` | Passe à l'itération suivante |

`range()` est un itérable réutilisable, sans construire une liste de tous ses
entiers ; il n'est pas lui-même un itérateur.

### `yield` et évaluation paresseuse

```python
def counter():
    """Yield two successive numbers."""
    yield 1
    yield 2


gen = counter()  # Le corps n'a pas encore été exécuté.
next(gen)        # 1.
next(gen)        # 2.
```

Une fonction contenant `yield` est une **fonction génératrice**. Son appel
renvoie un générateur, qui est un itérateur. `yield` produit une valeur puis
suspend l'exécution ; l'appel suivant reprend après ce point en conservant les
variables locales. `return` termine le générateur.

Une expression génératrice utilise une syntaxe proche d'une compréhension :

```python
squares = (n * n for n in range(1_000_000))
```

Les carrés sont calculés à la demande. La variante `[n * n for ...]` construit
une liste immédiatement. Le gain de mémoire concerne les résultats produits ;
un générateur peut toujours conserver une référence à une grosse entrée.

### Reproduire `filter()`

Un **prédicat** est une fonction utilisée pour décider si un élément doit être
conservé. Son résultat est évalué selon sa valeur de vérité, sans exiger
exactement `True`.

```python
def ft_filter(function, iterable):
    """\
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        function = bool
    for item in iterable:
        if function(item):
            yield item
```

C'est l'implémentation présente dans le dépôt. Elle conserve les éléments
originaux pour lesquels le prédicat est truthy. Si le prédicat vaut `None`,
elle conserve directement les éléments truthy.

```python
list(ft_filter(lambda n: n % 2 == 0, range(6)))  # [0, 2, 4]
list(ft_filter(None, [0, "", None, "Hello", 3]))  # ["Hello", 3]
```

`print(ft_filter(...))` affiche une représentation du générateur. Utiliser
`list(...)`, `next(...)` ou une boucle pour obtenir ses valeurs.

| Construction | Résultat | Moment du filtrage |
|---|---|---|
| `[x for x in data if predicate(x)]` | Liste | Immédiatement |
| `(x for x in data if predicate(x))` | Générateur | À la consommation |
| `filter(predicate, data)` | Itérateur natif | À la consommation |
| `ft_filter(predicate, data)` | Générateur | À la consommation |

Le sujet exige `yield` et une docstring identique à `filter.__doc__`. La
vérification porte sur la chaîne exacte, y compris espaces et retours à la
ligne : une indentation ajoutée à la docstring peut changer son contenu.

Le générateur reproduit les valeurs filtrées, mais pas tous les détails de
construction de l'objet natif. `filter(None, 42)` lève `TypeError` dès l'appel ;
`ft_filter(None, 42)` ne lève l'erreur qu'à la première consommation, puisque
son corps est différé. Une exception du prédicat apparaît également pendant
la consommation : le `try` doit entourer cette étape pour l'intercepter.

## 12. Créer et installer un paquet — ex09

### Module, paquet et distribution

Un **module** contient du code importable. Un **paquet** regroupe des modules
sous un espace de noms. Une **distribution** est le projet installable avec
ses fichiers et ses métadonnées.

L'organisation du dépôt suit la disposition `src` :

```text
ex09/
├── pyproject.toml
├── README.md
├── LICENSE
├── .python-version
├── src/
│   └── ft_package/
│       ├── __init__.py
│       └── count_in_list.py
├── tests/
│   └── test.py
└── dist/
    ├── ft_package-0.0.1.tar.gz
    └── ft_package-0.0.1-py3-none-any.whl
```

Cette disposition sépare le code importable des fichiers du projet. Depuis
`ex09/`, il faut installer le paquet dans l'environnement utilisé pour exécuter
normalement le test ; la présence d'un dossier `src/` ne suffit pas à rendre
son contenu importable.

### Fonction et API publique

```python
def count_in_list(data_list: list, string: str) -> int:
    """Count occurrences of a string in a list."""
    return data_list.count(string)
```

`list.count(value)` compte les éléments égaux à `value`. Un élément absent
produit `0`.

Dans `__init__.py` :

```python
from .count_in_list import count_in_list

__all__ = ["count_in_list"]
```

Le point désigne un **import relatif** au paquet courant. La réexportation
permet à l'utilisateur d'écrire `from ft_package import count_in_list`.
`__all__` décrit notamment les noms exportés par un import avec `*` ; ce n'est
pas un mécanisme de confidentialité et cela n'impose pas d'utiliser `*`.

### Rôle de `pyproject.toml`

Le fichier utilise TOML pour configurer le projet et sa construction.

| Élément du dépôt | Rôle |
|---|---|
| `[project]` | Métadonnées de la distribution |
| `name`, `version` | `ft_package`, version `0.0.1` |
| `description`, `readme` | Résumé et description du projet |
| `authors`, `license`, `license-files` | Auteur et licence MIT |
| `requires-python = ">=3.12"` | Version minimale déclarée par ce paquet |
| `dependencies = []` | Aucune dépendance d'exécution déclarée |
| `[project.urls]` | Liens vers le dépôt et les issues |
| `[build-system]` | Dépendances et moteur de construction |
| `build-backend = "uv_build"` | Backend chargé de produire les distributions |

Le sujet accepte Python 3.10+, mais **ce paquet déclare Python 3.12+**.
Le fichier `.python-version` indique également `3.12` aux outils qui le lisent ;
il ne remplace pas la contrainte `requires-python`.

Les dépendances de construction, comme `uv_build`, servent à fabriquer le
paquet. Elles se distinguent des dépendances nécessaires à son utilisation.
`uv` est ici un outil capable de lancer la construction ; `pip` installe les
distributions obtenues.

### Environnement virtuel, construction et installation

Un environnement virtuel isole les paquets du projet de ceux du système. Les
commandes suivantes sont à lancer depuis `ex09/`, avec Python 3.12 ou supérieur,
`pip` disponible dans le venv et `uv` disponible pour la construction :

```bash
python3 -m venv .venv
source .venv/bin/activate
uv build
python -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
python -m pip list
python -m pip show -v ft_package
python tests/test.py
```

`uv build` produit les deux archives dans `dist/` :

- Le **sdist** `.tar.gz` contient les sources nécessaires à la construction.
  Son installation peut nécessiter de récupérer les outils de construction.
- Le **wheel** `.whl` est une distribution construite, directement installable.
  Le suffixe `py3-none-any` indique un wheel Python 3 sans ABI spécifique et
  indépendant de la plateforme.

Il n'est pas nécessaire de publier sur PyPI : l'installation locale suffit
pour cet exercice. Pour vérifier aussi le sdist dans le même environnement,
on peut réinstaller explicitement cette archive :

```bash
python -m pip install --force-reinstall ./dist/ft_package-0.0.1.tar.gz
python tests/test.py
```

Le test doit afficher `2` puis `0` avec chaque distribution. Employer
`python -m pip` rattache les opérations au même interpréteur que le test.
`deactivate` quitte l'environnement virtuel.

## 13. Qualité du code et vérifications

### Style et documentation

PEP 8 décrit les conventions de style : indentation, espaces autour des
opérateurs, nommage et séparation des fonctions. PEP 257 décrit les conventions
de docstrings.

**Flake8** est un linter : il analyse le code sans lancer le programme et
signale des problèmes de style et certaines erreurs probables. Il ne prouve
pas que le comportement est correct et, sans extension, ne vérifie pas toutes
les conventions de docstrings.

Depuis la racine, avec Flake8 installé :

```bash
flake8 ex00 ex01 ex02 ex03 ex04 ex05 ex06 ex07 ex08 ex09/src ex09/tests
```

Le fichier `.flake8` exclut `.venv`. `pip` installe des paquets dans un
environnement Python ; `pipx` sert plutôt à installer des applications en ligne
de commande dans des environnements isolés, par exemple un linter.

### Vérifier les comportements observables

Les commandes ci-dessous partent de la racine du dépôt :

| Cas | Commande ou vérification | Résultat attendu |
|---|---|---|
| Parité négative | `python3 ex04/whatis.py -5` | `I'm Odd.` |
| Aucun argument | `python3 ex04/whatis.py` | Aucun affichage |
| Conversion invalide | `python3 ex04/whatis.py abc` | `AssertionError: argument is not an integer` |
| Trop d'arguments | `python3 ex04/whatis.py 1 2` | `AssertionError: more than one argument is provided` |
| Texte en argument | `python3 ex05/building.py "Hello World!"` | 12 caractères ; 2 majuscules, 8 minuscules, 1 ponctuation, 1 espace, 0 chiffre |
| Texte via stdin | `printf 'Hello World!\n' \| python3 ex05/building.py` | 13 caractères, dont 2 espaces blancs |
| Morse valide | `python3 ex06/sos.py "sos"` | `... --- ...` |
| Morse invalide | `python3 ex06/sos.py 'h$llo'` | `AssertionError: the arguments are bad` |
| Filtrage | `python3 ex07/filterstring.py "Hello the World" 4` | `['Hello', 'World']` |
| Seuil trop grand | `python3 ex07/filterstring.py "Hello the World" 99` | `[]` |
| Arguments invalides | `python3 ex07/filterstring.py` | `AssertionError: the arguments are bad` |

Pour un test reproductible d'`ex08`, on peut lancer depuis la racine :

```bash
(cd ex08 && python3 - <<'PY'
from ft_filter import ft_filter

assert ft_filter.__doc__ == filter.__doc__
assert list(ft_filter(None, [0, "", None, "Hello", 3])) == ["Hello", 3]
assert list(ft_filter(lambda x: x % 2 == 0, range(6))) == [0, 2, 4]

seen = []


def keep(value):
    seen.append(value)
    return value > 1


gen = ft_filter(keep, [0, 1, 2, 3])
assert seen == []
assert next(gen) == 2
assert seen == [0, 1, 2]
assert list(gen) == [3]
assert list(gen) == []
PY
)
```

Ce test vérifie les valeurs, la documentation, l'absence de calcul initial,
la reprise et l'épuisement. Il complète les testeurs déjà présents dans
`ex02/`, `ex03/`, `ex09/tests/` et `tests/ex00/`.

`cat -e` rend les fins de ligne visibles avec `$` ; ce caractère ne fait pas
partie du texte à produire. Le test shell d'`ex00` compare des sorties exactes :
il reste sensible à l'ordre du set. Pour `ex01`, les valeurs temporelles
changent également à chaque exécution.

## 14. Révision et vocabulaire

### Les distinctions à savoir expliquer

| Notions | Différence essentielle |
|---|---|
| Mutation / réaffectation | Modifier un objet / associer un nom à un objet |
| `list` / `tuple` | Séquence mutable / immuable |
| `set` / `dict` | Valeurs uniques / associations clé-valeur |
| `==` / `is` | Valeur / identité |
| `False` / `0` / `None` | Booléen / entier / absence de valeur |
| `True` / truthy | Booléen précis / valeur acceptée comme vraie |
| `type()` / `isinstance()` | Type exact / appartenance incluant les sous-classes |
| `print()` / `return` | Afficher / transmettre une valeur à l'appelant |
| `return` / `yield` | Terminer / produire une valeur puis suspendre |
| Itérable / itérateur | Fournir un parcours / conserver l'état du parcours |
| Liste / générateur | Résultats construits / résultats produits à la demande |
| `input()` / `readline()` | Retirer / conserver le retour à la ligne final |
| `mapping[key]` / `.get(key)` | Lever `KeyError` / renvoyer un défaut si absent |
| Timestamp / date formatée | Mesure numérique d'un instant / représentation calendaire |
| Module / paquet / distribution | Unité importable / regroupement / projet installable |
| sdist / wheel | Sources à construire / distribution construite |
| Linter / test | Analyse du code / vérification de son exécution |

### Questions de soutenance et petits exercices

1. Modifier les quatre collections d'`ex00` sans écrire directement les valeurs
   finales. Expliquer pourquoi le tuple est réaffecté.
2. Avec le timestamp fixe `1666355857.3622`, retrouver les deux formats numériques
   d'`ex01`. Expliquer ce que le fuseau et la locale peuvent changer.
3. Prédire `False == 0`, `isinstance(False, int)` et `type(False) is int`.
   Justifier l'ordre et les tests choisis dans `NULL_not_found()`.
4. Écrire un traitement d'arguments qui distingue absence, nombre excessif et
   entier invalide, sans accéder à une position absente de `sys.argv`.
5. Comparer les résultats du compteur pour `"Hello World!"` et
   `"Hello World!\n"` ; expliquer le caractère supplémentaire.
6. Encoder `"SOS 42"`, puis expliquer pourquoi la même table refuse `"é"`
   même si cette lettre est alphanumérique.
7. Réécrire le filtrage des mots avec une boucle, une compréhension puis un
   générateur. Identifier le moment où chaque version fait son travail.
8. Créer un générateur de nombres pairs ; consommer une valeur avec `next()`
   puis le reste avec `list()`. Prédire une seconde conversion en liste.
9. Installer successivement les deux distributions d'`ex09` dans un venv et
   expliquer comment `__init__.py` expose `count_in_list`.

### Glossaire bref

| Terme | Sens dans le projet |
|---|---|
| Built-in | Outil fourni directement par Python, comme `len` ou `bool` |
| Mutable / immutable | Objet modifiable / non modifiable après création |
| Hashable — hachable | Objet ayant un hachage stable compatible avec l'égalité ; utilisable comme clé |
| Mapping | Correspondance entre clés et valeurs |
| Scope — portée | Contexte dans lequel un nom est recherché |
| Namespace — espace de noms | Association entre noms et objets |
| Type hint | Annotation décrivant le type attendu |
| Predicate — prédicat | Fonction dont le résultat décide de conserver un élément |
| Callback | Fonction passée à une autre pour être appelée par celle-ci |
| First-class function | Fonction manipulable comme une valeur |
| Lazy / eager evaluation | Calcul à la demande / immédiat |
| Generator | Itérateur produit par une fonction avec `yield` ou une expression génératrice |
| Short-circuit | Arrêt de l'évaluation dès que le résultat est déterminé |
| Traceback | Trace des appels ayant conduit à une exception |
| API publique | Noms et comportements proposés aux utilisateurs d'un module ou paquet |
| Build backend | Outil qui fabrique les distributions à partir du projet |
| Virtual environment | Environnement isolant l'interpréteur et les paquets d'un projet |
