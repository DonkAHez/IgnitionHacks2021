# imports necessary packages
from torch import nn
import torch
import pandas
import torch.optim as optim
import numpy as np
import torch.nn.functional as F
device = torch.device('cpu')

# Creates Model class
class NeuralNetwork(nn.Module):
  def __init__(self):
    super(NeuralNetwork, self).__init__()
    self.l1 = nn.Linear(2, 10)
    self.l2 = nn.ReLU()
    self.l3 = nn.Linear(10, 1)

  def forward(self, x):
    output = self.l1(x)
    output = self.l2(output)
    output = F.sigmoid(self.l3(output))
    return output

# Creates function to train model
def train(model, x, y, optimizer, lossF):
  model.zero_grad()
  output = model(x)
  loss = lossF(output, y)
  loss.backward()
  optimizer.step()

  return loss, output

# Instantiates model and optimizer
model = NeuralNetwork()

# Initializes loss function and optimizer
lossF = nn.MSELoss()
optm = optim.Adam(model.parameters(), lr=0.01)

# Opens data file
file = open("flappy_learn.dat", "r")
on = True

# Initializes data lists
x_train = []
y_train = []

# Reads through data file and fills data lists
while(on):
  text = file.readline()
  if text == "":
    on = False
  else:

    # Fills data lists by splitting info
    info = text.split(" ")
    for i in range(len(info)):
      info[i] = float(info[i]) 
    
    # Adds splitted info to data lists
    x_train += [info[:2]]
    y_train += [[info[2]]]

# Changes data lists into tensors
x = torch.Tensor(x_train)
y = torch.tensor(y_train)

# Changes tensors into Float Tensors
x = x.type(torch.FloatTensor)
# x_test = x_test.type(torch.FloatTensor)
y = y.type(torch.FloatTensor)
# y_test = y_test.type(torch.FloatTensor)

# Trains model by looping through the data (Epochs)
for i in range(100):
  for j in range(len(x)):
    loss, predicitons = train(model, x[j], y[j], optm, lossF)
    print(loss)
    print(torch.round(predicitons))