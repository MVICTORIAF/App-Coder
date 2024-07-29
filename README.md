# Academia Mundos Creativos

Este es un proyecto Django para una academia que incluye secciones para alumnos, profesores y cursos.




## Modelos

### Alumno
- **nombre**: Nombre del alumno (CharField)
- **edad**: Edad del alumno (IntegerField)
- **curso**: Curso del alumno (CharField)

### Profesor
- **nombre**: Nombre del profesor (CharField)
- **especialidad**: Especialidad del profesor (CharField)
- **experiencia**: Años de experiencia del profesor (IntegerField)

### Curso
- **nombre**: Nombre del curso (CharField)
- **descripcion**: Descripción del curso (TextField)
- **profesor**: Profesor asignado al curso (ForeignKey a Profesor)

## Formularios

### Alumno
Formulario para ingresar datos del alumno.

### Profesor
Formulario para ingresar datos del profesor.

### Curso
Formulario para ingresar datos del curso.

## Navegación

El sitio incluye las siguientes secciones en la barra de navegación:
- **Inicio**
- **Alumnos**
- **Profesores**
- **Cursos**
