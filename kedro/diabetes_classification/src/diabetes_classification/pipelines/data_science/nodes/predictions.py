




def predictions(knn, X_test):
    print(type(knn))
    y_pred = knn.predict(X_test)
    return y_pred