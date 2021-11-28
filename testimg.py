import imghdr
import os
def delect_webp_and_none_type(path):        #用来删除破损的图片
    for root,dir,file in os.walk(path):
        for name in file:
            target = (os.path.join(root,name))
            result_type = imghdr.what(target)
            if result_type == 'webp' or result_type == None:
                print(target)
                os.remove(target)
            if name =='main':
                delect_webp_and_none_type('./wallpaper')
if __name__ == '__main__':
    delect_webp_and_none_type('./wallpaper')
