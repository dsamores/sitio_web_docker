import time

def almacenar_item(text):
    # almacenar en base de datos
    time.sleep(3)

def num_words(text):
    almacenar_item(text)
    return len(text.split())

def num_characters(text):
    return len(text.strip())

def average_word_size(text):
    word_lengths = []
    for word in text.split():
        word_lengths.append(len(word))
    return sum(word_lengths) // len(word_lengths)

def text_analysis(text):
    try:
        promedio = average_word_size(text)
    except ZeroDivisionError:
        promedio = "indefinido"

    return (
        f"Texto: {text}"
        "<br>"
        f"El texto tiene {num_characters(text)} caracteres"
        "<br>"
        f"El texto tiene {num_words(text)} palabra{'' if num_words(text) == 1 else 's'}"
        "<br>"
        f"La longitud promedio de palabras es {promedio}"
    )
