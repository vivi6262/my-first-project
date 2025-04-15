"""Contacts.

Séparez le programme en plusieurs modules et packages,
en ajoutant les fichiers __init__.py et les imports si necessaire.

Vérifiez que le programme s'éxecute correctement en lancant main.py depuis la racine
du projet.
"""


from mon_package import TextContact as cs, user, send_mass_messages as smm


# Our main program.
alice = user.User("Alice", cs.TextContactSystem("0102030405"))
bob = user.User("Bob", cs.OwlContactSystem("4 Privet Drive"))

user_list = [alice, bob]
smm.send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
smm.send_mass_messages(
    "Salut {name}. Tes informations de contact sont-elles corrects?"
    " Nous avons celles-ci: {contact_info}.",
    user_list,
)