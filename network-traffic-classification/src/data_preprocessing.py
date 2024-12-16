import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    """Load and preprocess the dataset from a CSV file."""
    # Specify column names
    column_names = [
        'srcip', 'sport', 'dstip', 'dsport', 'proto', 'state', 'dur', 'sbytes', 'dbytes', 'sttl', 'dttl', 'sloss', 'dloss',
        'service', 'Sload', 'Dload', 'Spkts', 'Dpkts', 'swin', 'dwin', 'stcpb', 'dtcpb', 'smeansz', 'dmeansz', 'trans_depth',
        'res_bdy_len', 'Sjit', 'Djit', 'Stime', 'Ltime', 'Sintpkt', 'Dintpkt', 'tcprtt', 'synack', 'ackdat', 'is_sm_ips_ports',
        'ct_state_ttl', 'ct_flw_http_mthd', 'is_ftp_login', 'ct_ftp_cmd', 'ct_srv_src', 'ct_srv_dst', 'ct_dst_ltm', 'ct_src_ltm',
        'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'attack_cat', 'label'
    ]
    
    # Load the dataset with specified column names
    data = pd.read_csv(file_path, names=column_names, low_memory=False)
    
    # Print column names to inspect
    print(data.columns)
    
    # Select relevant features
    features = data[['proto', 'Spkts', 'Dpkts', 'sbytes', 'dbytes', 'dur']]
    target = data['service']
    
    # Encode categorical variables
    label_encoder = LabelEncoder()
    features.loc[:, 'proto'] = label_encoder.fit_transform(features['proto'])
    target = label_encoder.fit_transform(target)
    
    return features, target