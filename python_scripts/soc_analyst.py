import subprocess
import requests

def hacer_ping(ip):
    # Retorna True si la IP responde, False si no
    resultado = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    if resultado.returncode == 0:
        return True
    else:
        return False

def obtener_pais(ip):
    # Retorna el país de la IP usando la API
    url = f"https://ipinfo.io/{ip}/json"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json().get("country", "Desconocido")
    return "Error_API"

print("=== INICIANDO ANALISTA AUTOMÁTICO SOC ===")

with open("ips_sospechosas.txt", "r") as archivo:
    lista_ips = archivo.read().splitlines()

for ip in lista_ips:
    if ip == "":
        continue
        
    print(f"\n[*] Evaluando objetivo: {ip}")
    
    # Primero comprobamos si está viva
    if hacer_ping(ip):
        # Si está viva, consultamos la API
        pais = obtener_pais(ip)
        print(f"    [!] ALERTA: Host ACTIVO. Origen detectado: {pais}")
    else:
        print(f"    [-] INFO: Host caído. Se ignora.")

print("\n=== ANÁLISIS FINALIZADO ===")
