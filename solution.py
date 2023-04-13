import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 1135291357 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.09 
    n=len(x)
    mu = 500
    t_stat=(x.mean()-mu) / (x.std() /(n**0.5))
    crit_val=t.ppf(1-alpha, n-1)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return t_stat > crit_val # Ваш ответ, True или False
