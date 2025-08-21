# Weather Prediction using Quadratic Formula (Keyboard Input)

# Equation: T(t) = a*t^2 + b*t + c

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hour/day): "))

T = a * (t ** 2) + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")