import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
#from pynput import keyboard


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji = QLabel(self)
        self.description_label = QLabel(self)

       
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description_label)


        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.weather_button.setObjectName("weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji.setObjectName("emoji")
        self.description_label.setObjectName("description_label")

        self.city_input.setMinimumHeight(60)
        self.weather_button.setMinimumHeight(50)


      
        self.setStyleSheet("""                                                   
                           QLabel, QPushButton{
                            font-family: Helvetica;
                            
                           }

                           QLabel#city_label{
                            font-size: 35px;
                            font-style: italic;
                           }

                           QLineEdit#city_input{
                            font-size: 35px;
                           }

                           QPushButton#weather_button{
                            font-size: 25px;
                            font-weight: bold;
                            text-align: center;
                           }

                           QLabel#temp_label{
                            font-size: 65px;
                            padding-top: 20px;
                           }

                           QLabel#emoji{
                            font-size: 100px;
                            font-family: Apple Color Emoji;
                           }


                           QLabel#description_label{
                            font-size: 40px;
                           }                                               
                           """)

        self.setFixedSize(400, 475) 


        self.city_input.returnPressed.connect(self.get_weather)
        self.weather_button.clicked.connect(self.get_weather)



    def get_weather(self):
        api_key = "8b15472cbf9bb0532566ec038401279a"  
        city = self.city_input.text()

        try:
            response = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
            #rasises exception for http error
            response.raise_for_status()

            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)


        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")

                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")

                case 403:
                    self.display_error("Forbidden:\nAccess is denied")

                case 404:
                    self.display_error("Not found:\nCity not found")

                case 500:
                    self.display_error("Internal Server:\nPlease try again later")

                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")

                case 503:
                    self.display_error("Service Unavailable:\nServer is down")

                case 504:
                    self.display_error("Gateway Timeout:\nNo response from server")

                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")




    def display_error(self, message):
        self.emoji.clear()
        self.description_label.clear()
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)





    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 65px;")

        #converting k into celsius
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        weather_descrip = data["weather"][0]["description"] #weather description
        weather_id = data["weather"][0]["id"]
            
        self.description_label.setText(weather_descrip)
        self.emoji.setText(self.get_emoji(weather_id))
        self.temp_label.setText(f"{temp_c:.0f}℃")


    @staticmethod
    def get_emoji(weather_id):
        if 200<= weather_id <= 232:
            return "⛈️"
        
        elif 300 <= weather_id <= 321:
            return "🌦️"
        
        elif 300 <= weather_id <= 321:
            return "🌧️"
    
        elif 600 <= weather_id <= 622:
            return "❄️"
        
        elif 701 <= weather_id <= 762:
            return "🌁"
        
        elif weather_id == 741:
            return "🌋"
        
        elif weather_id == 762:
            return "🌋"
        
        elif weather_id == 771:
            return "💨"
        
        elif weather_id == 781:
            return "🌪️"
        
        elif weather_id == 800:
            return "☀️"
        
        elif 801 <= weather_id <= 854:
            return "☁️"
        
        else:
            return ""
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    
