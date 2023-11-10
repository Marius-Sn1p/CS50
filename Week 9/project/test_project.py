import pytest
import sys
from project import get_selection, get_validate_email, meal_selection, Breakfast_Meal

def mock_breakfast_recipe():
    return "mock breakfast recipe"

def test_get_selection(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_selection() == '1'

    monkeypatch.setattr('builtins.input', lambda _: "Option 1")
    assert get_selection() == '1'

    monkeypatch.setattr('builtins.input', lambda _: "1 meal")
    assert get_selection() == '1'

    monkeypatch.setattr('builtins.input', lambda _: "4")
    with pytest.raises(SystemExit):
        get_selection()

def test_get_validate_email(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "marius.skersys1@gmail.com")
    assert get_validate_email() == "marius.skersys1@gmail.com"

    monkeypatch.setattr('builtins.input', lambda _: "marius.skersys1@@gmail.com")
    with pytest.raises(SystemExit):
        get_validate_email()

def test_meal_selection(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "1")
    monkeypatch.setattr(Breakfast_Meal, 'get_recipe', mock_breakfast_recipe)
    assert meal_selection()=="mock breakfast recipe"

    monkeypatch.setattr('builtins.input', lambda _: "Option 1")
    monkeypatch.setattr(Breakfast_Meal, 'get_recipe', mock_breakfast_recipe)
    assert meal_selection()=="mock breakfast recipe"

    monkeypatch.setattr('builtins.input', lambda _: "Breakfast")
    monkeypatch.setattr(Breakfast_Meal, 'get_recipe', mock_breakfast_recipe)
    assert meal_selection()=="mock breakfast recipe"