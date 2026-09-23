import subprocess

print("=== Monitor de Red Python Múltiple ===")
# 1. Definimos una lista con 3 IPs. La última es inventada para forzar un fallo.
lista_ips = ["8.8.8.8", "1.1.1.1", "10.200.200.200"]

# 2. El bucle for pasará por cada IP de la lista, una por una.
for ip_actual in lista_ips:
    print(f"[*] Analizando {ip_actual}...")
    
    # 3. La variable objetivo ahora cambia dinámicamente en cada vuelta
    resultado = subprocess.run(["ping", "-c", "1", ip_actual], capture_output=True)
    
    # 4. Evaluamos el resultado
    if resultado.returncode == 0:
        print(f"    [+] ALERTA: El equipo {ip_actual} RESPONDE.")
    else:
        print(f"    [-] AVISO: El equipo {ip_actual} NO RESPONDE.")
        
print("=== Escaneo Finalizado ===")
