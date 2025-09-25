import pandas as pd
import extract as e
df = e.extract_students("students.csv")
df.rename(columns={"NOME": "first_name",
                   "Unnamed: 1": "last_name",
                   "compleanno": "date_of_birth",
                   "Carta": "badge",
                   "N": "number",
                   "fratelli": "relatives",
                   "Data": "issuing",
                   "Data.1": "expiration"}, inplace=True)

df.drop(columns=["Unnamed: 7","Unnamed: 8", "Unnamed: 9"], inplace=True)
# inplace=True   it means the changed that we made will remain permenent
# ^A-Za-z    all character that are not alpabates  capital or lower letter  and we replace them with nothing
df.replace({"first_name": r"[^A-Za-z ]"}, "", regex=True, inplace=True)
df.replace({"last_name": {r"[^A-Za-z\s]": ""}}, regex=True, inplace=True)

# df["date_of_birth"] = pd.to_datetime(df["date_of_birth"]).dt.strftime("%m-%d-%Y")
# df["issuing"] = pd.to_datetime(df["issuing"]).dt.strftime("%m-%d-%Y")

df["expiration"] = (df["issuing"].str[:4].astype(int) + 4).astype(str) + df["date_of_birth"].str[4:]
df.fillna({"relatives": "-1"}, inplace=True)
df["relatives"] = df["relatives"].apply(lambda x: str(x).replace(",", "."))
df["relatives"] = df["relatives"].apply(lambda x: int(float(x)))
df = df.astype({"relatives": int})
df.to_csv(r"../data/processed/students_cleaned.csv", encoding="utf-8", index_label = "id")



print(df)
