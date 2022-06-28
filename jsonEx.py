import json

with open("data_file.json", "r") as info:
    data = json.load(info)

    print(data["People"][0]["name"])

    data["People"][1]["role"] = "Also the GOAT, I guess"

    with open("next_data_file.json", "w") as s2:
        json.dump(data, s2)



# Notes
