
# 3.2. Utilītu bibliotēka

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


def factor(n: int) -> int:
    """Aprēķina skaitļa n faktoriālu."""
    if n < 0:
        raise ValueError("Faktoriāls nav definēts negatīviem skaitļiem")
    if n == 0:
        return 1
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

# validacija.py

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
    """Pārbauda, vai parole ir vismaz 8 simboli un satur skaitli un burtu."""
    return (
        len(pwd) >= 8
        and any(ch.isdigit() for ch in pwd)
        and any(ch.isalpha() for ch in pwd)
    )

def is_valid_date(text: str) -> bool:
    """Pārbauda, vai datums ir formātā YYYY-MM-DD."""
    import datetime
    try:
        datetime.datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


"""
validators.py – Datu validācijas funkcijas.
"""

def validate_range(value: int, low: int, high: int) -> bool:
    """
    Validē, vai skaitlis atrodas intervālā [low, high].
    """
    return low <= value <= high


def validate_text_length(text: str, minimum: int = 1) -> bool:
    """
    Pārbauda, vai teksts nav tukšs un garāks par norādīto minimumu.
    """
    return len(text.strip()) >= minimum


def validate_int_input(value: str) -> bool:
    """
    Pārbauda, vai ievadītā vērtība ir vesels skaitlis.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
