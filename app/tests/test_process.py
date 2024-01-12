from app.process import text_analysis, num_characters, num_words, average_word_size
import pytest

from unittest.mock import patch

def test_text_analysis():
    with patch("app.process.almacenar_item"):
        assert text_analysis("texto") == (
            f"Texto: texto"
            "<br>"
            "El texto tiene 5 caracteres"
            "<br>"
            "El texto tiene 1 palabra"
            "<br>"
            "La longitud promedio de palabras es 5"
        )

def test_text_analysis_empty():
    with patch("app.process.almacenar_item"):
        assert text_analysis("") == (
            f"Texto: "
            "<br>"
            "El texto tiene 0 caracteres"
            "<br>"
            "El texto tiene 0 palabras"
            "<br>"
            "La longitud promedio de palabras es indefinido"
        )

@pytest.mark.parametrize(
    "texto,esperado",
    [
        ("texto", 5),
        ("texto a analizar", 16),
        ("", 0),
        ("prueba con varias palabras y mas largo", 38),
        ("   texto    ", 5),
        ("con un espacio despues ", 22),
        (" con un espacio antes", 20),
    ]
)
def test_num_characters(texto, esperado):
    assert num_characters(texto) == esperado

@pytest.mark.parametrize(
    "texto,esperado",
    [
        ("texto", 1),
        ("texto a analizar", 3),
        ("", 0),
        ("prueba con varias palabras y mas largo", 7),
        ("   texto    ", 1),
        ("con un espacio despues ", 4),
        (" con un espacio antes", 4),
        ("   con  espacios    entre    palabras   ", 4),
    ]
)
def test_num_words(texto, esperado):
    with patch("app.process.almacenar_item"):
        assert num_words(texto) == esperado

def test_average_word_size_zero():
    with pytest.raises(ZeroDivisionError):
        average_word_size("")
