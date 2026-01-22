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

const lista = document.getElementById("lista-productos");

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

renderizarProductos();

document.getElementById("btnAgregar").addEventListener("click", () => {

    let nombre = prompt("Nombre del producto:");
    let precio = prompt("Precio:");
    let descripcion = prompt("Descripción:");

    if (nombre && precio && descripcion) {
        productos.push({
            nombre: nombre,
            precio: precio,
            descripcion: descripcion
        });

        renderizarProductos();
    } else {
        alert("Complete todos los campos");
    }
});
