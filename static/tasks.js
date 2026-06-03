
function toggleMenu() {
    console.log("Clica en el perfil...");
    const dropdown = document.getElementById("userDropdown");
    dropdown.classList.toggle("show");
}


window.onclick = function(event) {
    if (!event.target.closest('.user-section')) {
        const dropdown = document.getElementById("userDropdown");
        if (dropdown && dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
        }
    }
}


document.addEventListener('DOMContentLoaded', () => {
    const btnLogout = document.getElementById('btnLogout');
    
    if (btnLogout) {
        btnLogout.addEventListener('click', (e) => {
            e.preventDefault();
            console.log("Cerrando sesión...");

            fetch('/logout') 
                .then(() => {
                    window.location.href = "/"; 
                })
                .catch(err => console.error("Error al salir:", err));
        });
    }
});