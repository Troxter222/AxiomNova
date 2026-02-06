import random
import csv
import os

def generate_sample():
    # Простейшая арифметика для старта: a + b
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    op = random.choice(['+', '-'])
    problem = f"{a}{op}{b}"
    return problem, str(eval(problem))

def main():
    if not os.path.exists("data"):
        os.makedirs("data")
        
    filename = "data/math_dataset.csv"
    print(f"Generating dataset -> {filename}")
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["src", "tgt"]) # Source (задача), Target (ответ)
        
        for _ in range(10000): # 10 тысяч примеров!
            p, s = generate_sample()
            writer.writerow([p, s])
            
    print("Done!")

if __name__ == "__main__":
    main()