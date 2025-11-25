#!/usr/bin/env python

import json

from libft import *


def main():
    with open("thetas.json", "r") as file:
        t = json.load(file)

    t0: float = t[THETA_0]
    t1: float = t[THETA_1]
    mean_km: float = t[MEAN_KM]
    std_km: float = t[STD_KM]

    mileage = prompt_mileage()

    x = (mileage - mean_km) / std_km

    price = t0 + t1 * x
    print(f"Estimated price : {price:.2f}")


if __name__ == "__main__":
    main()
