#Importar librerias
import subprocess

#Crear variable que recopile los nombres de los perfiles de redes inalámbricas a los que se ha conectado previamente el usuario en una lista de Python.
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

#extrae los nombres de los perfiles de red inalámbrica que se muestran en la salida del comando "netsh wlan show profiles" y los almacena en una lista llamada profiles
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

#Crear un bucle for que recorra la lista profiles y extraiga los nombres de los perfiles de red inalámbrica que se muestran en la salida del comando "netsh wlan show profiles" y los almacena en una lista llamada profiles
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

input("")
