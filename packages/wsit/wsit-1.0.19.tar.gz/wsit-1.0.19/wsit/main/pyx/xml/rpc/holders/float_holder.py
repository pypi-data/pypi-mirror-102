import math
from wsit.main.pyx.xml.rpc.holders.holder import Holder

class FloatHolder(Holder):

    def __init__(self, new_value=0.0):
        self.set(new_value)

    def set(self, new_value):
        if type(new_value) in [int, float, float]:
            super().set(float(new_value))
        else:
            raise TypeError("value must be a float or an int type")

    def __eq__(self, obj):
        if isinstance(obj, FloatHolder):
            return math.isclose(self.get(), obj.get())
        return False
