import random
#polymorphism means ability to perform in many forms,same function can behave diffrently
class DentalHealthItem():
    def __init__(self,price):
        self.price=price

class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"

toothbrush=Toothbrush(price=100)
floss=Floss(price=50)
mouthwash=Mouthwash(price=80)
dental_health_kit=[toothbrush,floss,mouthwash]
random.shuffle(dental_health_kit)
actions=[value.use() for value in dental_health_kit]
print(actions)


