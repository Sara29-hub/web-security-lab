// 1. Función para mostrar/ocultar el menú al pinchar en "Profesor"
function toggleMenu() {
    console.log("Clica en el perfil...");
    const dropdown = document.getElementById("userDropdown");
    dropdown.classList.toggle("show");
}

// 2. Cerrar el menú si el usuario pincha fuera de él
window.onclick = function(event) {
    if (!event.target.closest('.user-section')) {
        const dropdown = document.getElementById("userDropdown");
        if (dropdown && dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
        }
    }
}

// 3. Lógica del botón de Logout
document.addEventListener('DOMContentLoaded', () => {
    const btnLogout = document.getElementById('btnLogout');
    
    if (btnLogout) {
        btnLogout.addEventListener('click', (e) => {
            e.preventDefault();
            console.log("Cerrando sesión...");

            fetch('/logout') // Llama a tu ruta en Python
                .then(() => {
                    window.location.href = "/"; // Redirige al login
                })
                .catch(err => console.error("Error al salir:", err));
        });
    }
});