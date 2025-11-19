from abc import ABC, abstractmethod
class PetInfo:
    @abstractmethod
    def get_info(self):
        pass
        # 'raise NotImplementedError' если надо без импорта

class CoolAnimalLibrary:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def get_details(self):
        return f'Animal Details: {self.type_}, {self.name}'

class AnimalAdapter(PetInfo):
    def __init__(self, animal):
        self.animal = animal
    def get_info(self):
        raw_details = self.animal.get_details()
        return raw_details

def show_pet_info(pet):
    print(pet.get_info())

cat = CoolAnimalLibrary('Silvester', 'cat')
adapt_cat = AnimalAdapter(cat)
show_pet_info(adapt_cat)