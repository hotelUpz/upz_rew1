import json

def data_upz_hotels_func(n1, n2):
    print(n1, n2)
    data_upz_hotels_renevate = []
    with open('./source/hotels_copy2.json', 'r') as f:
        data_upz_hotels = json.load(f)[n1:n2]
        for item in data_upz_hotels:
            try:
                data_upz_hotels_renevate.append(
                    { 
                    "id": item["id"],    
                    "hotel_id": item["hotel_id"],
                    "url": item["url"],
                    "otziv": item["otziv"],
                    }
                )
            except Exception as ex:
                print(f"json_reader____18str___{ex}")

        return data_upz_hotels_renevate


# python json_reader_test.py
