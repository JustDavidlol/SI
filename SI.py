# main.py

def calculate_square_area(side_length):
    """
    Vypočítá plochu čtverce.

    Parametry:
    - side_length (float): Délka strany čtverce.

    vráti:
    - float: Plocha čtverce.
    """
    if side_length <= 0:
        raise ValueError("Délka strany musí být kladné číslo")
    
    area = side_length ** 2
    return area


def calculate_circle_area(radius):
    """
  Vypočítá obsah kruhu.

    Parametr:
    - radius (float): Poloměr kruhu.

    Vrátí:
    - float: Plocha kruhu.
    """
    from math import pi

    if radius <= 0:
        raise ValueError("Poloměr musí být kladné číslo")

    area = pi * (radius ** 2)
    return area



""""
    square_side = zadá se délka strany čtverce
    circle_radius = zadá se délka poloměru kruhu

"""




if __name__ == "__main__":
    square_side = 10
    circle_radius = 20

    square_area = calculate_square_area(square_side)
    circle_area = calculate_circle_area(circle_radius)

    print(f"Délka strany čtverce {square_side}: {square_area}")
    print(f"Poloměr plochy kruhu {circle_radius}: {circle_area}")
