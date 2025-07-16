const form = document.getElementById("validacion-form");
const lista = document.getElementById("lista-usuarios");

document.addEventListener("DOMContentLoaded", () => {
  cargarUsuarios();

  const borrarBtn = document.getElementById("borrar-datos");
  if (borrarBtn) {
    borrarBtn.addEventListener("click", () => {
      if (confirm("¿Seguro que quieres borrar todos los registros?")) {
        fetch("http://localhost:5000/borrar-todo", {
          method: "DELETE"
        })
        .then(res => res.json())
        .then(data => {
          alert(data.mensaje);
          cargarUsuarios(); // Recargar la lista
        })
        .catch(error => {
          alert("Error al intentar borrar los registros.");
          console.error(error);
        });
      }
    });
  }
});

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const nombre = document.getElementById("nombre").value.trim();
  const email = document.getElementById("email").value.trim();
  const telefono = document.getElementById("telefono").value.trim();

  fetch("http://localhost:5000/registrar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ nombre, email, telefono })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        alert("Usuario registrado correctamente.");
        form.reset();
        cargarUsuarios();
      }
    })
    .catch(error => {
      alert("Error al conectar con el servidor.");
      console.error(error);
    });
});

function cargarUsuarios() {
  fetch("http://localhost:5000/usuarios")
    .then(res => res.json())
    .then(data => {
      lista.innerHTML = "";

      if (data.length === 0) {
        lista.innerHTML = "<li>No hay usuarios registrados.</li>";
        return;
      }

      data.forEach(u => {
        const item = document.createElement("li");
        item.innerHTML = `
          <strong>Nombre:</strong> ${u.nombre} <br>
          <strong>Email:</strong> ${u.email} <br>
          <strong>Teléfono:</strong> ${u.telefono} <br>
          <small><em>${u.fecha}</em></small>`;
        lista.appendChild(item);
      });
    })
    .catch(err => {
      lista.innerHTML = "<li>Error al cargar los usuarios.</li>";
      console.error(err);
    });
}
