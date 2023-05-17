def db_wrtr(total):
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print('hello db_writerr')

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Writerr connection established2")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

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
        print(resReviews[0])
        try:
            query7 = "INSERT INTO result_review_test1 (hotelid, title, cons, pros, dt1, average_score, author_name, room_id, checkin, checkout, languagecode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                  
            for item in resReviews:
                try:
                    values = (item["hotelid"], item["title"], item["cons"], item["pros"], item["dt1"], item["average_score"], item["author_name"], item["room_id"], item["checkin"], item["checkout"], item["languagecode"])
                    cursor.execute(query7, values)
                except Exception as ex:
                    print(f"db_writerr__str56__{ex}")
                    continue
            conn.commit()
        except:
            pass
        

    except Exception as ex:
        print(f"db_writerr__str63__{ex}")
        # pass
    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return 























# total = None
# db_opener(total)

# python db_writerrr.py



# resRoomHighlights = []
# with open('result_description__interval_0__1120__Items_982.json', 'r') as f:
#     data_result_descript = json.load(f)
# with open('photos__12_05_2023__16_32__443.json', 'r') as f:
#     resPhoto = json.load(f) 
# with open('facilities__12_05_2023__16_32__1030.json', 'r') as f:
#     resFacilities = json.load(f) 
# with open('room__12_05_2023__16_31__62.json', 'r') as f:
#     resRooms = json.load(f) 
# with open('room_block__12_05_2023__16_31__62.json', 'r') as f:
#     resRoomsBlock = json.load(f)
    # print(resRoomsBlock)
