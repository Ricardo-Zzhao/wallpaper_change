import os
import requests
import random
from lxml import etree

# 不存在文件夹  就创建
if not os.path.exists('./wallpaper'):
    os.mkdir('./wallpaper')

path='./wallpaper'

def get_code():
    ret = ""
    for i in range(14):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))#ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        ret += s
    return ret

def get_response(url):
    # 添加User-Agent，放在headers中，伪装成浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    # 获取所有包含新闻url的a标签
    res = requests.get(url, headers=headers)
    root = etree.HTML(res.text)
    img =root.xpath('//div[@class="col-xl-3 col-lg-4 col-sm-6 grid-item grid-sizer cat-three cat-four cat-two"]'
                    '/div/div/a/@href')
    for img_url in img:
        print(img_url)
        # 构造图片保存的名称
        image_name = '{}'.format(get_code()) + '.jpg'
        image_path = path + '/' + image_name
        image_data=requests.get(img_url).content
        with open(image_path, 'wb') as f:
            f.write(image_data)
            print(image_name, '下载完毕！！！')


def main():
    for i in range(0, 11):  # 爬取前11页
        url = 'https://iw233.cn/Tag/islandwind/iw233.php?page={}'.format(i)  # 拼接url
        get_response(url)

if __name__ == '__main__':
    main()
