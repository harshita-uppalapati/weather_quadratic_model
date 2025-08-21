# Weather Prediction using Quadratic Formula (Hardcoded Values)

# Equation: T(t) = a*t^2 + b*t + c
a = 0.5
b = -3
c = 28
t = 5  # Example time input

T = a * (t ** 2) + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")