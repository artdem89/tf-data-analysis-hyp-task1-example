import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.1
    counts = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    z_stat, p_value = proportions_ztest(counts, nobs, alternative = 'larger')
    
    return p_value < alpha # Ваш ответ, True или False
