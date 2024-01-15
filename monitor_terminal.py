import getpass
import telnetlib
import time
from tkinter import messagebox as Messagebox
from tkinter import simpledialog as SimpleDialog

ip_router = input('Introduzca la direccion IP del router que desea accesar: ')
USERNAME = 'cisco'
PASSWORD = 'cisco'


def ConfigGlo(router_ip, username, password):
    try:
        #Crear una conexión Telnet
        tn = telnetlib.Telnet(router_ip)

        #Esperar a que aparezca el prompt de inicion de sesión
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")

        #Espeara a que aprezca el prompt de contraseña
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        #Verificar si la autentificación fue exitosa
        output = tn.read_until(b"#") #Cambia el prompt según el router
        if b"incorrect" in output or b"denied" in output or b"%" in output:
            Messagebox.showerror("Error", "Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
            # print("Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
        else:
            Messagebox.showinfo("Mensaje", "Conexion exitosa del router.")
            # print("Conexion exitosa del router.")

            #Enviar el comando "show ip interfaces brief"
            tn.write(b"terminal length 0\n")
            output = tn.read_until(b"#") #Cambia el prompt según el router
            tn.write(b"show running-config\n")
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#")
            #output = tn.read_until(b"!\n!\nend") #Cambia el prompt segun el router
            output = output.decode('ascii')
            # print(output.decode('ascii'))
            Messagebox.showinfo("Datos", output)


        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def ConfigRut(router_ip, username, password):

    try:
        #Crear una conexión Telnet
        tn = telnetlib.Telnet(router_ip)

        #Esperar a que aparezca el prompt de inicion de sesión
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")

        #Espeara a que aprezca el prompt de contraseña
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        #Verificar si la autentificación fue exitosa
        output = tn.read_until(b"#") #Cambia el prompt según el router
        if b"incorrect" in output or b"denied" in output or b"%" in output:
            Messagebox.showerror("Error", "Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
            # print("Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
        else:
            Messagebox.showinfo("Mensaje", "Conexion exitosa del router.")
            # print("Conexion exitosa del router.")
            #Enviar el comando "show ip interfaces brief"
            tn.write(b"terminal length 0\n")
            output = tn.read_until(b"#") 
            tn.write(b"show ip route\n")
                
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#") #Cambia el prompt segun el router
            output = output.decode('ascii')
            # print(output.decode('ascii'))

        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def ConfigDHCP(router_ip, username, password):

    try:
        #Crear una conexión Telnet
        tn = telnetlib.Telnet(router_ip)

        #Esperar a que aparezca el prompt de inicion de sesión
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")

        #Espeara a que aprezca el prompt de contraseña
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        #Verificar si la autentificación fue exitosa
        output = tn.read_until(b"#") #Cambia el prompt según el router
        if b"incorrect" in output or b"denied" in output or b"%" in output:
            Messagebox.showerror("Error", "Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
            # print("Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
        else:
            Messagebox.showinfo("Mensaje", "Conexion exitosa del router.")
            # print("Conexion exitosa del router.")

            tn.write(b"terminal length 0\n")
            output = tn.read_until(b"#") 
            #Enviar el comando "show ip interfaces brief"
            tn.write(b"show ip dhcp pool\n")
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#") #Cambia el prompt segun el router
            output = output.decode('ascii')
            # print(output.decode('ascii'))
            Messagebox.showinfo("Datos", output)

        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def ConfigACL(router_ip, username, password):

    try:
        #Crear una conexión Telnet
        tn = telnetlib.Telnet(router_ip)

        #Esperar a que aparezca el prompt de inicion de sesión
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")

        #Espeara a que aprezca el prompt de contraseña
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        #Verificar si la autentificación fue exitosa
        output = tn.read_until(b"#") #Cambia el prompt según el router
        if b"incorrect" in output or b"denied" in output or b"%" in output:
            Messagebox.showerror("Error", "Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
            # print("Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
        else:
            Messagebox.showinfo("Mensaje", "Conexion exitosa del router.")
            # print("Conexion exitosa del router.")

            tn.write(b"show ip access-list\n")
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#") #Cambia el prompt segun el router
            output = output.decode('ascii')
            Messagebox.showinfo("Datos", output)

            # print(output.decode('ascii'))

        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def ConfigNAT(router_ip, username, password):

    try:
        #Crear una conexión Telnet
        tn = telnetlib.Telnet(router_ip)

        #Esperar a que aparezca el prompt de inicion de sesión
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")

        #Espeara a que aprezca el prompt de contraseña
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        #Verificar si la autentificación fue exitosa
        output = tn.read_until(b"#") #Cambia el prompt según el router
        if b"incorrect" in output or b"denied" in output or b"%" in output:
            Messagebox.showerror("Error", "Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
            # print("Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
        else:
            Messagebox.showinfo("Mensaje", "Conexion exitosa del router.")
            # print("Conexion exitosa del router.")

            tn.write(b"terminal length 0\n")
            output = tn.read_until(b"#") 
            #Enviar el comando "show ip interfaces brief"
            tn.write(b"show ip nat translations\n")
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#") #Cambia el prompt segun el router
            output = output.decode('ascii')
            Messagebox.showinfo("Datos", output)
            # print(output.decode('ascii'))

        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def ConfigInterfaces(router_ip, username, password):
    try:
        #Crear una conexión Telnet
        tn = telnetlib.Telnet(router_ip)

        #Esperar a que aparezca el prompt de inicion de sesión
        tn.read_until(b"Username: ")
        tn.write(username.encode('ascii') + b"\n")

        #Espeara a que aprezca el prompt de contraseña
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        #Verificar si la autentificación fue exitosa
        output = tn.read_until(b"#") #Cambia el prompt según el router
        if b"incorrect" in output or b"denied" in output or b"%" in output:
            Messagebox.showerror("Error", "Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
            # print("Error en la autenticacion. Verifica el nombre de usuario y la contraseña.")
        else:
            Messagebox.showinfo("Mensaje", "Conexion exitosa del router.")
            # print("Conexion exitosa del router.")

            #Enviar el comando "show ip interfaces brief"
            tn.write(b"terminal length 0\n")
            output = tn.read_until(b"#") #Cambia el prompt según el router
            tn.write(b"show ip int br\n")
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#")
            #output = tn.read_until(b"!\n!\nend") #Cambia el prompt segun el router
            output = output.decode('ascii')
            # print(output.decode('ascii'))
            Messagebox.showinfo("Datos", output)


        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output


print('Seleccione la opcion que desea visualizar:')
print('1. Configuracion global')
print('2. Configuracion rutas')
print('3. Configuracion DHCP')
print('4. Configuracion ACL')
print('5. Configuracion NAT')
print('6. Configuracion interfaces')

opc = input('')

if opc == '1':
    ConfigGlo(ip_router, USERNAME, PASSWORD)
elif opc == '2':
    ConfigRut(ip_router, USERNAME, PASSWORD)
elif opc == '3':
    ConfigDHCP(ip_router, USERNAME, PASSWORD)
elif opc == '4':
    ConfigACL(ip_router, USERNAME, PASSWORD)
elif opc == '5':
    ConfigNAT(ip_router, USERNAME, PASSWORD)
elif opc == '6':
    ConfigInterfaces(ip_router, USERNAME, PASSWORD)
else:
    print('Hasta luego')