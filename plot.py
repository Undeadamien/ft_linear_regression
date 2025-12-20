#!/usr/bin/env python

import json

import matplotlib.pyplot as plt

from libft import *


def main():
    model = load_model()
    data = load_csv()
    kms = [v[0] for v in data]
    prices = [v[1] for v in data]

    regression = []
    for km in kms:
        x = (km - model[MEAN_KM]) / model[STD_KM]
        price = model[THETA_0] + model[THETA_1] * x
        regression.append(price)

    plt.scatter(kms, prices)
    plt.plot(kms, regression)
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.show()


if __name__ == "__main__":
    main()
