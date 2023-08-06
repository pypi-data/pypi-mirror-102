import numpy as np


def exist_two_class(matrix):
    """
    to ensure all cols in coding matrix have 1 and -1
    :param matrix: coding matrix
    :return: true or false
    """
    col_count = matrix.shape[1]
    for i in range(col_count):
        col_unique = np.unique(matrix[:, i])
        if (1 not in col_unique) or (-1 not in col_unique):
            return False
    return True

def get_data_subset(data, label, target_label):
    """
    to get data with certain labels
    :param data: data set
    :param label: label corresponding to data
    :param target_label: the label which we want to get certain data
    :return:
    """
    data_subset = np.array([data[i] for i in range(len(label)) if label[i] in target_label])
    label_subset = np.array([label[i] for i in range(len(label)) if label[i] in target_label])
    return data_subset, label_subset
