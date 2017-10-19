from fractions import Fraction

def get_fraction():
    while True:
        fraction = input().split('/')
        num      = int(fraction[0])
        den      = int(fraction[1])

        if den >= num:
            return Fraction(num,den)

def format_fractions(fractions):
    formatted_fractions = []

    for divisor in fractions:
        formatted_fractions.append("1/"+str(divisor))

    return formatted_fractions

def egyptian():
    fraction           = get_fraction()
    egyptian_fractions = []
    divisor            = 1

    while fraction != 0:
        unit_fraction = Fraction(1,divisor)

        # A primeira fração unitária menor ou igual à outra fração
        if unit_fraction <= fraction:
            egyptian_fractions.append(divisor)
            fraction = fraction - unit_fraction
            
        divisor = divisor + 1

    return format_fractions(egyptian_fractions)
