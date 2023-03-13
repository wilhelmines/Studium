def harmonic_series(n):
    """
    Berechnet die harmonische Reihe bis zum n-ten Glied und gibt die Zwischenergebnisse aus.
    """
    result = 0.0
    for i in range(1, n+1):
        result += 1.0/i
        print(f"Zwischenergebnis bei i={i}: {result}")
    return result