import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def load_and_preprocess_data(filepath):
    # Add the 42 column names (41 features + 1 label)
    column_names = [
        "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment",
        "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted",
        "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
        "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
        "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
        "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
        "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
        "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"
    ]

    # Load CSV with column names
    df = pd.read_csv(filepath, header=None, names=column_names)

    # Encode categorical features
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    
    # Normalize features
    scaler = MinMaxScaler()
    X = df.drop('label', axis=1)
    y = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

