import json

USD_TO_INR = 83

clean_data = []
seen = set()

with open("sales.csv", "r") as file:
    for line in file:
        parts = line.split(",")

        product_id = parts[0].strip()
        product_name = parts[1].replace('"', '').strip()

        price_raw = parts[2].replace("$", "").strip()
        price_USD = float(price_raw)

        country = parts[3].strip()

        key = (product_name, price_USD)
        if key in seen:
            continue
        seen.add(key)

        price_INR = price_USD * USD_TO_INR

        clean_data.append({
            "id": int(product_id),
            "product": product_name,
            "price_USD": price_USD,
            "price_INR": price_INR,
            "country": country
        })

with open("clean_sales.json", "w") as json_file:
    json.dump(clean_data, json_file, indent=4)

print("JSON file successfully generated")