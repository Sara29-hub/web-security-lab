/*function comprobarClave(){
    event.preventDefault();

    let usuariocontraseña = document.getElementById("contraseña").value;
    let confirmarcontraseña = document.getElementById("confirmarcontraseña").value;

    if (usuariocontraseña != confirmarcontraseña){

        alert("Las contraseñas no coinciden");
        return false;
    }
    alert("Contraseñas correctas. Procediendo con el registro")
    document.getElementById("formRegistro").submit()
}
 

document.getElementById("formRegistro").addEventListener("submit", async function(event){
    event.preventDefault(); // Evita recargar la página

    // 1️⃣ Recoger datos del formulario
    const nombre = document.getElementById("usuarionombre").value;
    const apellidos = document.getElementById("apellidosusuario").value;
    const email = document.getElementById("usuarioemail").value;
    const contraseña = document.getElementById("usuariocontraseña").value;

    // 2️⃣ Crear el JSON que se enviará al backend
    const datos = {
        "Nombre usuario": nombre,
        "Apellidos usuario": apellidos,
        "Email usuario": email,
        "password": contraseña
    };

    try {
        // 3️⃣ Enviar con fetch
        const respuesta = await fetch("http://127.0.0.1:5000/Usuario/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        });

        const resultado = await respuesta.json();
        alert(resultado.Mensaje); // Se muestra lo que devuelve el backend

    } catch (error) {
        alert("Error conectando con el servidor");
        console.log(error);
    }
});*/
