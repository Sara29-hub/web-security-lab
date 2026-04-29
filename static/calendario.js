document.addEventListener("DOMContentLoaded", async () => {
  const calendarEl = document.getElementById("calendar");

  // 1) Cargar tareas del backend y convertirlas a eventos FullCalendar
  async function cargarEventos() {
    const resp = await fetch("/tareas/read");
    if (!resp.ok) throw new Error("No se pudieron cargar las tareas");

    const tareas = await resp.json();

    // Tu backend devuelve keys tipo: Fecha, Nombre_tarea, Contendio_tarea, id
    return tareas.map((t) => ({
      id: String(t.id),
      title: t.Nombre_tarea ?? "Sin título",
      start: t.Fecha,          // "YYYY-MM-DD"
      allDay: true,
      extendedProps: {
        contenido: t.Contendio_tarea ?? ""
      }
    }));
  }

  // 2) Crear tarea en backend
  async function crearTarea({ nombre, contenido, fecha }) {
    const resp = await fetch("/tareas/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        Nombre: nombre,
        Contenido: contenido,
        Fecha: fecha, // YYYY-MM-DD
      }),
    });

    const data = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      throw new Error(data.Mensaje || "Error al crear la tarea");
    }
    return data;
  }

  // Cargar eventos iniciales
  let eventosIniciales = [];
  try {
    eventosIniciales = await cargarEventos();
  } catch (e) {
    console.error(e);
    // No bloqueamos el calendario: lo cargamos vacío
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

    // Click en evento -> mostrar contenido (simple)
    eventClick: (info) => {
      const contenido = info.event.extendedProps.contenido || "";
      alert(`${info.event.title}\n\n${contenido}`);
    },

    // Seleccionar un día o rango -> crear tarea y pintarla
    select: async (info) => {
      const fecha = info.startStr; // en month view suele ser YYYY-MM-DD

      const nombre = prompt("Nombre de la tarea:");
      if (!nombre) return;

      const contenido = prompt("Contenido (opcional):") || "";

      try {
         const data = await crearTarea({ nombre, contenido, fecha });

        // Añadir en el calendario sin recargar
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
