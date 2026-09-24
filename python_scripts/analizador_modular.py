import requests

# 1. DEFINIMOS LA FUNCIÓN (La máquina)
def obtener_pais(ip):
    url = f"https://ipinfo.io/{ip}/json"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos.get("country", "Desconocido") # Devuelve el país
    else:
        return "Error"

print("=== Sistema de Análisis Modular ===")

# 2. USAMOS LA FUNCIÓN (Llamamos a la máquina)
ip_test = "8.8.8.8"
print(f"[*] Analizando {ip_test}...")

# Aquí está la magia: guardamos en una variable lo que la función RETORNA
pais_origen = obtener_pais(ip_test)

print(f"[+] El ataque proviene de: {pais_origen}")
