def exp_6_raspi_with_mqtt():
    s="""import paho.mqtt.client as mqtt
import Rpi.GPIO as GPIO
import dht11
import json
import time

GPIO.setWarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "TOPIC_NAME"

instance = dht11.DHT11(pin=14)
result = instance.read()
client = mqtt.Client()

def on_connect(client,userdata,flags,rc):
    print("connected with result code : ",str(rc))

def on_publish(client,userdata,mid):
    print("message published")

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(MQTT_BROKER,MQTT_PORT,60)

try:
    while True:
        humidity = result.humidity
        temperature = result.temperature
        if(humidity is not None and temperature is not None):
            data = {
                "temperature" : round(temperature,2),
                "humidity" : round(humidity,2)
            }
            payload = json.dumps(data)
            client.publish(MQTT_TOPIC,payload)
            print(f"Published : {payload}")
        else:
            print("failed to retrive data")
        time.sleep(10)
except KeyboardInterrupt:
    print("Interupt by the user")
    client.disconnect()"""
    return s

def exp2_i_bllinking_of_led_ino():
    s="""const int ledPin = 3;
void setup()
{
    pinMode(ledPin,OUTPUT);
}
void loop()
{
    digitalWrite(ledPin,HIGH);
    delay(500);
    digitalWrite(ledPin,LOW);
}"""
    return s

def exp2_ii_multiple_led_blinking_pattern_ino():
    s="""//make sure that the led wires are connected on port 2,3,4,5

int ledPin;
void pattern1();
void pattern2();

void setup()
{
    Serial.begin(9600);
    for(ledPin=2;ledPin<6;ledPin++)
    {
        pinMode(ledPin,OUTPUT);
    }
    Serial.println("choose between option 1 or 2");
}
void pattern1()
{
    for(ledPin=2;ledPin<6;ledPin++)
    {
        digitalWrite(ledPin,HIGH);
    }
    delay(500);
    for(ledPin=2;ledPin<6;ledPin++)
    {
        digitalWrite(ledPin,LOW);
    }
    exit(0);
}
void pattern2()
{
    for(ledPin=2;ledPin<6;ledPin++)
    {
        digitalWrite(ledPin,HIGH);
        delay(500);
        digitalWrite(ledPin,LOW);
    }
    exit(0);
}

void loop()
{
    int inp = Serial.parseInt();
    if(inp==1)
    {
        pattern1();
    }
    if(inp==2)
    {
        pattern2();
    }
}"""
    return s

def exp3_a_ultrasonic_with_serial_monitor_ino():
    s="""const int echoPin = 3;
const int trigPin = 2;

void setup()
{
    Serial.begin(9600);
    pinMode(echoPin,INPUT);
    pinMode(trigPin,OUTPUT);
}
void loop()
{
    digitalWrite(trigPin,HIGH);
    delay(100);
    digitalWrite(trigPin,LOW);
    long long duration = pulseIn(echoPin,HIGH);
    float distance = (duration*0.0034)/2;
    Serial.println(distance);
}"""
    return s

def exp3_b_ultrasonic_with_buzzer_ino():
    s="""const int trigPin = 2;
const int echoPin = 3;
const int buzzerPin = 4;

void setup()
{
    pinMode(trigPin,OUTPUT);
    pintMode(echoPin,INPUT);
    pinmode(buzzerPin,OUTPUT);
}

void loop()
{
    digitalWrite(trigPin,HIGH);
    delay(100);
    digitalWrite(echoPin,LOW);
    long long duration = pulseIn(echoPin,HIGH);
    float distance = (duration*0.0034)/2;
    if(distance<20.0)
    {
        digitalWrite(buzzerPin,HIGH);
    }
    else
    {
        digitalWrite(buzzerPin,LOW);
    }
}"""
    return s

def exp4_a_servomotor_ino():
    s="""#include <Servo.h>
Servo myServo;
int servoPin = 9;
int pos = 0;

void setup() {
    myServo.attach(9);
}

void loop()
{
    for (pos = 0; pos <= 180; pos++) {
        myServo.write(pos);
        delay(15);
    }
    delay(1000);
    for (pos = 180; pos >= 0; pos--) {
        myServo.write(pos);
        delay(15);
    }
    delay(1000);
}"""
    return s

