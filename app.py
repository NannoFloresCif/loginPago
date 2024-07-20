from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
# -----------------------------------------------------------------------------------------
@app.route("/calculoCompras", methods= ["GET","POST"])
def compras():
    total = 0
    nombre = None
    edad = None
    descuento = 0
    cobro = 0
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros_pintura = int(request.form["tarros_pintura"])

        total = tarros_pintura*9000

        if edad >=18 and edad<=30:
            descuento = total * 0.15
        elif edad >30:
            descuento = total * 0.25
        else:
            descuento = 0

        cobro = total - descuento
             


    return render_template("calculo_compras.html", nombre = nombre, total = total, descuento = descuento, cobro = cobro)

#-------------------------------------------------------------------------------------------------

users = {
    "juan": "admin",
    "pepe": "user"
}

@app.route("/inicioSesion", methods= ["GET","POST"])
def sesion():
    mensaje = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        contrasena = request.form["contrasena"]
       
        try:
            if users[nombre]==contrasena and nombre =="juan":
                mensaje =f"Bienvenido administrador {nombre}"
            
            elif users[nombre]==contrasena and nombre =="pepe":
                mensaje =f"Bienvenido usuario {nombre}"
        except:
            mensaje = "Usuario o contraseña incorrectos"
            
    return render_template("inicio_sesion.html", mensaje = mensaje)
        


if __name__ == '__main__':
    app.run(debug=True)