#from get_names import get_names
from functions.find_figi import find_FIGI
from functions.get_history import get_history
#from token_1 import TOKEN
from to_decimal import process_quotation_data

def main(ticker):
    
    get_history(find_FIGI(ticker))
    
    process_quotation_data()

