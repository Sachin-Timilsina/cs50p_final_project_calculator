import pytest  # type: ignore
import math
from project import bmi_calculator
from project import calculator
from project import km_to_m, m_to_km, lb_to_kg, kg_to_lb, fahrenheit_to_celcius
from project import celcius_to_fahrenheit, feet_to_meter, meter_to_feet

def test_calculator():
    assert calculator('+', 10, 10) == 20
    assert calculator('-', 10, 10) == 0
    assert calculator('*', 10, 100) == 1000
    assert calculator('/', 10, 2) == 5
    assert calculator('%', 3, 2) == 1
    assert calculator('sin', 90, mode='d') == 1
    assert calculator('cos', 90, mode='d') == 0
    assert calculator('tan', 45, mode='d') == 1
    assert calculator('sin', 3, mode='r') == 0.141
    assert calculator('cos', 3, mode='r') == -0.990
    assert calculator('tan', 3, mode='r') == -0.143

def test_calculator_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert calculator('/', 0, 0)
    with pytest.raises(ZeroDivisionError):
        assert calculator('%', 4, 0)

def test_calculator_undefined_angles():
    with pytest.raises(ValueError):
        calculator('tan', first_num=90, mode='d')
    with pytest.raises(ValueError):
        calculator('tan', first_num=270, mode='d')
    with pytest.raises(ValueError):
        calculator('tan', first_num=math.pi/2, mode='r')
    with pytest.raises(ValueError):
        calculator('tan', first_num=math.pi + math.pi / 2, mode='r')

def test_bmi_calculator():
    assert bmi_calculator(20, 1.37) == [10.66, 'Underweight']
    assert bmi_calculator(90, 1.72) == [30.42, 'Obese']
    assert bmi_calculator(77, 1.82) == [23.25, 'Healthy weight']
    assert bmi_calculator(100, 1.22) == [67.19, 'Extremely obese']

def test_km_to_m():
    assert km_to_m(1) == 1000
    assert km_to_m(0) == 0

def test_m_to_km():
    assert m_to_km(1) == 0.001
    assert m_to_km(0) == 0

def test_feet_to_meter():
    assert feet_to_meter(1) == 0.30
    assert feet_to_meter(0) == 0

def test_meter_to_feet():
    assert meter_to_feet(1) == 3.28
    assert meter_to_feet(0) == 0

def test_fahrenheit_to_celcius():
    assert fahrenheit_to_celcius(1) == -17.22
    assert fahrenheit_to_celcius(0) == -17.78

def test_celcius_to_fahrenheit():
    assert celcius_to_fahrenheit(1) == 33.8
    assert celcius_to_fahrenheit(0) == 32

def test_lb_to_kg():
    assert lb_to_kg(2) == 0.91
    assert lb_to_kg(0) == 0

def test_kg_to_lb():
    assert kg_to_lb(3) == 6.61
    assert kg_to_lb(0) == 0