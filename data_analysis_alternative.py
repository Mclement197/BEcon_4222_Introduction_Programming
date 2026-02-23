"""
Economic Data Analysis
======================
Calculate key economic indicators from survey data
"""

# Survey data (responses in thousands)
employed = 58_500
unemployed = 3_250
not_in_labor_force = 38_250

# TODO: Calculate unemployment rate (percentage)
# Formula: (unemployed / labor_force) * 100
# where labor_force = employed + unemployed
unemployment_rate = None

# TODO: Calculate employment-to-population ratio (percentage)
# Formula: (employed / population) * 100
# where population = employed + unemployed + not_in_labor_force
employment_ratio = None

# Display results
if unemployment_rate is not None:
    print(f"Unemployment Rate: {unemployment_rate:.1f}%")
else:
    print("Unemployment Rate: Not calculated yet")

if employment_ratio is not None:
    print(f"Employment-to-Population Ratio: {employment_ratio:.1f}%")
else:
    print("Employment-to-Population Ratio: Not calculated yet")
