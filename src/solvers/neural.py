import torch
import torch.nn as nn
from src.core.base_solver import BaseSolver

# Словарь символов (Vocabulary)
CHARS = "0123456789+-=xy "
CHAR_TO_IDX = {c: i for i, c in enumerate(CHARS)}
IDX_TO_CHAR = {i: c for i, c in enumerate(CHARS)}
VOCAB_SIZE = len(CHARS)

class SimpleMathLSTM(nn.Module):
    def __init__(self, hidden_size=128):
        super(SimpleMathLSTM, self).__init__()
        self.embedding = nn.Embedding(VOCAB_SIZE, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, VOCAB_SIZE) # Предсказываем следующий символ или класс

    def forward(self, x):
        # x shape: (batch, seq_len)
        embedded = self.embedding(x)
        output, (hidden, cell) = self.lstm(embedded)
        # Берем последнее состояние LSTM (мы хотим ответ после прочтения всей строки)
        last_output = output[:, -1, :] 
        prediction = self.fc(last_output)
        return prediction

class NeuralSolver(BaseSolver):
    """
    Решатель на основе PyTorch.
    Пытается "интуитивно" решить задачу.
    """
    def __init__(self, model_path=None):
        self.model = SimpleMathLSTM()
        self.model.eval() # Режим предсказания
        if model_path:
            try:
                self.model.load_state_dict(torch.load(model_path))
                print(f"Loaded Neural Model from {model_path}")
            except:
                print("Warning: Model weights not found. Using random brain.")

    def get_solver_type(self) -> str:
        return "DeepLearning (PyTorch LSTM)"

    def _encode(self, text):
        # Превращает строку "2+2" в тензор [2, 10, 2]
        idxs = [CHAR_TO_IDX.get(c, 0) for c in text]
        return torch.tensor(idxs).unsqueeze(0) # Добавляем batch dimension

    def solve(self, problem: str) -> str:
        # Для простоты этот пример пока настроен на предсказание одной цифры
        # В будущем мы расширим это до Seq2Seq (генерации длинного ответа)
        tensor_in = self._encode(problem)
        with torch.no_grad():
            output = self.model(tensor_in)
            predicted_idx = torch.argmax(output, dim=1).item()
            return IDX_TO_CHAR.get(predicted_idx, "?")