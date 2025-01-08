import torch.optim as optim
import torch.nn as nn
from data_loader import trainloader
from model import mlp

# Définition du device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
mlp.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(mlp.parameters(), lr=0.05, momentum=0.9)

def train():
    for epoch in range(5):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            # Envoie des données au device
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = mlp(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 20 == 19:
                print(f"[Epoch {epoch + 1}, Iteration {i + 1}] Loss: {running_loss / 20:.3f}")
                running_loss = 0.0

    print("Entraînement terminé.")

if __name__ == "__main__":
    train()
