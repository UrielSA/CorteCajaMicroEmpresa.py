import tkinter as tk
import smtplib
from tkinter import messagebox

ventana=tk.Tk()
ventana.geometry("500x1000+1+1")
ventana.resizable(False,False)




letras= ("arial",15);
color= ("#03AAA7")
importante= ("#AA0303")

#texto Titulo

titulo=tk.Label(ventana,text=("Ciber Bullis"),font=letras,fg=color)
titulo.pack()

#subtitulo
Subtitulo=tk.Label(ventana,text=("Corte Cajas"), font=("arial",20), fg=importante)
Subtitulo.pack()

#tu nombre
nombre=tk.Label(ventana, text="Escribe tu nombre")
nombre.pack()

nombre_ent=tk.Entry(ventana)
nombre_ent.pack()

#texto caja cobro
cobro_txt=tk.Label(ventana,text=("Cobro Billetes"),font=letras,fg=importante)
cobro_txt.pack()

#entrada Cobro
cobro_ent=tk.Entry(ventana)
cobro_ent.pack()

cobro_txt_monedas=tk.Label(ventana,text=("Cobro Monedas"), font=letras,fg=importante)
cobro_txt_monedas.pack()

cobro_ent_monedas=tk.Entry(ventana)
cobro_ent_monedas.pack()

#texto caja wifi
wifi_txt=tk.Label(ventana,text="Wifi Billetes",font=letras,fg=importante)
wifi_txt.pack()

#entrada wifi
wifi_ent=tk.Entry(ventana)
wifi_ent.pack()

wifi_txt_monedas=tk.Label(text="Wifi Monedas",font=letras,fg=importante)
wifi_txt_monedas.pack()

wifi_ent_monedas=tk.Entry(ventana)
wifi_ent_monedas.pack()

#texto caja tienda

tienda_txt=tk.Label(ventana,text="Tienda Billetes",font=letras,fg=importante)
tienda_txt.pack()


#entarda tienda

tienda_ent=tk.Entry(ventana)
tienda_ent.pack()

tienda_txt_Monedas=tk.Label(text="Tienda Monedas",font=letras,fg=importante )
tienda_txt_Monedas.pack()

tienda_ent_monedas=tk.Entry(ventana)
tienda_ent_monedas.pack()

Pago_Trab=tk.Label(ventana,text="cuanto te cobraste en monedas",fg=importante)
Pago_Trab.pack()

pago_monedas_ent=tk.Entry(ventana)
pago_monedas_ent.insert(0,"0")
pago_monedas_ent.pack()  

pago_billetes=tk.Label(ventana,text="cuanto te cobraste en billetes",fg=importante)
pago_billetes.pack()

pago_billetes_ent=tk.Entry(ventana)
pago_billetes_ent.insert(0,"0")
pago_billetes_ent.pack()

def suma():
    cobroinfBilletes = float( cobro_ent.get())
    cobroinfMonedas = float(cobro_ent_monedas.get())

    wifiinfBilletes = float(wifi_ent.get())
    wifiinfMonedas = float(wifi_ent_monedas.get())

    tiendainfBilletes=float( tienda_ent.get())
    tiendainfMonedas=float(tienda_ent_monedas.get())

    pagoinfBilletes = float(pago_billetes_ent.get())
    pagoinfMonedas = float(pago_monedas_ent.get())

    cobro=float(cobro_ent.get())
    wifi = float(wifi_ent.get())
    tienda= float(tienda_ent.get())
    CobroMonedas=float(cobro_ent_monedas.get())
    WifiMonedas=float(wifi_ent_monedas.get())
    TiendaMonedas=float(tienda_ent_monedas.get())
    PagoMonedas=float(pago_monedas_ent.get())
    PagoBilletes=float(pago_billetes_ent.get())
    cobro=float(cobro_ent.get())
    wifi = float(wifi_ent.get())
    tienda= float(tienda_ent.get())
    CobroMonedas=float(cobro_ent_monedas.get())
    WifiMonedas=float(wifi_ent_monedas.get())
    TiendaMonedas=float(tienda_ent_monedas.get())
    PagoMonedas=float(pago_monedas_ent.get())
    PagoBilletes=float(pago_billetes_ent.get())
   

    TotalDinero= cobro + wifi + tienda + CobroMonedas + WifiMonedas + TiendaMonedas - PagoMonedas - PagoBilletes
    Total_monedas= WifiMonedas + TiendaMonedas + CobroMonedas - PagoMonedas
    Billetes = cobro + wifi + tienda - PagoBilletes
    totaldinero= cobro + wifi + tienda + CobroMonedas + WifiMonedas + TiendaMonedas 
    TotalPago=PagoBilletes + PagoMonedas
    totalcobro= cobro + CobroMonedas
    totalwifi= wifi + WifiMonedas
    totalTienda= tienda + TiendaMonedas
    totalbilletes=cobro + wifi + tienda 
    
    
    resultado_lbl.config(text=f"Billetes en Cobro:{cobroinfBilletes} $\nMonedas en Cobro:{cobroinfMonedas} $\n____________ \nTotal: {totalcobro} $\n\nBilletes wifi:{wifiinfBilletes } $\nMonedas wifi:{wifiinfMonedas} $\n____________ \n Total: {totalwifi} $\n\nTienda Billetes : {tiendainfBilletes} $\nTienda Monedas:{tiendainfMonedas} $\n____________ \n total: {totalTienda} $\n \nTotal billetes: {totalbilletes} $ \n \nTu trabajador se cobro {TotalPago} $\n \n Tu trabajador tomo en monedas: {PagoMonedas} $\n \n Tu trabajador tomo en billetes: {PagoBilletes} $\n \ntotal menos paga: {TotalDinero} $ \nQuedan billetes en caja: {Billetes} $\n Quedan Monedas en caja: {Total_monedas} $")
    

