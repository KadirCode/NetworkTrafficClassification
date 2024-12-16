from sklearn.preprocessing import StandardScaler

def scale_features(data, target):
    X = data
    y = target
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y