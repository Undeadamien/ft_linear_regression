#!/usr/bin/env python

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


def main():
    model = load_model()
    mileage = prompt_mileage()
    x = (mileage - model[MEAN_KM]) / model[STD_KM]
    price = model[THETA_0] + model[THETA_1] * x
    print(f"Estimated price : {price:.2f}")


if __name__ == "__main__":
    main()
