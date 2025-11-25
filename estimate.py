#!/usr/bin/env python

import json

from libft import *


def prompt_mileage() -> float:
    while True:
        value = input("Mileage: ")
        try:
            value = float(value)
            break
        except:
            continue
    return value


def load_model():
    default = {THETA_0: 0.0, THETA_1: 0.0, MEAN_KM: 0.0, STD_KM: 1.0}
    try:
        with open(FILE_THETAS, "r") as file:
            data = json.load(file)
            return {**default, **data}
    except Exception:
        return default


def main():
    model = load_model()
    mileage = prompt_mileage()
    x = (mileage - model[MEAN_KM]) / model[STD_KM]
    price = model[THETA_0] + model[THETA_1] * x
    print(f"Estimated price : {price:.2f}")


if __name__ == "__main__":
    main()
