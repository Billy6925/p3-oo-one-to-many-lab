class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name,pet_type,owner =None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f'Invalid pet_type: {pet_type}. Choose from {self.PET_TYPES}')
        self.name = name
        self.pet_type = pet_type
        self.owner =owner
        Pet.all.append(self)

class Owner:
    def __init__(self,name):
        self.name =name
    def pets(self):
        return [pets for pets in Pet.all if pets.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise Exception("Pet must be an instance of the Pet class")
        pet.owner =self
    def get_sorted_pets(self):
        return sorted(self.pets(), key= lambda pets: pets.name)

        
        