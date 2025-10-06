# PyQt-Weather-App
A Python desktop weather application built with PyQt5 that fetches real-time data from the OpenWeatherMap API. It displays temperature, weather conditions, and matching emoji forecasts with smooth error handling and a clean, minimal interface.


---

## Overview

This application provides a clean and interactive interface for checking weather conditions in any city. When a user enters a city name, the app retrieves real-time data from the OpenWeatherMap API, converts the temperature from Kelvin to Celsius, and displays it along with a short description such as “light rain” or “clear sky.” It also includes weather-specific emojis for a more visual experience. The program handles invalid city names, network errors, and API issues gracefully, providing clear feedback messages for each situation. Its compact and minimalist GUI makes it ideal for quick and simple weather lookups right from the desktop.

---

## Technologies Used
- **Python 3.10+**
- **PyQt5** – for GUI components  
- **Requests** – to fetch data from the OpenWeatherMap API  
- **OpenWeatherMap API** – for real-time weather information  

---


## How to Run

1. **Install dependencies:**
   - Run the following command in your terminal:
     ```bash
     pip install PyQt5 requests
     ```

2. **Get an OpenWeatherMap API key:**
   - Go to [OpenWeatherMap](https://openweathermap.org/api) and create a free account.
   - Copy your API key from the dashboard.

3. **Add your API key to the code:**
   - Open the `weather.py` file.
   - Find this line on line 102:
     ```python
     api_key = "YOUR_API_KEY_HERE"
     ```
   - Replace `"YOUR_API_KEY_HERE"` with your actual API key.

4. **Run the application:**
   - In your terminal, run:
     ```bash
     python weather.py
     ```
