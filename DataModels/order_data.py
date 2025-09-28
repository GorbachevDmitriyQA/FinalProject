from dataclasses import dataclass

@dataclass
class OrderData:
    """Опция П-образная столешница"""
    p_example_option: bool
    """Толщина столешницы"""
    top_thickness: str
    """Опция Остров"""
    island_option: bool
    """Опция Плинтус"""
    plintus_option: bool
    """Опция Проточки для стока воды"""
    grooves_of_water_option: bool
    """Цвет столешницы"""
    top_color: str
    """Итоговая сумма заказа"""
    sum_price = ""