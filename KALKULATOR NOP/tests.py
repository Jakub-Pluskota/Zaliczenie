from logic import infix_to_rpn, evaluate_rpn

def test_logic():
    test_cases = [
        ("3 + 4", "3 4 +", 7),
        ("3 + 4 * 2", "3 4 2 * +", 11),
        ("(1 + 2) * 3", "1 2 + 3 *", 9),
        ("10 / (5 - 3)", "10 5 3 - /", 5),
        ("5 + (6 - 2) * 3", "5 6 2 - 3 * +", 17),
        ("8 / 4 / 2", "8 4 / 2 /", 1)
    ]
    for expr, expected_rpn, expected_result in test_cases:
        rpn = infix_to_rpn(expr)
        result = evaluate_rpn(rpn)
        rpn_str = ' '.join(rpn)
        if rpn_str != expected_rpn:
            raise AssertionError(f"Błąd ONP: {expr} => {rpn_str}, oczekiwano: {expected_rpn}")
        if abs(result - expected_result) > 1e-6:
            raise AssertionError(f"Błąd wyniku: {expr} => {result}, oczekiwano: {expected_result}")
    print("Wszystkie testy logiki przeszły pomyślnie.")