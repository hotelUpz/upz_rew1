def black_filter(finRes):
    d_lackList = []
    refactor_blacList = []


    print('hello b_filter_func')

    for t in finRes:
        try:
           d_lackList.append(t[1])
        except Exception as ex:
            print(f"black_filter__str11__{ex}")
            continue
    try:
        d_lackList = list(filter(None, d_lackList))                
        d_lackList = list(filter([], d_lackList))
    except Exception as ex:
        print(f"black_filter__str17___{ex}")
    try:
        for t2 in d_lackList:
            try:
               refactor_blacList += t2 
            except Exception as ex:
                print(f"black_filter__str23___{ex}")
                continue
    except Exception as ex:
        print(f"black_filter__str26___{ex}")

    try:
        print(f"refactor_blackList___19str__len__{len(refactor_blacList)}")
        print(refactor_blacList)
        return refactor_blacList
    except Exception as ex:
        # print(f"331____{ex}")
        return None

