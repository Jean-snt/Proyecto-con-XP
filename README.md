HISTORIA DE USUARIO : VALIDACION DE DATOS DE USUARIO

Título: Registro seguro de nuevos usuarios

Como sistema de gestión de usuarios,

quiero validar automáticamente los datos ingresados en el formulario de registro (nombre, correo electrónico y teléfono),

para que solo se almacren registros completos y con formato correcto, evitando errores de datos y garantizando la calidad de la información.

Criterios de Aceptación:

Nombre obligatorio:

Dado que el usuario abre el formulario de registro,

cuando deja el campo “Nombre” en blanco y envía el formulario,

entonces el sistema muestra el mensaje de error “El nombre no puede estar vacío.”

Formato de correo válido:

Dado que el usuario ingresa un correo sin @ o sin dominio (.),

cuando envía el formulario,

entonces el sistema muestra el mensaje de error “El correo no es válido.”

Teléfono con prefijo internacional:

Dado que el usuario ingresa un número de teléfono sin un + seguido de código de país y dígitos,

cuando envía el formulario,

entonces el sistema muestra el mensaje de error “El teléfono debe incluir un prefijo internacional (p. ej. +51) y solo dígitos.”

Registro exitoso:

Dado que todos los campos cumplen sus validaciones,

cuando el usuario envía el formulario,

entonces el sistema acepta la solicitud y devuelve { "status": "success", "message": "Registro correcto" }.
