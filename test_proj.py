import pytest
from app.calc import Calculator

class TestCalc:
 def setup(self):
    self.calc = Calculator

 def test_adding_success(self):
     assert self.calc.adding(self, 1 , 1)  == 2

 def test_adding_unsuccess(self):
     assert self.calc.adding(self, 1 , 1) == 3

 def test_zero_divchisla(self):
     with pytest.raises(ZeroDivisionError):
         self.calc.divchisla(self, 1 , 0)
 def test_multiply(self):
     assert self.calc.multiply(self, 1, 2 ) == 2

 def test_vichitnie(self):
     assert  self.calc.vichitnie(self, 4, 2 ) == 2

 def test_vstepen(self):
     assert self.calc.vstepen(self, 2 , 2) == 4

 def test_koren(self):
     assert self.calc.koren(self,4)==2

 def teardown(self):
     print('Выполнение метода teardown')