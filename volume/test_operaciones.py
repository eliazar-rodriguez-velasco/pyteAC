import pytest
import operaciones as ar

orden = [5,3,4,2,1]
DC= [{"nombre":"francisco","edad":43},
    {"nombre":"armando","edad":5},
    {"nombre":"juan","edad":19}]

def testOr():
    assert ar.Ordenar(orden) == [1,2,3,4,5]

def testmayores():
    assert ar.Mayores(DC) == 2