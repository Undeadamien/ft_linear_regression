import csv
import json
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
    with open(FILE_DATA, "r") as file:
        reader = list(csv.reader(file))
        if reader[0] == ["km", "price"]:
            reader.pop(0)
            for km, price in reader:
                data.append([float(km), float(price)])
    return data


def load_model():
    default = {THETA_0: 0.0, THETA_1: 0.0, MEAN_KM: 0.0, STD_KM: 1.0}
    try:
        with open(FILE_THETAS, "r") as file:
            data = json.load(file)
            return {**default, **data}
    except Exception:
        return default
