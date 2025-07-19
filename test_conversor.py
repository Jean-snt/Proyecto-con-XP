from conversor import convertir

def test_celsius_a_fahrenheit():
    resultado = convertir(0, "C", "F")
    assert resultado == 32.0
