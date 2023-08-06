import numpy as np
from copy import deepcopy
from math import sqrt
from . import Unit
from ..exceptions import UnitDimensionDismatchError, DividingZeroError
from biobuilder.utils.judgement import isAlmostEqual

class Quantity:
    def __init__(self, value, unit:Unit) -> None:
        """
        Parameters
        ----------
        value : int or float
            the value of quantity
        unit : Unit
            the unit of quantity
        """        
        self.value = value
        self.unit = unit
        
    def __repr__(self) -> str:
        return (
            '<Quantity object: %e %s at 0x%x>' 
            %(self.value*self.unit.relative_value, self.unit.base_dimension, id(self))
        )

    def __str__(self) -> str:
        return (
            '%e %s' %(self.value*self.unit.relative_value, self.unit.base_dimension)
        )

    def isDimensionLess(self):
        """
        isDimensionLess judges wether ``self`` is dimensionless

        Returns
        -------
        bool
            - True, the quantity is dimensionless
            - False, the quantity isn't dimensionless
        """      
        if self.unit.isDimensionLess():
            return True
        else:
            return False

    # If the unit is dimensionless, just return the absolute value
    def judgeAndReturn(self):
        """
        judgeAndReturn returns different value depends on the result of ``self.isDimensionLess()``

        Returns
        -------
        int or float or Quantity
            - If ``self.isDiemsionLess() == True``, return the ``self.value * self.unit.relative_value``
            - If ``self.isDiemsionLess() == False``, return ``deepcopy(self)``
        """        
        if self.isDimensionLess():
            return self.value * self.unit.relative_value
        else:
            return deepcopy(self)

    def convertTo(self, target_unit):
        """
        convertTo converts ``self`` to the unit of ``target_unit``

        Parameters
        ----------
        target_unit : Quantity
            the unit defined by openpd or users

        Returns
        -------
        Quantity
            Quantity with the same absolute value but new unit

        Raises
        ------
        ValueError
            If ``self.unit.base_dimension != target_unit.unit.base_dimension``. E.g ``(10*meter).convertTo(second)``
        """        
        if self.unit.base_dimension != target_unit.unit.base_dimension:
            raise UnitDimensionDismatchError(
                'Dimension %s and %s is different, can not convert'
                %(self.unit.base_dimension, target_unit.unit.base_dimension)
            )
        else:
            return self / target_unit * target_unit

    def __eq__(self, other) -> bool:
        if isinstance(other, Quantity):
            if self.unit == other.unit:
                if self.value == other.value:
                    return True
                else:
                    return False
            elif self.unit.base_dimension == other.unit.base_dimension:
                if isAlmostEqual(
                    self.value, 
                    other.value * other.unit.relative_value / self.unit.relative_value 
                ):
                    return True
                else:
                    return False
            else:
                return False
        # Value judgement, without relative value like 10*angstrom == 10
        else:
            if other == self.value:
                return True
            else:
                return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        if isinstance(other, Quantity):
            if self.unit.base_dimension != other.unit.base_dimension:
                raise UnitDimensionDismatchError(
                    'Dimension %s and %s is different, can not compare'
                    %(self.unit.base_dimension, other.unit.base_dimension)
                )
            else:
                return (
                    self.value * self.unit.relative_value <
                    other.value * other.unit.relative_value
                )
        else:
            return (self.value < other)

    def __le__(self, other) -> bool:
        if isinstance(other, Quantity):
            if self.unit.base_dimension != other.unit.base_dimension:
                raise UnitDimensionDismatchError(
                    'Dimension %s and %s is different, can not compare'
                    %(self.unit.base_dimension, other.unit.base_dimension)
                )
            else:
                return (
                    self.value * self.unit.relative_value <=
                    other.value * other.unit.relative_value
                )
        else:
            return (self.value <= other)
    
    def __gt__(self, other) -> bool:
        if isinstance(other, Quantity):
            if self.unit.base_dimension != other.unit.base_dimension:
                raise UnitDimensionDismatchError(
                    'Dimension %s and %s is different, can not compare'
                    %(self.unit.base_dimension, other.unit.base_dimension)
                )
            else:
                return (
                    self.value * self.unit.relative_value >
                    other.value * other.unit.relative_value
                )
        else:
            return (self.value > other)

    def __ge__(self, other) -> bool:
        if isinstance(other, Quantity):
            if self.unit.base_dimension != other.unit.base_dimension:
                raise UnitDimensionDismatchError(
                    'Dimension %s and %s is different, can not compare'
                    %(self.unit.base_dimension, other.unit.base_dimension)
                )
            else:
                return (
                    self.value * self.unit.relative_value >=
                    other.value * other.unit.relative_value
                )
        else:
            return (self.value >= other)

    def __add__(self, other):
        if isinstance(other, Quantity):
            return Quantity(
                self.value + other.value * (other.unit.relative_value / self.unit.relative_value) ,
                self.unit + other.unit # Test wether the base dimension is same Or the dimension will be changed in the next step
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(self+value)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                res.append(self+value)
            return np.array(res)
        else:
            return Quantity(
                self.value + other,
                self.unit
            ).judgeAndReturn()

    __iadd__ = __add__
    
    def __radd__(self, other):
        if isinstance(other, Quantity):
            return Quantity(
                other.value + self.value * (self.unit.relative_value / other.unit.relative_value) ,
                other.unit + self.unit
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(self+value)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                res.append(self+value)
            return np.array(res)
        else:
            return Quantity(
                self.value + other,
                self.unit
            ).judgeAndReturn()

    def __sub__(self, other):
        if isinstance(other, Quantity):
            return Quantity(
                self.value - other.value * (other.unit.relative_value / self.unit.relative_value) ,
                self.unit - other.unit
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(self - value)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                res.append(self - value)
            return np.array(res)
        else:
            return Quantity(
                self.value - other,
                self.unit
            ).judgeAndReturn()

    __isub__ = __sub__

    def __rsub__(self, other):
        if isinstance(other, Quantity):
            return Quantity(
                other.value - self.value * (self.unit.relative_value / other.unit.relative_value),
                other.unit - self.unit 
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(value - self)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                print(type(value))
                res.append(value - self)
            return np.array(res)
        else:
            return Quantity(
                other - self.value,
                self.unit
            ).judgeAndReturn()
            
    def __neg__(self):
        return Quantity(
            - self.value,
            self.unit
        ).judgeAndReturn()

    def __mul__(self, other):
        if isinstance(other, Quantity):
            return Quantity(
                self.value * other.value,
                self.unit * other.unit
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(self * value)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                res.append(self * value)
            return np.array(res)
        else:
            return Quantity(
                self.value * other,
                1 * self.unit
            ).judgeAndReturn()

    __imul__ = __mul__
    __rmul__ = __mul__
    
    def __truediv__(self, other):
        if isinstance(other, Quantity):
            if other.value == 0:
                raise DividingZeroError('Dividing 0: Nan')
            return Quantity(
                self.value / other.value,
                self.unit / other.unit
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(self/value)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                res.append(self/value)
            return np.array(res)
        else:
            if other == 0:
                raise DividingZeroError('Dividing 0: Nan')
            return Quantity(
                self.value / other,
                self.unit
            ).judgeAndReturn()

    __itruediv__ = __truediv__

    def __rtruediv__(self, other):
        if self.value == 0:
            raise DividingZeroError('Dividing 0: Nan')
        elif isinstance(other, Quantity):
            return Quantity(
                other.value / self.value,
                other.unit / self.unit
            ).judgeAndReturn()
        elif isinstance(other, list):
            res = []
            for value in other:
                res.append(value/self)
            return res
        elif isinstance(other, np.ndarray):
            res = []
            for value in other:
                res.append(value/self)
            return np.array(res)
        else:
            return Quantity(
                other / self.value,
                1 / self.unit
            ).judgeAndReturn()

    def __pow__(self, value):
        if isinstance(value, list) or isinstance(value, np.ndarray):
            raise ValueError('The power term should be a single number')
        return Quantity(
            self.value**value,
            self.unit**value
        ).judgeAndReturn()

    def sqrt(self):
        """
        sqrt returns square root of Quantity

        Returns
        -------
        Unit
            square root of ``self``
        """   
        return Quantity(
            sqrt(self.value),
            self.unit.sqrt()
        ).judgeAndReturn()

    def __abs__(self):
        return abs(self.value * self.unit.relative_value)