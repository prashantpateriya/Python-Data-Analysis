"""
Data loading utilities for the Python Data Analysis project.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_csv(file_path, **kwargs):
    """
    Load CSV file into pandas DataFrame.
    
    Args:
        file_path (str): Path to CSV file
        **kwargs: Additional arguments for pd.read_csv()
    
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_csv(file_path, **kwargs)
        logger.info(f"Successfully loaded CSV: {file_path} ({len(df)} rows)")
        return df
    except Exception as e:
        logger.error(f"Error loading CSV {file_path}: {e}")
        raise


def load_excel(file_path, sheet_name=None, **kwargs):
    """
    Load Excel file into pandas DataFrame.
    
    Args:
        file_path (str): Path to Excel file
        sheet_name (str): Sheet name (None for first sheet)
        **kwargs: Additional arguments for pd.read_excel()
    
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, **kwargs)
        logger.info(f"Successfully loaded Excel: {file_path} ({len(df)} rows)")
        return df
    except Exception as e:
        logger.error(f"Error loading Excel {file_path}: {e}")
        raise


def load_json(file_path, **kwargs):
    """
    Load JSON file into pandas DataFrame.
    
    Args:
        file_path (str): Path to JSON file
        **kwargs: Additional arguments for pd.read_json()
    
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_json(file_path, **kwargs)
        logger.info(f"Successfully loaded JSON: {file_path} ({len(df)} rows)")
        return df
    except Exception as e:
        logger.error(f"Error loading JSON {file_path}: {e}")
        raise


def save_dataframe(df, file_path, format='csv', **kwargs):
    """
    Save DataFrame to file.
    
    Args:
        df (pd.DataFrame): DataFrame to save
        file_path (str): Output file path
        format (str): File format ('csv', 'excel', 'json')
        **kwargs: Additional arguments for save functions
    """
    try:
        # Create directory if it doesn't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        if format == 'csv':
            df.to_csv(file_path, index=False, **kwargs)
        elif format == 'excel':
            df.to_excel(file_path, index=False, **kwargs)
        elif format == 'json':
            df.to_json(file_path, **kwargs)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        logger.info(f"Successfully saved DataFrame to {file_path}")
    except Exception as e:
        logger.error(f"Error saving DataFrame to {file_path}: {e}")
        raise


def get_data_info(df):
    """
    Get basic information about a DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame
    
    Returns:
        dict: Dictionary with DataFrame information
    """
    info = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'memory_usage': df.memory_usage(deep=True).sum(),
        'numeric_columns': list(df.select_dtypes(include=[np.number]).columns),
        'categorical_columns': list(df.select_dtypes(include=['object', 'category']).columns)
    }
    return info


def clean_data(df, drop_na=True, fill_na=None, remove_duplicates=True):
    """
    Basic data cleaning operations.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        drop_na (bool): Whether to drop rows with NA values
        fill_na (dict): Dictionary of fill values for specific columns
        remove_duplicates (bool): Whether to remove duplicate rows
    
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    df_clean = df.copy()
    
    # Handle missing values
    if drop_na:
        before_rows = len(df_clean)
        df_clean = df_clean.dropna()
        after_rows = len(df_clean)
        logger.info(f"Dropped {before_rows - after_rows} rows with NA values")
    
    if fill_na:
        df_clean = df_clean.fillna(fill_na)
        logger.info(f"Filled NA values with: {fill_na}")
    
    # Remove duplicates
    if remove_duplicates:
        before_rows = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        after_rows = len(df_clean)
        logger.info(f"Removed {before_rows - after_rows} duplicate rows")
    
    return df_clean


if __name__ == "__main__":
    # Example usage
    print("Data loader utilities loaded successfully!")
    print("Available functions:")
    print("- load_csv()")
    print("- load_excel()")
    print("- load_json()")
    print("- save_dataframe()")
    print("- get_data_info()")
    print("- clean_data()")
