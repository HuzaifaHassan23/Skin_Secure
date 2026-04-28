# pandas ek library hai jo tabular data (Excel, CSV, etc.) ko read aur process karne ke liye use hoti hai.
import pandas as pd

# dataset ka metadata file (CSV format) ka path diya.
# ye file har image ka detail rakhti hai (jaise image id, disease label, age, gender, etc.).
csv_path = r"C:\Users\ITG LAB\Downloads\archive (1)\HAM10000_metadata.csv"

# CSV load karo
# CSV file ko load karke df (DataFrame) mai store kar liya.
# DataFrame ek table ki tarah hota hai (rows aur columns). 
df = pd.read_csv(csv_path)
# columns (matlab dataset ke fields jaise image_id, dx, age, etc.) print karta hai.
# df.head() → pehli 5 rows print karta hai taake sample data samajh aaye.
print("Metadata columns:", df.columns)
print("Sample rows:\n", df.head())


# ek sample row select ki (iloc[0] → pehli row).
# us row se image_id aur uski disease label (dx) print ki.
# matlab ek image ke saath uska label (ground truth) check karne ka example.

# ek image ka label nikalne ka example
sample = df.iloc[0]
print(f"Image: {sample['image_id']} | Disease: {sample['dx']}")


# "Ye code metadata file ko pandas ke through load karta hai, uske columns 
# aur sample rows print karta hai, aur ek image ke saath uska disease label
#  nikalne ka example deta hai. General purpose mai pandas data handling aur 
# analysis ke liye hoti hai. Humare Skin_Secure project mai ye isliye use hua 
# kyunki images ke saath labels (diseases) CSV file mai diye gaye hain, aur model
#  training ke liye hume images aur unke labels ko connect karna padta hai."