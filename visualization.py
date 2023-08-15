visualization_py_content = """
import matplotlib.pyplot as plt

def plot_financial_data(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['Price'], label='Price', color='blue')
    plt.title('Finansal Veri Grafiği')
    plt.xlabel('Tarih')
    plt.ylabel('Fiyat')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
"""


with open("/mnt/data/visualization.py", "w") as file:
    file.write(visualization_py_content)