btn=tk.Button(ventana,text=("Suma total"),command=suma,fg=importante)
btn.pack()

resultado_lbl=tk.Label(ventana,text=("Resultado"))
resultado_lbl.pack()

# Función para enviar el correo electrónico
def enviar_correo():
    # Configura la conexión SMTP
    smtp_server = 'smtp.office365.com'  # Reemplaza con el servidor SMTP adecuado
    smtp_port = 587  # Reemplaza con el puerto SMTP adecuado
    smtp_username = 'cookiesone1@hotmail.com'  # Reemplaza con tu dirección de correo electrónico
    smtp_password = 'GiioGalleta25Y1'  # Reemplaza con tu contraseña de correo electrónico

    # Crea una conexión SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Obtiene los datos del formulario
        destinatario = "bullisliopuren@gmail.com"

        quienManda = nombre_ent.get()

        cobroinfBilletes = float( cobro_ent.get())
        cobroinfMonedas = float(cobro_ent_monedas.get())

        wifiinfBilletes = float(wifi_ent.get())
        wifiinfMonedas = float(wifi_ent_monedas.get())

        tiendainfBilletes=float( tienda_ent.get())
        tiendainfMonedas=float(tienda_ent_monedas.get())

        pagoinfBilletes = float(pago_billetes_ent.get())
        pagoinfMonedas = float(pago_monedas_ent.get())

        cobro=float(cobro_ent.get())
        wifi = float(wifi_ent.get())
        tienda= float(tienda_ent.get())
        CobroMonedas=float(cobro_ent_monedas.get())
        WifiMonedas=float(wifi_ent_monedas.get())
        TiendaMonedas=float(tienda_ent_monedas.get())
        PagoMonedas=float(pago_monedas_ent.get())
        PagoBilletes=float(pago_billetes_ent.get())
   

        TotalDinero= cobro + wifi + tienda + CobroMonedas + WifiMonedas + TiendaMonedas - PagoMonedas - PagoBilletes
        Total_monedas= WifiMonedas + TiendaMonedas + CobroMonedas - PagoMonedas
        Billetes = cobro + wifi + tienda - PagoBilletes
        totaldinero= cobro + wifi + tienda + CobroMonedas + WifiMonedas + TiendaMonedas 
        TotalPago=PagoBilletes + PagoMonedas
        totalcobro= cobro + CobroMonedas
        totalwifi= wifi + WifiMonedas
        totalTienda= tienda + TiendaMonedas
        totalbilletes=cobro + wifi + tienda 

       

        
        # Crea el correo electrónico
        correo = f"Subject: {quienManda}\nTo: {destinatario}\n\nBilletes en Cobro:{cobroinfBilletes} $\nMonedas en Cobro:{cobroinfMonedas} $\n____________ \nTotal: {totalcobro} $\n\nBilletes wifi:{wifiinfBilletes } $\nMonedas wifi:{wifiinfMonedas} $\n____________ \n Total: {totalwifi} $\n\nTienda Billetes : {tiendainfBilletes} $\nTienda Monedas:{tiendainfMonedas} $\n____________ \n total: {totalTienda} $\n \nTotal billetes: {totalbilletes} $ \n \nTu trabajador se cobro {TotalPago} $\n \n Tu trabajador tomo en monedas: {PagoMonedas} $\n \n Tu trabajador tomo en billetes: {PagoBilletes} $\n \ntotal menos paga: {TotalDinero} $ \nQuedan billetes en caja: {Billetes} $\n Quedan Monedas en caja: {Total_monedas} $"

        # Envía el correo electrónico
        server.sendmail(smtp_username, destinatario, correo)
        server.quit()

        messagebox.showinfo("Éxito", "Correo electrónico enviado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo electrónico: {str(e)}")
        
        
    

enviar_button = tk.Button(ventana, text="Enviar", command=enviar_correo, height=2,width=5,border=5,bg="#C5FDFC")
enviar_button.pack()

ventana.mainloop()