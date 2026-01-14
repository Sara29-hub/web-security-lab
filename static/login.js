const form = document.getElementById("formLogin");

form.addEventListener('submit', async (e) =>{
    e.preventDefault();

    const email = document.getElementById("email").value;
    const contraseña = document.getElementById("contraseña").value;

    const datos = {

        "email": email,
        "password": contraseña

    }

    try {
        
        const respuesta = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        });

        const resultado =  await respuesta.json();
        if (respuesta.ok){
            window.location.href = "/tasks";
        }else{
            alert("Error al logearse")
        }


    } catch (error) {
        alert("Error conectando con el servidor");
        console.log(error);
    }


})