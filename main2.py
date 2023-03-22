import subprocess

# Ejecuta el comando para escanear las redes WiFi cercanas y guarda la salida en una variable
result = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=Bssid']).decode('ascii')

# Separa la salida por líneas
result_lines = result.split('\r\n')

# Elimina las primeras dos líneas (información de encabezado)
result_lines = result_lines[2:]

# Crea una lista vacía para almacenar la información de la red WiFi
wifi_networks = []

# Analiza la salida y guarda la información de cada red WiFi en la lista wifi_networks
while len(result_lines):
    line = result_lines.pop(0).strip()
    if 'SSID' in line:
        wifi_networks.append({'SSID': line.split(':')[-1].strip()})
    elif 'Signal' in line:
        wifi_networks[-1]['Signal'] = line.split(':')[-1].strip()
    elif 'BSSID' in line:
        wifi_networks[-1]['BSSID'] = line.split(':')[-1].strip()
    elif 'Authentication' in line:
        wifi_networks[-1]['Authentication'] = line.split(':')[-1].strip()

# Imprime la información de cada red WiFi encontrada
for network in wifi_networks:
    print('SSID: ' + network['SSID'] + ', Signal: ' + network['Signal'] + ', BSSID: ' + network['BSSID'] + ', Authentication: ' + network['Authentication'])
