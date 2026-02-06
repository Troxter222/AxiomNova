import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from src.solvers.neural import SimpleMathLSTM, CHAR_TO_IDX, VOCAB_SIZE

def encode_str(text):
    return [CHAR_TO_IDX.get(c, 0) for c in text]

def train():
    print("Loading dataset...")
    df = pd.read_csv("data/math_dataset.csv")
    
    model = SimpleMathLSTM()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    print("Starting training (Neural Network is learning)...")
    epochs = 5
    
    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        
        # Проходим по всему датасету
        for _, row in df.iterrows():
            problem = row['src']
            answer = str(row['tgt'])
            
            # Подготовка данных
            input_tensor = torch.tensor(encode_str(problem)).unsqueeze(0) # (1, seq_len)
            
            # Мы учим сеть предсказывать ПОСЛЕДНЮЮ цифру (для упрощения сейчас)
            # Если ответ "15", мы пока учим "5". Полноценный seq2seq сложнее.
            # Для теста возьмем задачи где ответ 1 цифра (0-9).
            if len(answer) > 1: continue 
            
            target_tensor = torch.tensor([CHAR_TO_IDX.get(answer[0], 0)])
            
            # Forward
            optimizer.zero_grad()
            output = model(input_tensor)
            
            loss = criterion(output, target_tensor)
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            
            # Проверка
            pred = torch.argmax(output, dim=1).item()
            if pred == CHAR_TO_IDX.get(answer[0], 0):
                correct += 1
                
        print(f"Epoch {epoch+1}/{epochs} | Loss: {total_loss/len(df):.4f} | Accuracy: {correct} correct")

    # Сохраняем мозг
    torch.save(model.state_dict(), "data/axiom_brain.pth")
    print("✅ Model saved to data/axiom_brain.pth")

if __name__ == "__main__":
    train()