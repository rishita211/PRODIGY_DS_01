import zipfile
import os
import pandas as pd
import matplotlib.pyplot as plt

# === Your ZIP path ===
zip_path = r"C:\Users\RISHITA\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_38144.zip"
extract_dir = "population_data"

# === Extract the ZIP file ===
os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f"[✅] Extracted to {extract_dir}")

# === Find CSV file inside ===
csv_file = None
for file in os.listdir(extract_dir):
    if file.endswith(".csv") and "Metadata" not in file:
        csv_file = os.path.join(extract_dir, file)
        break

if not csv_file:
    raise Exception("❌ Could not find a valid population CSV inside the ZIP.")

# === Load the CSV into pandas ===
df = pd.read_csv(csv_file, skiprows=4)  # World Bank CSV has 4 header rows to skip

# === Clean and visualize ===
# Get population for 2022 and drop missing
df_pop = df[['Country Name', '2022']].dropna()
df_pop = df_pop.sort_values(by='2022', ascending=False).head(10)

# === Bar chart ===
plt.figure(figsize=(10, 6))
plt.barh(df_pop['Country Name'], df_pop['2022'], color='skyblue')
plt.xlabel('Population')
plt.title('Top 10 Most Populous Countries (2022)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
