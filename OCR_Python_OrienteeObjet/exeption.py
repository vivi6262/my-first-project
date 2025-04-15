class Passenger:
    def __init__(self, bag):
        self.bag = bag

    def fly_in(self):
        try:
            passport = self.bag["passeport"]
        except KeyError:
            raise NoPassportException()
        else:
            print("Je prends l'avion")

class NoPassportException(Exception):
    def __init__(self, msg="Tu as oublié ton passeport!", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

bag = {"clothing":10}
passenger = Passenger(bag=bag)
passenger.fly_in()