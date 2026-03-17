
import random

def generate_secret(low: int = 1, high: int = 10) -> int:
    """Ģenerē noslēpto skaitli intervālā [low, high]."""
    return random.randint(low, high)

def check_guess(secret: int, guess: int) -> str:
    """
    Atgriež:
      - "correct", ja minējums precīzs
      - "high",    ja minējums par lielu
      - "low",     ja minējums par mazu
    """
    if guess == secret:
        return "correct"
    return "high" if guess > secret else "low"
