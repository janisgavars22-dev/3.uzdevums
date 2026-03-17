
# 3.3. Validācijas bibliotēka

def is_valid_name(name: str) -> bool:
    """Pārbauda, vai vārds sākas ar lielo burtu un satur tikai burtus."""
    return name.isalpha() and name[0].isupper()


def is_phone_number(number: str) -> bool:
    """Pārbauda, vai telefona numurs atbilst Latvijas formātam +371xxxxxxxx."""
    return number.startswith("+371") and number[4:].isdigit() and len(number) == 12


def is_valid_age(age: int) -> bool:
    """Pārbauda, vai vecums ir 0–150."""
    return isinstance(age, int) and 0 <= age <= 150


def is_password_strong(pwd: str) -> bool:
    """Pārbauda, vai parole ir vismaz 8 simboli un satur skaitli."""
    return (
        len(pwd) >= 8
        and any(ch.isdigit() for ch in pwd)
        and any(ch.isalpha() for ch in pwd)
    )

# utili.py

def capitalize(text: str) -> str:
    """Pārveido pirmo burtu uz lielo."""
    return text.capitalize()

def truncate(text: str, max_len: int = 20) -> str:
    """Saīsina tekstu, ja tas ir garāks par max_len."""
    return text[:max_len] + ("..." if len(text) > max_len else "")

def count_words(text: str) -> int:
    """Saskaita vārdus tekstā."""
    return len(text.split())

def clamp(value: int, low: int, high: int) -> int:
    """Ierobežo vērtību intervālā [low, high]."""
    return max(low, min(value, high))

def is_prime(n: int) -> bool:
    """Nosaka, vai skaitlis ir pirmskaitlis."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    """Aprēķina skaitļa n faktoriālu."""
    if n < 0:
        raise ValueError("Faktoriāls negatīviem skaitļiem nav definēts")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def totals(numbers: list) -> int:
    """Atgriež saraksta elementu summu."""
    return sum(numbers)

def average(numbers: list) -> float:
    """Aprēķina saraksta vidējo lielumu."""
    return sum(numbers) / len(numbers)
``


def is_valid_date(text: str) -> bool:
    """Pārbauda, vai datums ir formātā YYYY-MM-DD."""
    import datetime
    try:
        datetime.datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

"""
utils.py – Palīgfunkcijas programmas dažādām daļām.
"""

import datetime

def get_current_time() -> str:
    """Atgriež tekošo laiku skaistā formātā."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def normalize_text(text: str) -> str:
    """Atgriež tekstu ar noņemtiem liekajiem atstarpēm un vienotā formā."""
    return text.strip().lower()


def is_number(value: str) -> bool:
    """Pārbauda, vai virkne ir pārvēršama par veselu skaitli."""
    try:
        int(value)
        return True
    except ValueError:
        return False
