def d_flex(percentage: int, of: int) -> int:
    """Esta funcion se encarga de dividir la pantalla/componente padre entre el 100% del mismo

    Args:
        percentage (int): porcentaje requerido
        of (int): [description]
    """
    return int((percentage * of) / 100.0)

