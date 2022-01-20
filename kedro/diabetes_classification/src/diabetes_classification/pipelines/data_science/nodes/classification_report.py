from sklearn.metrics import classification_report as cr

def classification_report(y_test, y_predict):
    print(cr(y_test, y_predict))
    return None
