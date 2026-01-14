const form = document.getElementById('formRegistro');

form.addEventListener('submit', async (e) =>{
    e.preventDefault();

    const nombre = document.getElementById("usuarionombre").value;
    const apellidos = document.getElementById("apellidosusuario").value;
    const email = document.getElementById("usuarioemail").value;
    const contraseña = document.getElementById("usuariocontraseña").value;

    let usuariocontraseña = document.getElementById("usuariocontraseña").value;
    let confirmarcontraseña = document.getElementById("confirmarcontraseña").value;

    if (usuariocontraseña != confirmarcontraseña){

        alert("Las contraseñas no coinciden");
        return false;
    }
    
    const datos = {

        "Nombre usuario": nombre,
        "Apellidos usuario": apellidos,
        "Email usuario": email,
        "Rol usuario": "usuario",
        "password": contraseña
        
    }


    try {
        
        const respuesta = await fetch("http://127.0.0.1:5000/Usuario/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        });

        const resultado = await respuesta.json();
        if (respuesta.ok){
            alert("Usuario creado")
        }else {
            alert(resultado.Mensaje)
        }

    } catch (error) {
        alert("Error conectando con el servidor");
        console.log(error);
    }

});



// === Mostrar / ocultar contraseña ===
const toggleButtons = document.querySelectorAll('.toggle-password');

toggleButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetId = button.getAttribute('data-target');
        const input = document.getElementById(targetId);

        if (input.type === 'password') {
            input.type = 'text';
        } else {
            input.type = 'password';
        }
    });
});
