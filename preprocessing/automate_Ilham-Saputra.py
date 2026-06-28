"""
automate_Ilham-Saputra.py

Script otomatisasi (automate) untuk tahap preprocessing dataset German Credit Data.
Script ini merupakan hasil ekstraksi dari workflow yang sudah dilakukan secara manual
pada notebook eksperimen (Eksperimen_Ilham-Saputra.ipynb), sehingga proses preprocessing
bisa dijalankan ulang secara otomatis tanpa harus membuka notebook satu per satu.

Cara pakai:
    python automate_Ilham-Saputra.py

Output:
    namadataset_preprocessing/german_credit_data_preprocessing_train.csv
    namadataset_preprocessing/german_credit_data_preprocessing_test.csv
"""

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

RAW_DATA_PATH = os.path.join("..", "namadataset_raw", "german_credit_data_raw.csv")
OUTPUT_DIR = "namadataset_preprocessing"

NUMERICAL_FEATURES = [
    "duration_months",
    "credit_amount",
    "installment_rate_pct",
    "present_residence_since",
    "age",
    "existing_credits",
    "people_liable",
]

TARGET_COLUMN = "credit_risk"


def load_data(path: str) -> pd.DataFrame:
    """Memuat dataset mentah dari file CSV."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Menghapus missing values dan data duplikat."""
    df_clean = df.copy()
    df_clean = df_clean.dropna()
    df_clean = df_clean.drop_duplicates()
    return df_clean


def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    """Melakukan Label Encoding pada seluruh kolom bertipe kategorikal (object)."""
    df_encoded = df.copy()
    categorical_features = df_encoded.select_dtypes(include=["object", "category"]).columns.tolist()
    for col in categorical_features:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])
    return df_encoded


def cap_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Menangani outlier menggunakan metode capping berbasis IQR."""
    df_out = df.copy()
    Q1 = df_out[column].quantile(0.25)
    Q3 = df_out[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_out[column] = np.where(df_out[column] < lower_bound, lower_bound, df_out[column])
    df_out[column] = np.where(df_out[column] > upper_bound, upper_bound, df_out[column])
    return df_out


def handle_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Menangani outlier pada beberapa kolom numerik sekaligus."""
    df_out = df.copy()
    for col in columns:
        df_out = cap_outliers_iqr(df_out, col)
    return df_out


def split_and_scale(df: pd.DataFrame, numerical_features: list, target_column: str,
                     test_size: float = 0.2, random_state: int = 42):
    """Memisahkan fitur dan target, split train/test, lalu standarisasi fitur numerik."""
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    scaler = StandardScaler()
    X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
    X_test[numerical_features] = scaler.transform(X_test[numerical_features])

    return X_train, X_test, y_train, y_test


def preprocess_pipeline(raw_path: str = RAW_DATA_PATH,
                         numerical_features: list = NUMERICAL_FEATURES,
                         target_column: str = TARGET_COLUMN):
    """Menjalankan seluruh pipeline preprocessing dari awal hingga akhir."""
    df = load_data(raw_path)
    df = clean_data(df)
    df = encode_categorical(df)
    df = handle_outliers(df, ["credit_amount", "duration_months", "age"])

    X_train, X_test, y_train, y_test = split_and_scale(
        df, numerical_features, target_column
    )

    train_df = X_train.copy()
    train_df[target_column] = y_train.values

    test_df = X_test.copy()
    test_df[target_column] = y_test.values

    return train_df, test_df


def save_outputs(train_df: pd.DataFrame, test_df: pd.DataFrame, output_dir: str = OUTPUT_DIR):
    """Menyimpan hasil preprocessing ke folder namadataset_preprocessing."""
    os.makedirs(output_dir, exist_ok=True)
    train_path = os.path.join(output_dir, "german_credit_data_preprocessing_train.csv")
    test_path = os.path.join(output_dir, "german_credit_data_preprocessing_test.csv")
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    print(f"Disimpan: {train_path}")
    print(f"Disimpan: {test_path}")


if __name__ == "__main__":
    print("Memulai pipeline preprocessing otomatis...")
    train_df, test_df = preprocess_pipeline()
    print(f"Ukuran data train: {train_df.shape}")
    print(f"Ukuran data test : {test_df.shape}")
    save_outputs(train_df, test_df)
    print("Preprocessing selesai.")