def exp4_b_stepperMotor_ino():
    s="""#include <AccelStepper.h>

AccelStepper stepper(8, 10, 12, 11, 13);

void setup() {
    Serial.begin(9600);
    Serial.println("Stepper motor running continuously");

    stepper.setMaxSpeed(1000.0);
    stepper.setAcceleration(100.0);
    stepper.setSpeed(200);
}

void loop() {
    stepper.runSpeed();
}"""
    return s

def exp5_lcd_display_ino():
    s="""#include<Keypad.h>
#include<LiquidCrystal_I2C.h>
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};
byte rowPins[ROWS] = {2,3,4,5};
byte colPins[COLS] = {6,7,8,9};

Keypad keypad = Keypad(makeKeymap(keys),rowPins,colPins,ROWS,COLS);

LiquidCrystal_I2C lcd(0x20,4,5,6,0,1,2,3,7,POSITIVE);

void setup()
{
    lcd.begin(16,2);
    lcd.backlight();
    lcd.clear();
    lcd.setCursor(0,0);
}
void loop()
{
    char key = keypad.getKey();
    if(key)
    {
        lcd.setCursor(2,0);
        lcd.print(key);
    }
}"""
    return s

def exp7_log_ultrasonic_sensor_values_to_firebase_py():
    s="""import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials, firestore
import json

cred = credentials.Certificate("/path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")

        data = {
            'value': distance
        }
        json_data = json.dumps(data)

        doc_ref = db.collection(u'ultrasonic').document(u'distance')
        doc_ref.set(json.loads(json_data))

        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()"""
    return s

def exp8_servomotor_with_keyboard_py():
    s="""import Rpi.GPIO as GPIO
import time

servo_pin = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm = GPIO.PWM(servo_pin,50)
pwm.start(0)

def set_angle(angle):
    pwm.ChangeDutyCycle((angle/18)+2)
    time.sleep(1)
    pwm.ChangeDutyCycle(0)

try:
    print('q to quit')
    while True:
        angle_str = input("enter angle")
        if(angle=="q"):
            break
        try:
            angle = int(angle_str)
            if(0<=angle<=180):
                set_angle(angle)
            else:
                print("invalid angle")
        except ValueError:
            print("value error raised")
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
            """
    return s

def exp9_brightness_level_py():
    s="""import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

ledPin = 18  # Replace with the actual GPIO pin connected to the LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
pwm = GPIO.PWM(ledPin, 100)
pwm.start(0)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("IOTIF/Rpi/PWM")

def on_message(client, userdata, msg):
    brightness = int(msg.payload)
    print(f"Received brightness: {brightness}")
    pwm.ChangeDutyCycle(brightness)

client = mqtt.Client()
client.connect("broker.hivemq.com")
client.on_connect = on_connect
client.on_message = on_message

try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()"""
    return s

def exp_10_webpage_text_display_py():
    s="""import paho.mqtt.client as mqtt
from time import sleep
from RPI_i2c_driver import i2c_driver

lcd = i2c_driver.lcd()

broker_address = "hive.broker.mqtt"
port = 1883
topic = "your_topic"

def on_connect(client,userdata,flags,rc):
    print("connected")
    client.subscribe("TOPIC_NAME")

def on_message(client,userdata,message):
    data = str(message.payload.decode("utf-8"))
    lcd.lcd_display_string(message,1)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("hive.broker.mqtt")
try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()"""
    return s
def exp_11_12_py():
    s="""from flask import Flask,request,url_for,redirect,send_from_directory
import RPi.GPIO as GPIO

HOST = '0.0.0.0'
PORT = 80
DEGUB = True

GPIO.setmode(GPIO.BCM)
ledPin = 2
GPIO.setup(ledPin,GPIO.OUT)
relayPin = 5
GPIO.setup(relayPin,GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello world")
    return 'Hello World'

@app.route('/led_on')
def led_on():
    print("led on")
    GPIO.output(ledPin,GPIO.HIGH)

@app.route('/relay_on')
def relay_on():
    print('relay on')
    GPIO.output(ledPin,GPIO.HIGH)

@app.route('/led_off')
def led_off():
    print("led off")
    GPIO.output(ledPin,GPIO.LOW)

@app.route('/relay_off')
def relay_off():
    print('relay off')
    GPIO.output(ledPin,GPIO.LOW)

if __name__== '__main__':
    app.run(host=HOST,port=PORT,debug=True)"""
    return s
