#!/usr/bin/env python

import json

import matplotlib.pyplot as plt

from libft import *


def main():
    with open("thetas.json", "r") as file:
        t = json.load(file)

    t0: float = t[THETA_0]
    t1: float = t[THETA_1]
    mean_km: float = t[MEAN_KM]
    std_km: float = t[STD_KM]

    data = load_csv()
    kms = [v[0] for v in data]
    prices = [v[1] for v in data]

    regression = []
    for km in kms:
        x = (km - mean_km) / std_km
        price = t0 + t1 * x
        regression.append(price)

    plt.scatter(kms, prices)
    plt.plot(kms, regression)
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.show()


if __name__ == "__main__":
    main()
