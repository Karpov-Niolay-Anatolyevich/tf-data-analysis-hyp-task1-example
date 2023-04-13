import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 1135291357 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    successes = np.array([x_success, y_success])
    trails = np.array([x_cnt, y_cnt])
    z_value, p_value = proportions_ztest(successes, trails, alternative='larger')
    alpha = 0.07
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return p_value < alpha # Ваш ответ, True или False

  
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
