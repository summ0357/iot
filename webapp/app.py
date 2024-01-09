from flask import Flask,render_template,request
import time
import sys
from adafruit_servokit import ServoKit

app = Flask(__name__)
pca = ServoKit(channels=16)
new_angle = 0

MIN_IMP=[500,500,500,500,500,500]
MAX_IMP=[2500,2500,2500,2500,2500,2500]
MIN_ANG=[0,0,0,0,0,0]
MAX_ANG=[180,180,180,180,180,180]



def server0right():
    # 获取当前角度
    current_angle = pca.servo[15].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle =  (current_angle + 20) % 180
    pca.servo[15].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
# 调用函数移动 Servo

def server0left():
    # 获取当前角度
    current_angle = pca.servo[15].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle =  (current_angle - 20) % 180
    pca.servo[15].angle = new_angle
   
    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
# 调用函数移动 Servo

    

def server1up():
    # 获取当前角度
    current_angle = pca.servo[14].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    
    new_angle = (current_angle - 20) % 180
    
    pca.servo[14].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server1down():
    # 获取当前角度
    current_angle = pca.servo[14].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）

    new_angle = (current_angle + 20) % 180     
    pca.servo[14].angle = new_angle

    

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server2up():
    # 获取当前角度
    current_angle = pca.servo[6].angle
    time.sleep(1)
    print("current_angle",current_angle)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle = (current_angle - 20) % 180
    pca.servo[6].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server2down():
    # 获取当前角度
    current_angle = pca.servo[6].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle = (current_angle + 20) % 180
    pca.servo[6].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server3up():
    # 获取当前角度
    current_angle = pca.servo[5].angle
    time.sleep(1)
    print("current_angle",current_angle)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle = (current_angle - 20) % 180
    pca.servo[5].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
    
def server3down():
    # 获取当前角度
    current_angle = pca.servo[5].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle = (current_angle + 20) % 180
    pca.servo[5].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()
    
def server4up():
    # 获取当前角度
    current_angle = pca.servo[1].angle
    time.sleep(1)
    print("current_angle",current_angle)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
    new_angle = (current_angle - 20) % 180
    pca.servo[1].angle = new_angle

    # 返回新的角度
    print(new_angle)
    return render_template('index.html')
    #print("Servo moved to {new_angle} degrees")
    sys.exit()

def server4down():
    # 获取当前角度
    current_angle = pca.servo[1].angle
    time.sleep(1)
    # 如果当前角度为None，将其设置为0
    if current_angle is None:
        current_angle = 0

    # 移动 Servo 到新的角度（当前角度 + 20）
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
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
