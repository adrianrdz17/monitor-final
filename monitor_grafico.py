import telnetlib
import tkinter as tk
from tkinter import messagebox as Messagebox
from PIL import Image

class RouterConfigApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Configuración de Router")
        
        self.label_ip = tk.Label(master, text="Dirección IP del router:")
        self.label_ip.pack()

        self.entry_ip = tk.Entry(master)
        self.entry_ip.pack()

        self.label_username = tk.Label(master, text="Nombre de usuario:")
        self.label_username.pack()

        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_password = tk.Label(master, text="Contraseña:")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.button_connect = tk.Button(master, text="Conectar", command=self.connect_router)
        self.button_connect.pack()

        self.label_option = tk.Label(master, text="Seleccione la opción que desea visualizar:")
        self.label_option.pack()

        self.options = [
            "Configuración global",
            "Configuración rutas",
            "Configuración DHCP",
            "Configuración ACL",
            "Configuración NAT",
            "Configuración interfaces",
            "Configuracion RMON"
        ]

        self.selected_option = tk.StringVar(master)
        self.selected_option.set(self.options[0])

        self.option_menu = tk.OptionMenu(master, self.selected_option, *self.options)
        self.option_menu.pack()

        self.button_execute = tk.Button(master, text="Ejecutar", command=self.execute_option)
        self.button_execute.pack()

        self.text_result = tk.Text(master, height=10, width=70)
        self.text_result.pack()

        image_path_jpg = './img/Topologia.jpeg'
        image_ppm = self.convert_jpg_to_ppm(image_path_jpg)
        self.photo = tk.PhotoImage(data=image_ppm)
        self.label_image = tk.Label(master, image=self.photo)
        self.label_image.pack()

    def convert_jpg_to_ppm(self, image_path):
        image = Image.open(image_path)
        ppm_image_path = 'temp_image.ppm'
        image.save(ppm_image_path, 'ppm')
        with open(ppm_image_path, 'rb') as ppm_file:
            image_ppm = ppm_file.read()
        return image_ppm

    def connect_router(self):
        ip_router = self.entry_ip.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not ip_router or not username or not password:
            Messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Llama a la función correspondiente según la opción seleccionada
        option = self.selected_option.get()
        if option == "Configuración global":
            result = global_config(ip_router, username, password)
        elif option == "Configuración rutas":
            result = route_config(ip_router, username, password)
        elif option == "Configuración DHCP":
            result = dhcp_config(ip_router, username, password)
        elif option == "Configuración ACL":
            result = acl_config(ip_router, username, password)
        elif option == "Configuración NAT":
            result = nat_config(ip_router, username, password)
        elif option == "Configuración interfaces":
            result =interface_config(ip_router, username, password)
        elif option == "Configuracion RMON":
            result = rmon_config(ip_router, username, password)
        
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, result)

    def execute_option(self):
        self.connect_router()

def global_config(router_ip, username, password):
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
            # Messagebox.showinfo("Datos", output)


        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def route_config(router_ip, username, password):

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

def dhcp_config(router_ip, username, password):

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

def acl_config(router_ip, username, password):

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
            # Messagebox.showinfo("Datos", output)

            # print(output.decode('ascii'))

        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def nat_config(router_ip, username, password):

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
            # Messagebox.showinfo("Datos", output)
            # print(output.decode('ascii'))

        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def interface_config(router_ip, username, password):
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
            # Messagebox.showinfo("Datos", output)


        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output

def rmon_config(router_ip, username, password):
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
            tn.write(b"show rmon events\n")
            #Leer y mostrar la salida del comando
            output = tn.read_until(b"#")
            #output = tn.read_until(b"!\n!\nend") #Cambia el prompt segun el router
            output = output.decode('ascii')
            # print(output.decode('ascii'))
            # Messagebox.showinfo("Datos", output)


        #Cerrrar la conexion Telnet
        tn.close()

    except Exception as e:
        Messagebox.showerror("Error al conectarse con el router", str(e))
        # print("Error al conectarse al router:", str(e))
    return output


if __name__ == "__main__":
    root = tk.Tk()
    app = RouterConfigApp(root)
    root.mainloop()