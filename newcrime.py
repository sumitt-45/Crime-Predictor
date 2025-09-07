import pandas as pd
import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt

# =========================
# 1. Load dataset
# =========================
file_path = "Cleaned Crime Data Set.csv.xlsx"  # change path if needed
data = pd.read_excel(file_path)

# =========================
# 2. Count crimes per city
# =========================
city_counts = data["City"].value_counts().reset_index()
city_counts.columns = ["City", "Crime Count"]

# =========================
# 3. Assign coordinates for cities (central lat/lon)
# =========================
city_coords = {
    "Ahmedabad": [23.0225, 72.5714],
    "Chennai": [13.0827, 80.2707],
    "Ludhiana": [30.9010, 75.8573],
    "Pune": [18.5204, 73.8567],
    "Mumbai": [19.0760, 72.8777],
    "Delhi": [28.7041, 77.1025],
    "Bhopal": [23.2599, 77.4126],
    "Kolkata": [22.5726, 88.3639],
    # ➡️ Add more if dataset has other cities
}

# =========================
# 4. Create City-Level Heatmap
# =========================
m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)  # India center

heat_data = []
for _, row in city_counts.iterrows():
    city = row["City"]
    if city in city_coords:  # only plot known cities
        lat, lon = city_coords[city]
        heat_data.append([lat, lon, row["Crime Count"]])  # intensity = crime count

HeatMap(heat_data, radius=25).add_to(m)

# Save interactive map
m.save("city_level_crime_heatmap.html")
print("✅ Heatmap saved as 'city_level_crime_heatmap.html'")

# =========================
# 5. Crime Category Distribution (Pie Chart)
# =========================
plt.figure(figsize=(7,7))
data["Crime Domain"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Crime Category Distribution")
plt.ylabel("")
plt.show()
