import subprocess

print("=== Monitor de Red Python ===")
objetivo = "10.200.200.200"

# Ejecutamos un ping de 1 paquete. capture_output oculta el texto técnico de Linux.
resultado = subprocess.run(["ping", "-c", "1", objetivo], capture_output=True)

# El código de retorno 0 en Linux significa que el comando funcionó sin errores.
if resultado.returncode == 0:
    print(f"[+] ALERTA: El equipo {objetivo} está RESPONDIENDO.")
else:
    print(f"[-] AVISO: El equipo {objetivo} parece estar CAÍDO.")
