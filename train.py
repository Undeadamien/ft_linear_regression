#!/usr/bin/env python

import json

from libft import *


def main():
    data = load_csv()

    kms = [v[0] for v in data]

    mean_km = sum(kms) / len(kms)
    std_km: float = (sum((km - mean_km) ** 2 for km in kms) / len(kms)) ** 0.5
    norm_data = [((km - mean_km) / std_km, price) for km, price in data]

    t0, t1 = 0.0, 0.0
    m = len(norm_data)

    for _ in range(M):
        sum0 = sum((t0 + t1 * x - y) for x, y in norm_data)
        sum1 = sum(((t0 + t1 * x - y) * x) for x, y in norm_data)

        new_t0 = t0 - RATE * (sum0 / m)
        new_t1 = t1 - RATE * (sum1 / m)

        t0, t1 = new_t0, new_t1

    content = {THETA_0: t0, THETA_1: t1, MEAN_KM: mean_km, STD_KM: std_km}

    print(content)
    with open(FILE_THETAS, "w") as file:
        print(f"Saving results to: '{FILE_THETAS}'")
        json.dump(content, file)


if __name__ == "__main__":
    main()
