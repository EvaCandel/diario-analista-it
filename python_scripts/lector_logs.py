import subprocess

archivo_texto = "ips_sospechosas.txt"
print(f"[*] Abriendo archivo de amenazas: {archivo_texto}")

# 1. Abrimos el archivo en modo lectura ("r")
with open(archivo_texto, "r") as archivo:
    # 2. Extraemos las líneas limpias y las guardamos en una lista
    lista_ips = archivo.read().splitlines()

print(f"[*] Se han cargado {len(lista_ips)} IPs. Iniciando análisis...\n")

# 3. Reutilizamos el bucle de ayer, pero ahora la lista viene del archivo
for ip_actual in lista_ips:
    resultado = subprocess.run(["ping", "-c", "1", ip_actual], capture_output=True)
    
    if resultado.returncode == 0:
        print(f"[!] ALERTA CRÍTICA: La IP sospechosa {ip_actual} está activa en la red.")
    else:
        print(f"[+] INFO: La IP {ip_actual} está bloqueada o inactiva.")
