from Wizard import Wizard
from Archer import Archer

class WizardArcher(Wizard, Archer):
    
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)