
HU1 - Validación de datos personales

Como usuario, quiero ingresar correctamente mis datos personales (nombre, fecha de nacimiento y teléfono), para que el sistema los valide y me permita registrarme sin errores.

Criterios de aceptación:

Nombre:Número:

No puede estar vacío.

No debe contener números ni símbolos especiales.

Mínimo 2 caracteres.

Teléfono:

Debe comenzar con “+” seguido del código de país.

Solo debe contener números.

Entre 10 y 15 dígitos.

Fecha de nacimiento:

Debe tener formato válido (DD/MM/AAAA).

Debe validar que el usuario tenga 18 años o más.

HU2 - Validación de Correo Electrónico Como usuario, quiero que el sistema valide correctamente mi correo electrónico, para poder recibir notificaciones importantes sin errores.

Criterios de aceptación:

El correo debe contener un @ y al menos un . después.

El dominio debe ser válido (ej. gmail.com, http://outlook.com ).

No debe contener espacios ni símbolos inválidos.

El campo no puede estar vacío.

HU3 - Validación y confirmación de contraseña

Como usuario, quiero establecer una contraseña segura y confirmarla correctamente, para proteger mi cuenta y evitar accesos no deseados.

Criterios de aceptación:

Contraseña:

Mínimo 8 caracteres.

Al menos una mayúscula, una minúscula, un número y un símbolo.

No debe contener espacios.

Confirmación:

Debe coincidir exactamente con la primera contraseña.

Mostrar error si no coinciden.

HU4 – Mensajes de Error y Control del Formulario

Como usuario, quiero ver mensajes claros de error en cada campo y que el sistema me impida enviar el formulario si hay errores, para saber exactamente qué debo corregir.

Criterios de aceptación:

Cada campo inválido debe mostrar un mensaje específico.

Los errores deben desaparecer al corregir el campo.

El botón “Registrar” debe estar desactivado si hay errores.

El formulario solo se envía si todos los campos están validados correctamente.
