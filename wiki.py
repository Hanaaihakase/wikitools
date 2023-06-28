import requests
import os
from file import *
from link import *

def get_wiki(title,save_title,save_type,save_site,save_lang,save_path):
    # 使用Wikisource API獲取頁面內容
    url = f"https://{save_lang}.{save_site}.org/w/api.php?action=query&prop=extracts&format=json&titles={title}"
    print(f"The url link is {url}")
    response = requests.get(url)
    data = response.json()
    print(data)

    # 解析響應，獲取頁面內容
    page = data["query"]["pages"]
    content = page[next(iter(page))]["extract"]

    save_content = content

    # 保存文件
    file_save(save_title,save_type,save_content,save_path)

def get_and_delink_wiki(save_site,save_lang,save_type,title):
    # Save wiki and delink
    save_title = f"{title}_{save_lang}_{save_site}"
    save_title = save_title.replace("/", "_")
    filename = f"{save_title}.{save_type}"
    save_path = fr".\{save_site}\{save_lang}\{save_type}"

    get_wiki(title, save_title, save_type, save_site, save_lang, save_path)
    delink(filename,save_path)