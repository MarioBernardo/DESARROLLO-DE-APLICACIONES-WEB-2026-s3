// Lista de productos
let productos = [
    {
        nombre: "Laptop",
        precio: 800,
        descripcion: "Laptop para trabajo y estudio"
    },
    {
        nombre: "Mouse",
        precio: 15,
        descripcion: "Mouse inalámbrico"
    },
    {
        nombre: "Teclado",
        precio: 25,
        descripcion: "Teclado mecánico"
    }
];

// Referencia al UL
const lista = document.getElementById("lista-productos");

// Función para mostrar productos
function renderizarProductos() {
    lista.innerHTML = "";

    productos.forEach(producto => {
        const li = document.createElement("li");

        li.innerHTML = `
            <strong>${producto.nombre}</strong><br>
            Precio: $${producto.precio}<br>
            ${producto.descripcion}
        `;

        lista.appendChild(li);
    });
}

// Cargar productos al iniciar
document.addEventListener("DOMContentLoaded", renderizarProductos);

// Agregar nuevo producto
document.getElementById("btnAgregar").addEventListener("click", () => {

    let nombre = prompt("Ingrese el nombre del producto:");
    let precio = prompt("Ingrese el precio:");
    let descripcion = prompt("Ingrese la descripción:");

    if (nombre && precio && descripcion) {
        const nuevoProducto = {
            nombre: nombre,
            precio: precio,
            descripcion: descripcion
        };

        productos.push(nuevoProducto);
        renderizarProductos();
    } else {
        alert("Debe completar todos los datos");
    }
});
