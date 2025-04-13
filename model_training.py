from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from logger import get_logger

logger = get_logger(__name__)

def train_model(df):
    try:
        X = df.drop(['price'], axis=1)
        y = df['price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        logger.info("Model trained successfully.")
        return model
    except Exception as e:
        logger.error("Training error", exc_info=True)
        raise e
