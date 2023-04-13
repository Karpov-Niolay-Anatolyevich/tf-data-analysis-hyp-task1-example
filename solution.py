import pandas as pd
import numpy as np
from scipy.stats import kruskal

chat_id = 1135291357 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array , y:np.array) -> bool:
    alpha = 0.09
    test_stat, p_value = kruskal(x, y)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return p_value < alpha # Ваш ответ, True или False
