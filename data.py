data_py_content = """
import pandas as pd
import numpy as np

def get_sample_data():
    np.random.seed(42)
    dates = pd.date_range("20230101", periods=100)
    prices = np.random.randn(100).cumsum() + 50  # kumulatif rastgele fiyat hareketleri
    data = pd.DataFrame(prices, index=dates, columns=["Price"])
    return data
"""

with open("/mnt/data/data.py", "w") as file:
    file.write(data_py_content)
