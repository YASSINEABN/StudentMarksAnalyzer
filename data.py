import numpy as np
import pandas as pd

# Générer des données simulées
np.random.seed(42)
data = {
    "Nom": [f"Étudiant {i+1}" for i in range(100)],
    "Mathématiques": np.random.normal(12, 3, 100).clip(0, 20),
    "Physique": np.random.normal(14, 4, 100).clip(0, 20),
    "Chimie": np.random.normal(10, 2, 100).clip(0, 20),
}
df = pd.DataFrame(data)
df.to_csv("notes_etudiants.csv", index=False)

