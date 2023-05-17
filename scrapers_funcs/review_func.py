from bs4 import BeautifulSoup

def page_scraper_otziv(resHtml, hotelid):
    # return print('hello page_scraper_otziv')
    result_review_upz = []

    try:
        soup1 = BeautifulSoup(resHtml, "lxml")  
        # print(resHtml)     
    except Exception as ex:
        # print(f"str102___{ex}")
        return None
 
    try:
        # print('hello finder')
        try:
           review_block = soup1.find('ul', attrs={}).find_all('li', class_='review_list_new_item_block')
        except:
            return None
        # print(len(review_block))
        for item in review_block:
            try:
                title = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get_text().strip()
                # print(title)               
            except Exception as ex:
                title = 'not found'
                # print(f"str129___{ex}")
            try:
                pros = item.find('p').find('span', class_='c-review__body').get_text().strip()
                # print(pros)              
            except Exception as ex:
                pros = 'not found' 
                # print(f"str129___{ex}")
            try:
                cons = item.find_all('p')[1].find('span', class_='c-review__body').get_text().strip()
                # print(cons)
            except Exception as ex:
                cons = 'not found' 
                # print(f"str129___{ex}") 
            try:
                dt1 = item.find_all('span', class_='c-review-block__date')[1].get_text().split(':')[1].strip()
                # print(dt1)
            #    break
            except Exception as ex:
                dt1 = 'not found'
                # print(f"str129___{ex}") 
            try:
                average_score = item.find('div', class_='bui-review-score__badge').get_text().strip()
                # print(average_score)
            #    break
            except Exception as ex:
                average_score = 'not found'
                # print(f"str129___{ex}") 
            try:
                author_name = item.find('span', class_='bui-avatar-block__title').get_text().strip()
                # print(author_name)
            #    break
            except Exception as ex:
                author_name = 'not found'
                # print(f"str129___{ex}") 
            try:
                room_id = item.find('div', class_='bui-list__body').get_text().strip()
                # print(room_id)
            #    break
            except Exception as ex:
                room_id = 'not found'
                # print(f"str129___{ex}") 
            try:
                checkinBlock = item.find_all('div', class_='bui-list__body')[1]
                #    print(checkinBlock)
                checkin = checkinBlock.get_text(strip=True, separator="\n")
                # print(checkin)
                #    break
            except Exception as ex:
                checkin = 'not found'
                # print(f"str129___{ex}") 
            try:
                checkout = checkin 
            except Exception as ex:
                checkout = 'not found'
                # print(f"str129___{ex}") 
            try:                
                languagecode = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get('lang').strip()
            except:
                try:
                    languagecode = item.find('p').find('span', class_='c-review__body').get('lang').strip()
                except:
                    try:
                        languagecode = item.find_all('p')[1].find('span', class_='c-review__body').get('lang').strip()
                    except Exception as ex:
                        languagecode = 'not found'
                        print(f"review_func__str96___{ex}") 
            # print(languagecode)
            result_review_upz.append({
                "hotelid": hotelid,
                "title": title, 
                "cons": cons, 
                "pros":pros, 
                "dt1": dt1, 
                "average_score": average_score, 
                "author_name": author_name, 
                "room_id":room_id, 
                "checkin": checkin, 
                "checkout": checkout, 
                "languagecode": languagecode,                
            })

            # print(len(result_review_upz_list))
    except Exception as ex:
        print(f"str162___{ex}") 
        pass
    try:
        return result_review_upz
    except:
        return None