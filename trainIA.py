from tensorflow import keras as K


def trainIA(train, test):
    model = K.Sequential()

    model.add(K.layers.Dense(784, activation='relu'))
    model.add(K.layers.Dropout(0.5))
    model.add(K.layers.Dense(128, activation='relu'))

    model.compile(loss='mse', optimizer='adam', metrics=[])
    model.fit(train[0], train[1], epochs=10, batch_size=1000, validation_split=0.2)

    loss = model.evaluate(test[0], test[1])
    print(f"loss: {loss:.5f}")
