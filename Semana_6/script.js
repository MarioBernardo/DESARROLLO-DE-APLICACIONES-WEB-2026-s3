const nombre = document.getElementById("nombre");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const edad = document.getElementById("edad");
const btnEnviar = document.getElementById("btnEnviar");
const form = document.getElementById("registroForm");

function marcar(input, valido, errorId, mensaje) {
    const error = document.getElementById(errorId);
    if (valido) {
        input.classList.add("valido");
        input.classList.remove("invalido");
        error.textContent = "";
        return true;
    } else {
        input.classList.add("invalido");
        input.classList.remove("valido");
        error.textContent = mensaje;
        return false;
    }
}

function validarNombre() {
    return marcar(nombre, nombre.value.trim().length >= 3, "errorNombre", "Mínimo 3 caracteres");
}

function validarEmail() {
    const r = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return marcar(email, r.test(email.value), "errorEmail", "Correo inválido");
}

function validarPassword() {
    const r = /^(?=.*\d)(?=.*[^\w\s]).{8,}$/;
    return marcar(
        password,
        r.test(password.value),
        "errorPassword",
        "8 caracteres, número y símbolo"
    );
}

function validarConfirmPassword() {
    return marcar(
        confirmPassword,
        confirmPassword.value === password.value && confirmPassword.value !== "",
        "errorConfirmPassword",
        "No coinciden"
    );
}

function validarEdad() {
    return marcar(
        edad,
        Number(edad.value) >= 18,
        "errorEdad",
        "Debe ser mayor de edad"
    );
}

function validarFormulario() {
    const ok =
        validarNombre() &&
        validarEmail() &&
        validarPassword() &&
        validarConfirmPassword() &&
        validarEdad();

    btnEnviar.disabled = !ok;
}

[nombre, email, password, confirmPassword, edad].forEach(campo => {
    campo.addEventListener("input", validarFormulario);
});

form.addEventListener("submit", e => {
    e.preventDefault();
    alert("Formulario creado correctamente ✅");
});

form.addEventListener("reset", () => {
    btnEnviar.disabled = true;
});
