import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1135291357 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.07
    p_value = ttest_ind(x, y, alternative="greater").pvalue
    return p_value < alpha # Ваш ответ, True или False
