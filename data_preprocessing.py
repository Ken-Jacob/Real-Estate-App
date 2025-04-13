import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        logger.info("Data loaded successfully.")
        return df
    except Exception as e:
        logger.error("Error loading data", exc_info=True)
        raise e

def preprocess_data(df):
    try:
        df['property_age'] = df['year_sold'] - df['year_built']
        df.drop(['Address'], axis=1, errors='ignore', inplace=True)
        df = pd.get_dummies(df, drop_first=True)
        if 'price' in df.columns:
            cols = df.columns.tolist()
            cols.remove('price')
            df = df[cols + ['price']]
            
        logger.info("Preprocessing completed.")
        return df
    except Exception as e:
        logger.error("Preprocessing error", exc_info=True)
        raise e
