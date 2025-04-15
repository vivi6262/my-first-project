class SmartPlug:
    """Prise intelligente : connecte les appareils."""

    def __init__(self):
        """Initialise la liste d'appareils."""
        self.devices = []

    def connect(self, device):
        """Connecte un appareil à la prise."""
        self.devices.append(device)

    def display_connected_devices(self):
        """Affiche les appareils connectés."""
        print("Affichage des appareils connectés...")

        if not self.devices:
            print("Aucun appareil n'est connecté !")
            return

        for device in self.devices:
            print(f"-> {device.name}")
        print("Fin de l'affichage.")



class Device:
    """Appareil électronique à connecter."""

    def __init__(self, name):
        """Initialise le nom."""
        self.name = name
        
plug = SmartPlug()
pc = Device("pc")
screen = Device("écran")

plug.connect(pc)
plug.connect(screen)

plug.display_connected_devices()