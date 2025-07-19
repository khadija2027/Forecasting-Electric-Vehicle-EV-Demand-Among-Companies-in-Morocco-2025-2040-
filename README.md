# 📈 Forecasting Electric Vehicle (EV) Demand Among Companies in Morocco (2025–2040)

This Python script estimates and visualizes the **projected demand for electric vehicles (EVs)** among companies in **Morocco** over a 15-year horizon, under different adoption scenarios. It helps simulate the impact of public and private initiatives to accelerate EV penetration in the corporate sector.

---

## 🚀 Objective

To simulate the adoption of EVs by companies in **Morocco** from **2025 to 2040**, based on eligibility criteria, average fleet sizes, and varying maximum adoption rates across three strategic scenarios.

---

## 🧮 Model Description

The simulation is based on three core scenarios:

1. **Scenario 1:** Large Enterprises (GE) adopting EVs under Corporate Social Responsibility (RSE) goals – **5% fleet conversion**.
2. **Scenario 2:** More ambitious target for GEs – **10% fleet conversion**.
3. **Scenario 3:** Combination of:
   - Large Enterprises converting **20%** of their fleet
   - **11% of SMEs** (with >100 employees and aided financially) converting **5%**

A **logistic growth function** models how adoption increases over time, reflecting gradual market maturity.

---

## 📍 Context: Moroccan Market Assumptions

- `N_ent`: **500,000** total companies in Morocco
- `V_moy_1`: Average of **200 vehicles** per large company
- `V_moy_3`: Average of **10 vehicles** per eligible SME
- `P_max`: Maximum adoption levels (5%, 10%, 20%)
- `k`: Growth rate (**0.75**)
- `t_0`: Inflection year of logistic curve (**2035**)

---

## 📊 Projected Demand Calculation

Using the `adoption()` function, EV demand is calculated yearly from **2025 to 2040** for each scenario.

```python
def adoption(t, P_max, t_0, k):
    return P_max / (1 + np.exp(-k * (t - t_0)))
