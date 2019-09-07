import os

EPOCHS = 1
LOOKBACK = 5
PREDICT = 5

def predict_on_stocks(stocks_path: str, store_path: str) -> None:
    ''' Arguments:
            - stocks_path:
                Path of where the stocks are stored
            - store_path:
                Path of where to store the predictions
    '''
    
    for file in os.listdir(stocks_path):
        if file.endswith('.json'):
            # 
            continue

    # Generate a prediction (cf wiki Irma) in store_path
    
    ## Model:
    #   faire la moyene de open high low close -> [mean, volumes]
