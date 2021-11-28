# wallpaper_change
1.首先爬取了https://iw233.cn/ 的图库具体见mirlkoi_spider.py，如果发现破损图片运行testimg.py<br>
2.为了适应屏幕每次从wallpaper中选取8张图片按照1024*1556的比例拼接在一起<br>
3.运行img_move.py copy图片至壁纸生成库<br>
4.运行compose.py 拼接图片<br>
5.运行change.py，每30min更换一次壁纸<br>
6.最后可以用Pyinstaller库来进行打包<br>
![QQ截图20211128020142](https://user-images.githubusercontent.com/76592978/143734289-c73a3c87-6238-40fc-869a-fcf1eb506f9f.png)
![QQ截图20211128155151](https://user-images.githubusercontent.com/76592978/143734364-03f2b21b-e177-4f7e-9bac-e8ffe4065c29.png)
![QQ截图20211128155230](https://user-images.githubusercontent.com/76592978/143734428-0f324123-72a3-4954-940c-036d4503a125.png)

