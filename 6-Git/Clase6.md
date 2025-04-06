# Git y Github

## ¿Qué es Git y Github?
Git es un sistema de control de versiones distribuido que permite llevar un seguimiento de los cambios en los archivos y colaborar con otros desarrolladores. Es ampliamente utilizado en el desarrollo de software y es una herramienta esencial para cualquier programador.

Github es una plataforma de alojamiento de código que utiliza Git como sistema de control de versiones. Permite a los desarrolladores almacenar su código en la nube, colaborar con otros y gestionar proyectos de software. Github también ofrece características adicionales como seguimiento de problemas, revisiones de código y documentación.

### Configuración de Git

Para instalar git puedes consultar la [Introducción a la línea de comandos](../2-IntroduccionLineaComandos/Clase2.md)

Lo primero que debes hacer es configurar tu nombre y correo electrónico. Esto es importante porque cada vez que hagas un commit, Git registrará esta información.

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "Tu correo"
```

Ejemplo:

```bash
git config --global user.name "Jesús"
git config --global user.email "ejemplo@gmail.com"
```
Nota: Las comillas son necesarias para que Git reconozca el nombre y correo como una cadena de texto. Si no las pones, Git no podrá identificar tu nombre y correo.

### Iniciar un repositorio
Para iniciar un nuevo repositorio, navega a la carpeta donde deseas crear el repositorio y ejecuta el siguiente comando:

```bash
git init
```
Esto creará una nueva carpeta oculta llamada `.git` en la carpeta actual. Esta carpeta contiene toda la información necesaria para el control de versiones del proyecto.

### Agregar archivos al repositorio
Para agregar archivos al repositorio, utiliza el siguiente comando:

```bash
git add nombre_del_archivo
```
Ejemplo:

```bash
git add Clase6.md
```
Esto agregará el archivo `Clase6.md` al área de preparación (staging area). Puedes agregar varios archivos a la vez utilizando un espacio entre los nombres de los archivos.
```bash
git add Clase6.md Ejercicios/ejercicios.md
```
También puedes agregar todos los archivos del directorio actual utilizando el siguiente comando:

```bash
git add .
```
Esto agregará todos los archivos y carpetas del directorio actual al área de preparación.
### Hacer un commit
Un commit es una instantánea de los archivos en el área de preparación. Para hacer un commit, utiliza el siguiente comando:

```bash
git commit -m "Mensaje del commit"
```
Ejemplo:

```bash
git commit -m "Agregando la clase 6"
```
Esto creará un nuevo commit con los archivos que has agregado al área de preparación. El mensaje del commit debe ser descriptivo y explicar los cambios realizados en el commit.
### Ver el estado del repositorio
Para ver el estado del repositorio, utiliza el siguiente comando:

```bash
git status
```
Esto mostrará información sobre los archivos que han sido modificados, agregados o eliminados desde el último commit. También mostrará si hay archivos en el área de preparación o si hay cambios sin agregar.
### Ver el historial de commits
Para ver el historial de commits, utiliza el siguiente comando:

```bash
git log
```
Esto mostrará una lista de todos los commits realizados en el repositorio, junto con la información del autor, la fecha y el mensaje del commit. Puedes usar las teclas de flecha para desplazarte por el historial y `q` para salir.
### Crear un repositorio en Github
Para crear un nuevo repositorio en Github, sigue estos pasos:
1. Inicia sesión en tu cuenta de Github.
2. Haz clic en el botón "New" o "Crear nuevo repositorio".
3. Ingresa un nombre para tu repositorio y una descripción opcional.
4. Selecciona si deseas que el repositorio sea público o privado.
5. Haz clic en el botón "Crear repositorio".

### Conectar el repositorio local con el remoto
Para conectar tu repositorio local con el repositorio remoto en Github, utiliza el siguiente comando:

```bash
git remote add origin main https://github.com/usuario/nombre_del_repositorio.git
```

### Subir cambios al repositorio remoto
Para subir los cambios al repositorio remoto, utiliza el siguiente comando:

```bash
git push origin main
```
Esto subirá los cambios al repositorio remoto en Github. Si es la primera vez que subes cambios, es posible que debas ingresar tu nombre de usuario y contraseña de Github.

### Ciclo de vida de un commit

El ciclo de vida de un commit en Git se puede resumir en los siguientes pasos:
1. **Modificación**: Realizas cambios en los archivos de tu proyecto.
2. **Adición**: Agregas los archivos modificados al área de preparación utilizando `git add`.
3. **Commit**: Realizas un commit utilizando `git commit -m "Mensaje del commit"`.
4. **Push**: Subes los cambios al repositorio remoto utilizando `git push origin main`.
5. **Pull**: Si trabajas en equipo, puedes obtener los cambios realizados por otros utilizando `git pull origin main`.
