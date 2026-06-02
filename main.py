import os
import logging
import pandas as pd
from sqlalchemy import create_engine
from src.transform import execute_transformations

# Initialize clean standard logging output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    source_path = "data/Restaurant_Reviews.tsv"
    target_db = "sqlite:///restaurant_analytics.db"
    target_table = "fact_restaurant_reviews"
    
    logging.info("--- Data Pipeline Execution Triggered ---")
    
    # PHASE 1: EXTRACT
    logging.info(f"Extracting source data from: {source_path}")
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Critical Error: Ingestion file target missing at {source_path}")
    df = pd.read_csv(source_path, sep='\t')
    
    # PHASE 2: TRANSFORM
    logging.info("Executing text normalization and injecting audit tracking columns...")
    transformed_df = execute_transformations(df)
    
    # PHASE 3: LOAD
    logging.info(f"Loading {len(transformed_df)} records to database table: {target_table}")
    engine = create_engine(target_db)
    
    # Append rows cleanly so the project scales seamlessly with multiple data batches
    transformed_df.to_sql(target_table, con=engine, if_exists='append', index=False)
    
    logging.info("--- Data Pipeline Successfully Completed Without Interruption ---")

if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        logging.error(f"Pipeline Execution Failed: {str(e)}")
