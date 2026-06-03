document.addEventListener("DOMContentLoaded", async () => {
  const calendarEl = document.getElementById("calendar");

  
  async function cargarEventos() {
    const resp = await fetch("/tareas/read");
    if (!resp.ok) throw new Error("No se pudieron cargar las tareas");

    const tareas = await resp.json();

    
    return tareas.map((t) => ({
      id: String(t.id),
      title: t.Nombre_tarea ?? "Sin título",
      start: t.Fecha,          
      allDay: true,
      extendedProps: {
        contenido: t.Contendio_tarea ?? ""
      }
    }));
  }

  
  async function crearTarea({ nombre, contenido, fecha }) {
    const resp = await fetch("/tareas/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        Nombre: nombre,
        Contenido: contenido,
        Fecha: fecha, 
      }),
    });

    const data = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      throw new Error(data.Mensaje || "Error al crear la tarea");
    }
    return data;
  }

 
  let eventosIniciales = [];
  try {
    eventosIniciales = await cargarEventos();
  } catch (e) {
    console.error(e);
    
  }

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridMonth",
    locale: "es",
    headerToolbar: {
      left: "prev,next today",
      center: "title",
      right: "dayGridMonth,timeGridWeek,listWeek",
    },
    selectable: true,
    events: eventosIniciales,

    
    eventClick: (info) => {
      const contenido = info.event.extendedProps.contenido || "";
      alert(`${info.event.title}\n\n${contenido}`);
    },

    
    select: async (info) => {
      const fecha = info.startStr; 

      const nombre = prompt("Nombre de la tarea:");
      if (!nombre) return;

      const contenido = prompt("Contenido (opcional):") || "";

      try {
         const data = await crearTarea({ nombre, contenido, fecha });

        
        calendar.addEvent({
          id: String(data.id),
          title: nombre,
          start: fecha,
          allDay: true,
          extendedProps: { contenido },
        });

      } catch (e) {
        alert(e.message);
        console.error(e);
      } finally {
        calendar.unselect();
      }
    },
  });

  calendar.render();
});
