from sklearn.metrics import classification_report, confusion_matrix
import numpy as np


def get_model_predictions(model, test_generator):
    predict_x = model.predict(test_generator)
    classes_x = np.argmax(predict_x, axis=1)
    return classes_x


def get_confusion_matrix_and_report(test_generator, predictions, target_names):
    cm = confusion_matrix(test_generator.classes, predictions)
    cr = classification_report(test_generator.classes, predictions, target_names=target_names)
    return cm, cr
