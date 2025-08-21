# Weather Prediction using Quadratic Formula (File Input - Multiple Sets)

# Reads multiple sets of a, b, c, t from inputs_multiple.txt
with open("inputs_multiple.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = a * (t ** 2) + b * t + c
        print(f"a={a}, b={b}, c={c}, t={t} -> Predicted Temp: {T:.2f}°C")