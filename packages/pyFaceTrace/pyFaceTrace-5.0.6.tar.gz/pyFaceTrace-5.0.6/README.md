# Author:KuoYuan Li
[![N|Solid](https://images2.imgbox.com/8f/03/gv0QnOdH_o.png)](https://sites.google.com/ms2.ccsh.tn.edu.tw/pclearn0915)  
本程式簡單地結合dlib,opencv  測試過在windows作業系統底下可正常運行且另外提供colab版本  
讓不懂機器學習的朋友可以軟簡單地操作人臉辨識,  
程式需另外安裝 dlib  
搜尋關鍵字：whl dlib cp***  ***代表python版本 ex:cp310代表 python 3.10  
dlib whl 安裝包下載網站: (https://github.com/Murtaza-Saeed/dlib/tree/master)
  - 本套工具主要針對windows使用者設計，相依之 package 及相容性問題需自行排除  
  - dlib whl 安裝包下載後必需由檔案離線安裝 pip install ...
  - opencv whl  下載點:請下載合適的opencv版本<br>
    (https://pypi.tuna.tsinghua.edu.cn/simple/opencv-contrib-python/)  
  - Note: opencv 安裝的路徑上如果有中文會導致運作不正常，建議使用者名稱不要使用中文，或是先確認python有裝在沒有中文的路徑底下  
  - 安裝 mediapipe 會順便自動安裝 opencv ，可以直接先安裝 mediapipe  
  ```
  pip install mediapipe
  ```
※PS:  
2022/11/24 使用 python3.10 搭配  
  dlib-19.22.99-cp310-cp310-win_amd64.whl  試用成功  
  
2023/4/2  
  調整函式，適配 colab  
    (https://colab.research.google.com/drive/1ou7nWLQGl8uYLR_jUDyush9-D8ToTe8P?usp=sharing)  
  移除不常用之影像檔處理函式  
  新增直接和 opencv 協作模式  
2023/11/4  
  發現的某些 windows 作業系統如果灌  
  python3.10 搭配  
  dlib-19.22.99-cp310-cp310-win_amd64.whl  
  會產生下列錯誤：  
  from _dlib_pybin11 import * ImportError: DLL load failed: 找不到指定的程序  
    
    
  ※解決方案：
  新安裝一組 python3.11(64bit) 搭配  
  (https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe)
  dlib-19.24.1-cp311-cp311-win_amd64.whl  
  ```
  pip install https://github.com/Murtaza-Saeed/dlib/raw/master/dlib-19.24.1-cp311-cp311-win_amd64.whl
  ```
  Thonny的使用者可至 工具>>選項>>直譯器>... 修改python.exe之位置，變成合適的python版本  
  vscode的使用者可按ctrl+shift+p 於上方輸入 >python:Select Interpreter 選擇合適的python版本  
  
	
	
##### Download the samples to 'train' folder(下載各種照片樣本至train資料夾)
```
import pyFaceTrace as ft  
ft.downloadImageSamples()  
```
##### work with opencv webcam process (detail)  
```
import pyFaceTrace as ft
import cv2
from PIL import ImageFont
#至train資料夾載入樣本,欲辨識之目標圖片可放入 train資料夾
ft.loadDB()
#設定文字物件
FONT = ImageFont.truetype("kaiu.ttf",50,index=0)
#webcamd 影像處理迴圈
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret, img = cap.read()
    if not ret : continue
    #取得 img 中所有人臉之矩型區域，放入rects
    rects=ft.detector(img,1)
    for rect in rects:
        #取得webcam img 中人臉之特徵向量
        fv=ft.getFeatureVector(img,rect)
        #將特徵向量和 ft.DB 中之人特徵向量做比對，找到距離最短的(dist)當作辨識結果(tag)
        tag,dist = ft.predictFromDB(fv)
        #將辨識結果顯示在 img 上
        cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,0,255),3)
        img=ft.addText2Img_cv2(img,tag,FONT,position=(rect.left(),rect.top()-FONT.size-1))
    if cv2.waitKey(10) == 27: break
    # 將 img show在視窗中
    cv2.imshow('press esc to exit...', img)
cap.release()
cv2.destroyAllWindows()
```
##### work with opencv webcam process (esay)
```
import pyFaceTrace as ft
import cv2
ft.loadDB()
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while(True):    
    ret, img = cap.read()
    if not ret:continue
    #img=cv2.flip(img,1)
    tags,dists,rects,img = ft.predictImage(img)            
    cv2.imshow('press esc to exit...', img)
    if cv2.waitKey(10) == 27: break
    
cap.release()
cv2.destroyAllWindows()
```
### Demo with webcam
```
import pyFaceTrace as ft
ft.loadDB(folder='train')
ft.predictCam()
```
##### 比對目前webcam擷取到的人臉和指定影像檔案並計算它們之間的距離
```
import pyFaceTrace as ft  
im = ft.captureImageFromCam()
VTest = ft.getFeatureVector(im)
Vtrain = ft.loadFeatureFromPic('train\\李國源.jpg')
D=ft.dist(VTest,Vtrain)
print('距離=',D)
```
##### 載入train資料夾中所有jpg檔之特徵及tag並直接預測目前webcam擷取到的人臉對應的TAG 
```
import pyFaceTrace as ft
ft.loadDB(folder='train')
im = ft.captureImageFromCam()
VTest = ft.getFeatureVector(im)
result = ft.predictFromDB(VTest)
print(result)
```



License
----

MIT
