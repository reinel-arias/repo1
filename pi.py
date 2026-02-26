from decimal import Decimal, getcontext
from math import factorial

def ramanujan_pi(precision, max_terms=50):
    """
    Calcula pi usando la serie de Ramanujan con la librería decimal.
    precision: dígitos decimales deseados.
    max_terms: número máximo de términos a sumar (por seguridad).
    """
    # usar precisión extra durante el cálculo para minimizar errores de redondeo
    getcontext().prec = precision + 10

    one = Decimal(1)
    factor = (Decimal(2).sqrt() * Decimal(2)) / Decimal(9801)  # 2*sqrt(2)/9801
    total = Decimal(0)

    for k in range(max_terms):
        # términos con factoriales enteros (math.factorial devuelve int)
        num = Decimal(factorial(4 * k)) * (Decimal(1103) + Decimal(26390) * k)
        den = (Decimal(factorial(k)) ** 4) * (Decimal(396) ** (4 * k))
        term = num / den
        total += term
        # criterio de parada: término pequeño respecto a la precisión deseada
        if term < Decimal(10) ** (-(precision + 5)):
            break

    pi = one / (factor * total)

    # reducir a la precisión solicitada y devolver
    getcontext().prec = precision
    return +pi , k  # el operador + aplica el contexto actual (redondea)

# Ejemplo de uso
if __name__ == "__main__":
    print(ramanujan_pi(100))