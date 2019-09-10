#!/usr/bin/env python3
from fetch import download_stocks
from predict import predict_on_stocks

COMPANIES_PATH = "../assets/companies.csv"
TEST_COMPANIES_PATH = "../assets/companies_test.csv"
PROXIES_PATH = "../assets/proxy_list.txt"
PREDICTIONS_PATH = "./predictions"
MODELS_PATH = "./models"
STOCKS_PATH = "./stocks"
RESULT_PATH = "/tmp"

if __name__ == "__main__":
    download_stocks(TEST_COMPANIES_PATH, STOCKS_PATH, max_dl=100)
    predict_on_stocks(STOCKS_PATH, PREDICTIONS_PATH, MODELS_PATH)
    # create_results(STOCKS_PATH, PREDICTIONS_PATH, RESULT_PATH)
