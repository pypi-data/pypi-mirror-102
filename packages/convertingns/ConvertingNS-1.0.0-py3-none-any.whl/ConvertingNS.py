def Convert(number: [int, str], start: int, end: int) -> str:
    Alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def ToDecimal(x: [int, str], base: int) -> int:
        result = 0
        for degree, digit in enumerate(reversed(str(x))):
            index = int(Alphabet.index(digit))
            if index >= start:
                raise ValueError(f'invalid literal with base {start}: "{x}"')
            result += index * base ** degree
        return result

    def FromDecimal(x: int, base: int) -> str:
        if base == 1:
            return '1' * x
        result = ''
        while x != 0:
            result += Alphabet[x % base]
            x //= base
        return result[::-1]

    def Exceptions() -> Exception:
        if not (type(number) in (int, str) and type(start) == int and type(end) == int):
            raise TypeError
        if not (1 <= start <= len(Alphabet) and 1 <= end <= len(Alphabet)):
            raise ValueError

    def Main() -> str:
        Exceptions()
        decimal = ToDecimal(number, start)
        result = FromDecimal(decimal, end)
        return result

    return Main()
