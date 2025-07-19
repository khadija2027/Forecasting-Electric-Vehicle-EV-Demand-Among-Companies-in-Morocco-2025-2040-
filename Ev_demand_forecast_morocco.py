import numpy as np
import matplotlib.pyplot as plt

# Hypothèses
N_ent = 500000  # Nombre total d'entreprises
V_moy_1 = 200   # Nombre moyen de véhicules par entreprise (Scénario 1)
V_moy_3 = 10    # Nombre moyen de véhicules par entreprise (Scénario 3)

# Paramètres pour la courbe logistique
P_max_1 = 0.05  # Maximum d'adoption (5%)
P_max_2 = 0.1   # Maximum d'adoption (10%)
P_max_3 = 0.2   # Maximum d'adoption (20%)
P_max_4 = 0.05  # Maximum d'adoption (5%)
k = 0.75        # Taux de croissance de l'adoption
t_0 = 2035      # Début de la simulation (année)

# Définir la fonction de la courbe logistique pour l'adoption
def adoption(t, P_max, t_0, k):
    return P_max / (1 + np.exp(-k * (t - t_0)))

# Scénario 1: RSE/client
P_eligibles_1 = 0.01
# Scénario 3: RSE + >100 employés + Aides financières
P_eligibles_3 = 0.11  # 11% des entreprises

# Calcul de la demande pour chaque scénario
years = np.arange(2025, 2041, 1)  # Années de 2025 à 2040
demand_1 = N_ent * P_eligibles_1 * adoption(years, P_max_1, t_0, k) * V_moy_1
demand_2 = N_ent * P_eligibles_1 * adoption(years, P_max_2, t_0, k) * V_moy_1
demand_3 = (N_ent * P_eligibles_1 * adoption(years, P_max_3, t_0, k) * V_moy_1 +
            N_ent * P_eligibles_3 * adoption(years, P_max_4, t_0, k) * V_moy_3)

# Affichage des résultats
plt.figure(figsize=(12, 6))
plt.plot(years, demand_1, label='Scénario 1 : 5% de la flotte des GE', color='blue', linewidth=2)
plt.plot(years, demand_2, label='Scénario 2 : 10% de la flotte des GE', color='orange', linewidth=2)
plt.plot(years, demand_3, label='Scénario 3 : 20% de la flotte des GE et 5% de PME', color='green', linewidth=2)

# Ajouter les annotations avec un fond blanc pour améliorer la lisibilité
colors = ['blue', 'orange', 'green']
demands = [demand_1, demand_2, demand_3]

for demand, color in zip(demands, colors):
    for i, year in enumerate(years):
        plt.text(year, demand[i] * 1.05, f'{int(demand[i]):,}',
                 ha='center', va='bottom', fontsize=10, color=color,
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Ajout des titres et labels
plt.title('Demande prévisionnelle de VE par les entreprises (2025-2040)', fontsize=14, fontweight='bold')
plt.xlabel('Année', fontsize=12)
plt.ylabel('Demande prévisionnelle de VE (nombre de véhicules)', fontsize=12)
plt.legend(fontsize=10)
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Affichage du graphique
plt.show()
