import json
raw_json = '{"station_id": "ORD_IL_404", "temp_k": 294.15}'

def process_stream(raw_data):
    data = json.loads(raw_data)
    celsius = round(data["temp_k"] - 273.15, 2)
    return {"station": data["station_id"], "temp_c": celsius}

if __name__ == "__main__":
    print(process_stream(raw_json))

