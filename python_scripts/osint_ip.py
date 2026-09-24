import requests

print("=== Herramienta OSINT de Geolocalización ===")
ip_objetivo = "8.8.8.8"
url_api = f"https://ipinfo.io/{ip_objetivo}/json"

print(f"[*] Consultando base de datos para la IP {ip_objetivo}...")

# 1. Hacemos la petición a la web
respuesta = requests.get(url_api)

# 2. Comprobamos que el servidor web respondió bien (Código HTTP 200 = OK)
if respuesta.status_code == 200:
    # 3. Convertimos el texto JSON a un diccionario de Python
    datos_json = respuesta.json()
    
    # 4. Extraemos los datos exactos que queremos cruzando las claves
    pais = datos_json["country"]
    empresa = datos_json["org"]
    
    print(f"[+] RESULTADO OSINT:")
    print(f"    - País de origen: {pais}")
    print(f"    - Organización: {empresa}")
else:
    print("[-] Error al contactar con la API externa.")
