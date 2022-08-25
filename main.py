import requests
import json
import os
from scraper import scrape_page_metadata
from screenshot import make_screenshot
def main (step) :
    dirname = os.path.dirname(__file__)
    foldername = os.path.join(dirname, "curation_index")
    last_link_index = 0
    count = 1
 
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    else :
        for path in os.listdir(foldername):
            # check if current path is a file
            if os.path.isfile(os.path.join(foldername, path)):
                count += 1
        # Opening JSON file
        f = open(foldername + '/linkv' + str(count -1) + '.json')
        data = json.load(f)
        last_link_index = data["count"]
    

    headers = {
        'authorization': 'Njk1MDM5Nzk1MzU2ODkzMjU1.GOF2R6.9E5QhhfMzvUqDJmGRWInLm5LX-vZMyNey9mQc4'
    }
    r1 = requests.get(f'https://discord.com/api/v6/channels/955206458268602378/messages?limit=1', headers=headers)
    
    jsonn1 = json.loads(r1.text)
    last_message_id = jsonn1[0]['id']

    new_content = {
        "items": [],
        "count": 0
    }
    item_counter = 0
    while True:
        try: 
            r = requests.get(f'https://discord.com/api/v6/channels/955206458268602378/messages?before={last_message_id}', headers=headers)
        except: 
            print("An exception in req occured.")
        jsonn = json.loads(r.text)

        if len(jsonn) == 0:
            break
        if jsonn[0]['content'] == "undefined":
            break

        last_message_id = jsonn[-1]['id']

        for value in jsonn:
            if item_counter > last_link_index :
                link = value['content']
                if link.startswith('http'):
                    if value['embeds'] and 'description' in value['embeds'][0] and 'title' in value['embeds'][0]:
                        title = value['embeds'][0]['title']
                        description = value['embeds'][0]['description']
                        if 'thumbnail' in value['embeds'][0]:
                            thumbnail = value['embeds'][0]['thumbnail']['url']
                            img_download = value['embeds'][0]['thumbnail']['proxy_url']
                            new_content["items"].append({"link": link, "title": title, "description": description, "thumbnail": thumbnail, "img_download":img_download})
                        else : 
                            # we only need to get screenshot and add it to folder
                            thumbnail = make_screenshot(link, foldername + "/screenshots", title)
                            img_download = thumbnail
                            new_content["items"].append({"link": link, "title": title, "description": description, "thumbnail": thumbnail, "img_download":img_download})
                    else :
                        #We need to get title and description as well as screenshot and add it to folder
                        page_info = scrape_page_metadata(link)
                        if page_info != False:
                            title = page_info['title']
                            if title == None: 
                                title = page_info['sitename']
                            description = page_info['description']
                            thumbnail = make_screenshot(link, foldername + "/screenshots", title)
                            img_download = thumbnail
                            new_content["items"].append({"link": link, "title": title, "description": description, "thumbnail": thumbnail, "img_download":img_download})
                    
            item_counter += 1
            print (item_counter)
            if item_counter == last_link_index + step:
                break
        if item_counter == last_link_index + step:
            break
    print (item_counter)
    new_content["count"] = item_counter
    print(new_content)

    outfile = open(foldername + '/linkv' + str(count) + '.json', 'w')
    json.dump(new_content, outfile, indent = 3)
        
main(230)