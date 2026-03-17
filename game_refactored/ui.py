
def ask_for_number(prompt: str = "Ievadi skaitli (1–10): ", low: int = 1, high: int = 10) -> int:
    """Droši nolasa veselu skaitli noteiktā intervālā."""
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Skaitlim jābūt no {low} līdz {high}!")
        except ValueError:
            print("Ievadiet veselu skaitli!")

def show_result(result: str, secret: int) -> None:
    """Attēlo rezultātu atkarībā no pārbaudes iznākuma."""
    messages = {
        "correct": "Pareizi! Tu uzminēji!",
        "high":    "Par lielu!",
        "low":     "Par mazu!",
    }
    print(messages.get(result, "Nezināms rezultāts."))
    print(f"Noslēptais skaitlis bija: {secret}")
