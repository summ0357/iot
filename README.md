# 懶人手臂：物品整理

## 簡介：
因爲覺得機器手臂很酷，然後想到可以使用機器手臂幫忙抓取移動物件去到達整理東西的效果。

### 硬體組件
樹莓派 3 *1
MG996R 伺服馬達 *6
6自由度機械手臂 *1
PCA9685（I2C介面） *1
開關電源供應器 *1（附帶電線）
杜邦線 *22（至少）

###  軟體下載
```
pip3 install flask
pip3 install adafruit-circuitpython-servokit
sudo pip3 install adafruit-circuitpython-pca9685
```
###    做法：
1.將PCA9685和樹莓派連接
![image](https://hackmd.io/_uploads/r1p_vYA_p.png)
*在連接的時候需注意自己的servo連到了那個pin，不然寫程式的時候如果servo寫錯，機器手臂就不會動

2.把馬達和PCA9685鏈接
![WhatsApp Image 2024-01-09 at 2.21.09 PM](https://hackmd.io/_uploads/r1noOFAdT.jpg =50%x)


3.把PCA9685和電源供應鏈接
![WhatsApp Image 2024-01-09 at 2.24.19 PM](https://hackmd.io/_uploads/HkQAOtAd6.jpg =50%x)
*由於電綫長度限制，所以機器手臂移動時會容易發生電綫因爲移動脫落（2&3步驟都容易發生），導致連接PCA9685和電源供應的電綫燒斷或者電源供應爆炸（不會到很嚴重）但是建議馬上把所以電源先拔掉再檢查是哪裏出問題

4.[使用樹莓派跑app.py檔去用flask打開html網頁](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask)
成功畫面：
![螢幕擷取畫面 2024-01-09 142535](https://hackmd.io/_uploads/rJy-hFRdT.png)
鏈接附教學

5.使用flask開啓html網頁分別控制機器手臂的馬達做移動和操作
![螢幕擷取畫面 2024-01-09 141139](https://hackmd.io/_uploads/ByOL3tCOa.png )
*flask需一直保持開啓狀態

[6.機器手臂移動](https://youtube.com/shorts/38PySIYNOsE)
演示影片

# 程式碼解釋
檔案：init.py
將5個servo 馬達（除了爪子開合的）設定至特定角度，並保持著該角度
```
import time
import sys
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)    //servo初始化
def init():
    pca.servo[0].angle = 50
    pca.servo[1].angle = 50
    pca.servo[5].angle = 50
    pca.servo[6].angle = 50
    pca.servo[14].angle = 50
   
    sys.exit()    //離開系統

init()    //run initial（）
```
<br/>

檔案：1up.py
控制爪子開合的servo馬達
```
import time
import sys
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)

pca.continuous_servo[5].throttle = 1 //開180度（180度為極限）
time.sleep(0.5)    //休息0.5分鐘 （如果太頻繁呼叫指令有可能造成馬達過熱冒烟，只要冒烟了馬達就壞掉了）
pca.continuous_servo[5].throttle = 0 //合至0度
pca.deinit_channels()
sys.exit()

```
<br/>

檔案a：pp.py

用flask使用html控制馬達
```
from flask import Flask,render_template,request
import time
import sys
from adafruit_servokit import ServoKit

app = Flask(__name__)
pca = ServoKit(channels=16)
new_angle = 0

//標準化6個馬達
MIN_IMP=[500,500,500,500,500,500]
MAX_IMP=[2500,2500,2500,2500,2500,2500]
MIN_ANG=[0,0,0,0,0,0]
MAX_ANG=[180,180,180,180,180,180]



def server0right():
    # 獲取當前角度
    current_angle = pca.servo[15].angle
    time.sleep(1)
    # 如果當前角度為None，將其設置為0
    if current_angle is None:
        current_angle = 0

    移動 Servo 到新的角度（當前角度 + 20）
    new_angle =  (current_angle + 20) % 180
    pca.servo[15].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
# 調用函數移動 Servo

def server0left():
    # 獲取當前角度
    current_angle = pca.servo[15].angle
    time.sleep(1)
    # 如果當前角度為None，將其設置為0
    if current_angle is None:
        current_angle = 0

    # 移動 Servo 到新的角度（當前角度 - 20）
    new_angle =  (current_angle - 20) % 180 //確保即使角度超過180但仍會移動
    pca.servo[15].angle = new_angle
   
    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
# 調用函數移動 Servo

    

def server1up():
    
    current_angle = pca.servo[14].angle
    time.sleep(1)
    
    if current_angle is None:
        current_angle = 0

   
    
    new_angle = (current_angle - 20) % 180
    
    pca.servo[14].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server1down():
    
    current_angle = pca.servo[14].angle
    time.sleep(1)
   
    if current_angle is None:
        current_angle = 0

    

    new_angle = (current_angle + 20) % 180     
    pca.servo[14].angle = new_angle

    

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server2up():
   
    current_angle = pca.servo[6].angle
    time.sleep(1)
    print("current_angle",current_angle)
   
    if current_angle is None:
        current_angle = 0

    
    new_angle = (current_angle - 20) % 180
    pca.servo[6].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server2down():
    
    current_angle = pca.servo[6].angle
    time.sleep(1)
   
    if current_angle is None:
        current_angle = 0

   
    new_angle = (current_angle + 20) % 180
    pca.servo[6].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server3up():
   
    current_angle = pca.servo[5].angle
    time.sleep(1)
    print("current_angle",current_angle)
    
    if current_angle is None:
        current_angle = 0

   
    new_angle = (current_angle - 20) % 180
    pca.servo[5].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
    
def server3down():
   
    current_angle = pca.servo[5].angle
    time.sleep(1)
   
    if current_angle is None:
        current_angle = 0

    
    new_angle = (current_angle + 20) % 180
    pca.servo[5].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
    
def server4up():
    
    current_angle = pca.servo[1].angle
    time.sleep(1)
    print("current_angle",current_angle)
   
    if current_angle is None:
        current_angle = 0

   
    new_angle = (current_angle - 20) % 180
    pca.servo[1].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server4down():
  
    current_angle = pca.servo[1].angle
    time.sleep(1)
   
    if current_angle is None:
        current_angle = 0

   
    new_angle = (current_angle + 20) % 180
    pca.servo[1].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server5up():    
    pca.continuous_servo[0].throttle = 1
    return render_template('index.html')
    sys.exit()
    
def server5down():
    pca.continuous_servo[0].throttle = 0
    return render_template('index.html')
    sys.exit()

    
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/button_click',methods=['POST'])
def button_click():
    button_value = request.form.get('button_action')

    if button_value == '0left':
        result = server0left()
    elif button_value == '0right':
        result = server0right()
    
    elif button_value == '1up':
        result = server1up()
    elif button_value == '1down':
        result = server1down()
    
    elif button_value == '2up':
        result = server2up()
    elif button_value == '2down':
        result = server2down()
        
    elif button_value == '3up':
        result = server3up()
    elif button_value == '3down':
        result = server3down()
        
    elif button_value == '4up':
        result = server4up()
    elif button_value == '4down':
        result = server4down()
    
    elif button_value == '5up':
        result = server5up()
    elif button_value == '5down':
        result = server5down()
    # Add more conditions for additional buttons as needed   
    return render_template('index.html')
    

if __name__ == '__main__':    //flask設定24
    app.run(debug=True, host='0.0.0.0')
    
```


## 參考文件

* https://docs.circuitpython.org/projects/servokit/en/latest/api.html#adafruit_servokit.ServoKit
* https://docs.circuitpython.org/projects/pca9685/en/latest/api.html 
* https://techmaze.romman.store/product/99187553
* https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
* https://projects.raspberrypi.org/en/projects/python-web-server-with-flask
* https://ithelp.ithome.com.tw/articles/10258223
* https://www.fooish.com/html/form.html
