from . import b_filter_func
from datetime import datetime
import json

def b_w_writerr(black_list):
    print("hello black writer")
    now = datetime.now() 
    curentTimeForFile = now.strftime("%d_%m_%Y__%H_%M")

    if black_list != None and black_list != []:
        print(f"len_blackList___{len(black_list)}")
        try:
            with open(f'black_list__{curentTimeForFile}__{len(black_list)}.json', "w", encoding="utf-8") as file: 
                json.dump(black_list, file, indent=4, ensure_ascii=False)
        except Exception as ex:
            print(f"str348__{ex}")
