class Calculator1:

    @staticmethod
    def exponentielle(base, *exponents):
        result = base
        for exp in exponents:
            result **= exp
        return result

    @staticmethod
    def factorielle(n):
        """Kalkile faktoryèl yon nonb."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Faktoryèl sèlman defini pou nonb pozitif entye")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def square(*args):
        """Kalkile rasin kare yon nonb."""
        if not args:
            raise ValueError("Ou dwe gen omwen yon nonb pou kalkile rasin kare")
        resultats = [num ** 0.5 if num >= 0 else ValueError(f"Ou pa ka kalkile rasin kare nan yon nonb negatif: {num}") for num in args]
        return resultats[0] if len(resultats) == 1 else resultats
