import random

class Film:
    """Un film possède un nom, une date de création, et un « lieu » (dans ma bibliothèque ou chez un ami)."""
    def __init__(self, name, date, type):
        self.name = name
        self.date = date
        self.type = type
        self.lieu = None
        self.preter= False
    
    def possession(self):
         print(f"Le film {self.name} est chez {self.lieu} ")

    def __str__(self):
         return f"{self.name}, {self.date}, {self.type}"



class Lieu:
    pass

class Ami(Lieu):
    def __init__(self, nom):
        self.nom = nom
        self.film_preter = []
    def ajouter_film(self, film):
        """Ajoute un film à l'ami"""
        if film.preter == False:
            self.film_preter.append(film)
            film.lieu  = self
            film.preter = True
        else:
            print(f"{film.name} déjà prêté à {film.lieu}")
    def afficher_film(self):
         for film in self.film_preter:
              print(film)

    def __str__(self):
         return self.nom

class Bibliotheque(Lieu):
    def __init__(self):
         self.liste_de_film = []
    def ajouter_film(self, film):
         """Ajoute un film à la bibliothèque"""
         self.liste_de_film.append(film)
         film.lieu = self
    def trier_films(self):
        """Trie les films par date et par nom"""
        self.liste_de_film.sort(key=lambda film: (film.date, film.name))
        print()
    def trier_film_type(self):
         """Trie les films par type"""
         self.liste_de_film.sort(key=lambda film: (film.type))
    def film_au_hasard(self):
         """Récupére un film choisi au hasard"""
         nb_film = len(self.liste_de_film)-1
         x = random.randint(0, nb_film)
         return self.liste_de_film[x]
         
    def __str__(self):
         return "\n".join(str(film) for film in self.liste_de_film)
    
def charger_films(liste_films, bibliotheque):
     for nom, date, type_film in liste_films:
          film = Film(nom, date, type_film)
          bibliotheque.ajouter_film(film)

amis = []
def charger_lieu(friends, bibliotheque):
    for friend in friends:
        ami = Ami(friend[0])
        amis.append(ami)
        for i in range(1, len(friend)):
            nom_film = friend[i]
            film_trouve = None
            for film in bibliotheque.liste_de_film:
                if film.name == nom_film:
                    film_trouve = film
                    break
            if film_trouve:
                ami.ajouter_film(film_trouve)
            else:
                print(f"film {nom_film} introuvable dans la bibliothèque")

def trouver_film(nom_film, bibliotheque):
    for film in bibliotheque.liste_de_film:
        if nom_film == film.name and film.preter == False:
            print(f"{nom_film} se trouve chez la bibliothèque")
            return
    for ami in amis:
        for film in ami.film_preter:
            if nom_film == film.name:
                print(f"{nom_film} est chez {ami.nom}")
                return
    print(f"{film.name} le film est introuvable")
    
    
films_data = [
    ("Star Wars", 1977, "VHF"),
    ("Inception", 2010, "VHF"),
    ("Marvel", 2011, "DVD"),
    ("Batman", 2009, "DVD")
]

friends = [("Jean", "Star Wars", "Inception") , ("Alice","Marvel")]

biblio = Bibliotheque()
charger_films(films_data, biblio)
charger_lieu(friends, biblio)
print(biblio)
for ami in amis:
    print(f"\n Films chez {ami.nom}: ")
    ami.afficher_film()

trouver_film("Star Wars", biblio)

amis[1].ajouter_film(biblio.liste_de_film[0])





    






