import requests

def obtener_clima_ciudad(ciudad):
    # Usamos una API de geocodificación gratuita para obtener latitud y longitud de la ciudad
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es&format=json"
    
    try:
        geo_response = requests.get(geo_url, timeout=5)
        geo_response.raise_for_status() # Manejo de errores HTTP [cite: 10]
        data = geo_response.json()
        
        if not data.get("results"):
            return "Ciudad no encontrada"
            
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]
        
        # Ahora obtenemos el clima usando lat y lon
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url, timeout=5)
        weather_response.raise_for_status()
        
        weather_data = weather_response.json()
        temperatura = weather_data["current_weather"]["temperature"]
        return f"{temperatura}°C"
        
    except requests.exceptions.RequestException as e:
        # Manejo de errores en caso de que la API no responda correctamente [cite: 10]
        return "Servicio de clima no disponible"