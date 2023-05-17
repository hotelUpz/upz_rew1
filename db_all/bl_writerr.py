def bl_db_wrtr(black_list):
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection established3")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    print(f"len blackList___{len(black_list)}")
    # print(black_list)

    try:
        query9 = "INSERT INTO black_list_reviews_test1 (hotelid, url, otziv) VALUES (%s, %s, %s)"

        for item in black_list:
            try:
                values = (item["hotel_id"], item["url"], item["otziv"])
                cursor.execute(query9, values)
            except Exception as ex:
                print(f"b_db_filter_func___59{ex}")
                continue
        conn.commit()
    except Exception as ex:
        print(f"b_db_filter_func___39{ex}")

    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"b_db_filter_func_Error connecting to MySQL: {e}")

    return 

