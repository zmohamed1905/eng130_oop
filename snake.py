from reptile import Reptile

class Sk(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
    def use_tongue_to_smell(self):
        return "if I can touch it I can smell it too"

smart_sk = Sk()
print(f"this function is called from the parent class {smart_sk.hunt()}")
print(f"this function is called from the current class {smart_sk.use_tongue_to_smell()}")
print(f"this function is called from the grand-parent class {smart_sk.breathe()}")