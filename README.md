# Zona Fit Guy

Aplicación sencilla para administrar clientes de un gimnasio. Incluye una interfaz gráfica hecha con Tkinter y un menú de consola. Ambas versiones utilizan MySQL.

## Requisitos

- Python 3.10 o superior
- MySQL Server
- `mysql-connector-python`

## Instalación

Desde la carpeta raíz del proyecto:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

En macOS o Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Configurar MySQL

1. Ejecuta el contenido de `sql/schema.sql` en MySQL Workbench o en el cliente de MySQL.
2. Copia `.env.example` como `.env`.
3. Edita `.env` y escribe la contraseña de tu usuario de MySQL.
4. El proyecto leerá automáticamente las variables del archivo `.env` al iniciar.

En Windows PowerShell:

```powershell
$env:ZONA_FIT_DB_PASSWORD = "tu_password"
```

En macOS o Linux:

```bash
export ZONA_FIT_DB_PASSWORD="tu_password"
```

También puedes definir `ZONA_FIT_DB_NAME`, `ZONA_FIT_DB_USER`, `ZONA_FIT_DB_HOST` y `ZONA_FIT_DB_PORT` si tu instalación utiliza otros valores.

## Ejecutar la aplicación gráfica

Desde la carpeta raíz:

```bash
python zona_fit_gui/app.py
```

## Ejecutar el menú de consola

Desde la carpeta raíz:

```bash
python -m zona_fit_db.menu
```

## Funcionalidades

- Listar clientes
- Agregar clientes
- Modificar clientes
- Eliminar clientes
- Validar los campos del formulario gráfico
