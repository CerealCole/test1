""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 202x Test 1
"""
class Resistor(object):
    """Model a fixed resistor."""
    
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)


### DEFINE class VariableResistor HERE ###
class VariableResistor(Resistor):
    """Model a variable resistor that can change its actual resistance based on a percentage of fixed resistance."""
    
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms and initializes actual_resistance."""
        super().__init__(res)  # Call the constructor of the parent class (Resistor)
        self.actual_resistance = res  # Initialize actual_resistance to the fixed resistance initially


if __name__ == "__main__":
    # This section will be uncommented in later steps for testing
    pass
