main_py_content = """
import data
import visualization

def main():
    financial_data = data.get_sample_data()
    visualization.plot_financial_data(financial_data)

if __name__ == "__main__":
    main()
"""


with open("/mnt/data/main.py", "w") as file:
    file.write(main_py_content)
