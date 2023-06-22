
import chess_data as c

import torch
from torch import nn # nn contains all of PyTorch's building blocks for neural networks
import matplotlib.pyplot as plt

# Check PyTorch version
print(torch.__version__)




#make data
X = []
Y = []



def normalize_table(table):
    x = 0
    for i in range(len(table)): #dla kazdego wiersza
        if len(table[i]) > x:
            x = len(table[i])
    
    for i in range(len(table)):
        while len(table[i]) < x:
            table[i].append(0)
    return x, table


for item in c.data:
    X.append(item[0])
    Y.append(item[1])
#print(x)
#print(y)

x, X = normalize_table(X)

#print(X[:10])

X = torch.tensor(X)


#make Y tensor

for i in range(len(Y)):
    Y[i] = [Y[i]]
Y = torch.tensor(Y)

print("===========")
#print(X[:10])
print("===========")
#print(Y[:10])


#split data

X_train = X[:int(len(X)*0.8)]
X_test = X[int(len(X)*0.8):]

Y_train = Y[:int(len(Y)*0.8)]
Y_test = Y[int(len(Y)*0.8):]

print("===========")
print( len (X_train))
print( len (X_test))
print( len (Y_train))
print( len (Y_test))

#make model

#the model will be a simple linear regression model

model = nn.Linear(x, 1)

print(model)

#loss function adam

loss_function = nn.MSELoss()

#optimizer

optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

#train

epochs = 1000

for epoch in range(epochs):
    Y_pred = model(X_train)
    loss = loss_function(Y_pred, Y_train)
    print('Epoch {}: train loss: {}'.format(epoch, loss.item()))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


    #test

    Y_pred = model(X_test)
    loss = loss_function(Y_pred, Y_test)
    print('Test loss: {}'.format(loss.item()))

#save model

#torch.save(model.state_dict(), 'model.pth')


while True:
    print("===========")

    #string = "david piotrowski"

    string = input("Enter name: ")

    #make string 31 long


    #make string into tensor using tokens


    tok_arr = []

    for char in string:
        for i in range(0, len(c.letter_tokens)):
            if  char == c.letter_tokens[i] and len(tok_arr) < 31:
                tok_arr.append(i/100)


    while len(tok_arr) < 31:
        tok_arr.append(0)

    print(tok_arr)

    print("===========")

    prediction = model(torch.tensor(tok_arr))

    prediction = prediction*10000
    #print(prediction[0])
    print("predicted chess elo: " + str(prediction[0].item()))
