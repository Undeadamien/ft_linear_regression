import csv
from pathlib import Path

FILE_THETAS: Path = Path("thetas.json")
FILE_DATA: Path = Path("data.csv")
M: int = 10000
RATE: float = 0.01

THETA_0: str = "theta0"
THETA_1: str = "theta1"
MEAN_KM: str = "mean_km"
STD_KM: str = "std_km"


def load_csv() -> list[tuple[float, float]]:
    data = []
    try:
        with open(FILE_DATA, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for km, price in reader:
                try:
                    data.append([float(km), float(price)])
                except Exception as e:
                    print(f"{e} {type(e)}")
                    continue
    except Exception as e:
        print(f"{e} {type(e)}")
    return data


def prompt_mileage() -> float:
    while True:
        value = input("Mileage: ")
        try:
            value = float(value)
            break
        except:
            continue
    return value
