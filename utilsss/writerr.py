from datetime import datetime
import json

def writerr(total):
    print(len(total))
    resReviews = []

    try:
        for t in total:
            try:
                for t2 in t[0]:
                    try:
                        resReviews += t2
                    except Exception as ex:
                        print(f"writerr__str13__{ex}")
                        continue 
            except Exception as ex:
                print(f"writerr__str18__{ex}")
                continue 



        try:
            resReviews = list(filter(None, resReviews))
            resReviews = list(filter("", resReviews)) 
            resReviews = list(filter([], resReviews)) 
        except:
            pass       

    except Exception as ex:
        print(f"writerr__str25__{ex}")
    
    now = datetime.now() 
    curentTimeForFile = now.strftime("%d_%m_%Y__%H_%M")

    try:
        if resReviews != None and resReviews != []:
            print(f"len_resReviews___{len(resReviews)}")
            try:
                with open(f'resReviews__{curentTimeForFile}__{len(resReviews)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resReviews, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"writerr__str39__{ex}")
    except Exception as ex:
        print(f"writerr__str41__{ex}")
