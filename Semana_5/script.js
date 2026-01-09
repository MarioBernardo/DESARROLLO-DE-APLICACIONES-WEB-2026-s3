const gallery = document.querySelector("#gallery");
const imageInput = document.querySelector("#imageInput");
const message = document.querySelector("#message");
const counter = document.querySelector("#counter");

let selectedId = null;
let imageCount = 0;

/* VALIDAR URL */
function isValidUrl(url) {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}

/* ACTUALIZAR CONTADOR */
function updateCounter() {
  counter.textContent = `${imageCount} imágenes`;
}

/* AGREGAR IMAGEN */
document.querySelector("#btnAdd").addEventListener("click", () => {
  const url = imageInput.value.trim();

  if (!isValidUrl(url)) {
    message.textContent = "URL no válida.";
    message.className = "text-danger";
    return;
  }

  imageCount++;

  const figure = document.createElement("figure");
  const img = document.createElement("img");

  img.src = url;
  img.dataset.id = imageCount;
  img.classList.add("fade-in");

  figure.appendChild(img);
  gallery.appendChild(figure);

  imageInput.value = "";
  message.textContent = "Imagen agregada correctamente.";
  message.className = "text-success";

  updateCounter();
});

/* SELECCIÓN (delegación de eventos) */
gallery.addEventListener("click", (e) => {
  if (e.target.tagName !== "IMG") return;

  document
    .querySelectorAll(".gallery img")
    .forEach(img => img.classList.remove("selected"));

  e.target.classList.add("selected");
  selectedId = e.target.dataset.id;
});

/* ELIMINAR IMAGEN */
document.querySelector("#btnDelete").addEventListener("click", () => {
  if (!selectedId) {
    message.textContent = "No hay imagen seleccionada.";
    message.className = "text-warning";
    return;
  }

  const imgToRemove = document.querySelector(
    `img[data-id="${selectedId}"]`
  );

  imgToRemove.parentElement.remove();
  selectedId = null;
  imageCount--;

  updateCounter();
});

/* ATAJOS DE TECLADO */
document.addEventListener("keydown", (e) => {
  if (e.key === "Delete") {
    document.querySelector("#btnDelete").click();
  }
});
