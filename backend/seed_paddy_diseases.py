import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "agriculture.db"

def seed_database():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # The 10 classes from the Paddy Doctor Dataset
    diseases = [
        {
            "disease_name": "bacterial_leaf_blight",
            "medicine": "Copper Hydroxide 50% WP",
            "medicine_secondary": "Streptomycin Sulfate",
            "dosage": "500g per acre",
            "timeline": "Apply immediately upon symptoms, repeat after 10 days",
            "preventive_measures": "Avoid excessive nitrogen, ensure proper field drainage"
        },
        {
            "disease_name": "bacterial_leaf_streak",
            "medicine": "Copper Oxychloride",
            "medicine_secondary": "Agrimycin",
            "dosage": "400g per acre",
            "timeline": "Spray at early infection stage, repeat at 7-day intervals",
            "preventive_measures": "Use resistant varieties, manage water effectively"
        },
        {
            "disease_name": "bacterial_panicle_blight",
            "medicine": "Oxolinic Acid",
            "medicine_secondary": "Kasugamycin",
            "dosage": "300ml per acre",
            "timeline": "Apply at heading stage",
            "preventive_measures": "Avoid late planting, balanced fertilizer application"
        },
        {
            "disease_name": "blast",
            "medicine": "Tricyclazole 75% WP",
            "medicine_secondary": "Isoprothiolane 40% EC",
            "dosage": "120g per acre",
            "timeline": "Spray immediately upon spotting diamond-shaped lesions",
            "preventive_measures": "Burn infected crop residues, avoid dense planting"
        },
        {
            "disease_name": "brown_spot",
            "medicine": "Mancozeb 75% WP",
            "medicine_secondary": "Propiconazole 25% EC",
            "dosage": "400g per acre",
            "timeline": "Apply at tillering and panicle emergence stages",
            "preventive_measures": "Ensure adequate soil nutrition, especially Silicon and Potassium"
        },
        {
            "disease_name": "dead_heart",
            "medicine": "Cartap Hydrochloride 4% GR",
            "medicine_secondary": "Chlorantraniliprole",
            "dosage": "7.5kg per acre",
            "timeline": "Apply granules in standing water at early tillering",
            "preventive_measures": "Install pheromone traps, clip seedling tips before transplanting"
        },
        {
            "disease_name": "downy_mildew",
            "medicine": "Metalaxyl + Mancozeb",
            "medicine_secondary": "Azoxystrobin",
            "dosage": "250g per acre",
            "timeline": "Apply when whitish fungal growth appears",
            "preventive_measures": "Ensure good drainage, avoid prolonged flooding in nurseries"
        },
        {
            "disease_name": "hispa",
            "medicine": "Chlorpyrifos 20% EC",
            "medicine_secondary": "Quinalphos 25% EC",
            "dosage": "500ml per acre",
            "timeline": "Spray when 1-2 adults per hill are seen",
            "preventive_measures": "Keep bunds clean, sweep nets for adult collection"
        },
        {
            "disease_name": "normal", # Healthy
            "medicine": "None",
            "medicine_secondary": "None",
            "dosage": "N/A",
            "timeline": "Routine monitoring",
            "preventive_measures": "Maintain standard nutrient and water management"
        },
        {
            "disease_name": "tungro",
            "medicine": "Imidacloprid 17.8% SL",
            "medicine_secondary": "Thiamethoxam 25% WG",
            "dosage": "50ml per acre",
            "timeline": "Vector control: Spray immediately if green leafhoppers are observed",
            "preventive_measures": "Destroy infected plants, synchronize planting in the area"
        }
    ]

    print("Seeding kb_diseases...")
    for d in diseases:
        cur.execute("""
            INSERT INTO kb_diseases (disease_name, medicine, medicine_secondary, dosage, timeline, preventive_measures)
            SELECT ?, ?, ?, ?, ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM kb_diseases WHERE disease_name = ?)
        """, (d["disease_name"], d["medicine"], d["medicine_secondary"], d["dosage"], d["timeline"], d["preventive_measures"], d["disease_name"]))
    
    # Prices for the medicines
    prices = [
        {"med": "Copper Hydroxide 50% WP", "brand": "Kocide", "price": 450, "unit": "kg"},
        {"med": "Streptomycin Sulfate", "brand": "Plantomycin", "price": 120, "unit": "kg"},
        {"med": "Copper Oxychloride", "brand": "Blitox", "price": 380, "unit": "kg"},
        {"med": "Agrimycin", "brand": "Agrimycin-17", "price": 150, "unit": "kg"},
        {"med": "Oxolinic Acid", "brand": "Starner", "price": 850, "unit": "liter"},
        {"med": "Kasugamycin", "brand": "Kasu-B", "price": 400, "unit": "liter"},
        {"med": "Tricyclazole 75% WP", "brand": "Baan", "price": 600, "unit": "kg"},
        {"med": "Isoprothiolane 40% EC", "brand": "Fuji-One", "price": 550, "unit": "liter"},
        {"med": "Mancozeb 75% WP", "brand": "Dithane M-45", "price": 350, "unit": "kg"},
        {"med": "Propiconazole 25% EC", "brand": "Tilt", "price": 900, "unit": "liter"},
        {"med": "Cartap Hydrochloride 4% GR", "brand": "Padan", "price": 80, "unit": "kg"},
        {"med": "Chlorantraniliprole", "brand": "Coragen", "price": 1800, "unit": "liter"},
        {"med": "Metalaxyl + Mancozeb", "brand": "Ridomil Gold", "price": 1200, "unit": "kg"},
        {"med": "Azoxystrobin", "brand": "Amistar", "price": 2500, "unit": "liter"},
        {"med": "Chlorpyrifos 20% EC", "brand": "Dursban", "price": 450, "unit": "liter"},
        {"med": "Quinalphos 25% EC", "brand": "Ekalux", "price": 500, "unit": "liter"},
        {"med": "Imidacloprid 17.8% SL", "brand": "Confidor", "price": 1200, "unit": "liter"},
        {"med": "Thiamethoxam 25% WG", "brand": "Actara", "price": 1500, "unit": "kg"},
    ]
    
    print("Seeding medicine_prices...")
    for p in prices:
        # Match with a disease to fill disease_name
        d_name = next((d["disease_name"] for d in diseases if d["medicine"] == p["med"] or d["medicine_secondary"] == p["med"]), "Unknown")
        
        cur.execute("""
            INSERT INTO medicine_prices (medicine_name, brand_name, unit_price, unit, disease_name)
            SELECT ?, ?, ?, ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM medicine_prices WHERE medicine_name = ?)
        """, (p["med"], p["brand"], p["price"], p["unit"], d_name, p["med"]))

    conn.commit()
    conn.close()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
