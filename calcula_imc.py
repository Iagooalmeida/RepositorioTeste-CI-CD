def calculate_bmi(weight, height):
    if height <= 0:
        return "Height must be greater than zero"
    # Erro proposital: fórmula incorreta
    return weight / height

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()