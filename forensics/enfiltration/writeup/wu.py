from enf_scripts.pyenf import process
import pandas as pd
from tqdm import tqdm
import os


def calculate_distance(data: pd.DataFrame, enf):
    sum = 0

    val = data["f"].values

    for idx in range(len(val)):
        if abs(val[idx] - enf[idx]) > 0.002:
            sum += 1
    return sum, data.iloc[0]["dtm"]


if __name__ == "__main__":
    print("Getting enf data from audio...")

    enf_data = [
        element[0]
        for element in process(
            "..\\chall.mp3"
        )
        if element[0] != 0.0
    ]

    print("Reading data from csv files...")

    dfs = []

    for file in os.listdir("data"):
        dfs.append(pd.read_csv("data\\" + file))

    print("Concatenating data...")
    british_data = pd.concat(dfs)

    british_data["f"] = pd.to_numeric(british_data["f"])

    enf_length = len(enf_data)

    british_len = len(british_data)

    results = {}

    for idx in tqdm(range(british_len)):
        end_idx = idx + enf_length

        if end_idx < british_len:
            a, b = calculate_distance(british_data.iloc[idx:end_idx], enf_data)

            results[b] = a

    sorted_results = {
        k: v for k, v in sorted(results.items(), key=lambda item: item[1])
    }

    count = 0

    for key, val in sorted_results.items():
        print(key, val)

        count += 1

        if count > 50:
            break
