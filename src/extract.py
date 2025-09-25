import pandas as pd
pd.set_option("display.max.rows", None)
pd.set_option("display.max.columns", None)
pd.set_option("display.width", None)
def extract_students(file_name):
    print("Extracting students...")

    df = pd.read_csv(r"../data/raw/" + file_name, sep=";")
    return df
if __name__ == "__main__":
    df =  extract_students("students.csv")
    print(df)
