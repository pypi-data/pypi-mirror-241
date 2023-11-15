class Calculator:
    @staticmethod
    def addition(*args):
        result = 0
        for num in args:
            result += num
        return result

    @staticmethod
    def soustraction(*args):
        result = args[0] if args else 0
        for num in args[1:]:
            result -= num
        return result

    @staticmethod
    def multiplication(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def division(*args):
        if not args:
            raise ValueError("Ou dwe gen omwen yon nonb pou divizyon")
        result = args[0]
        for num in args[1:]:
            if num != 0:
                result /= num
            else:
                raise ValueError("Ou pa ka divize pa zero")
        return result
