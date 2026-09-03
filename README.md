# Servicio FastAPI: /obtenercedula

Endpoint que devuelve un número entero aleatorio de 10 dígitos (entre 1000000000 y 9999999999).

Requisitos:

- Python 3.8+
- Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Ejecutar:

```bash
python main.py
# o
uvicorn main:app --reload
```

Ejemplo de respuesta:

```json
{"cedula": 1234567890}
```

Docker
------

Se provee un `Dockerfile` y un `docker-compose.yml` para ejecutar el servicio en contenedor.

Construir la imagen localmente:

```bash
docker build -t obtenercedula:latest .
```

Ejecutar con Docker:

```bash
docker run -p 8000:8000 obtenercedula:latest
```

Ejecutar con Docker Compose:

```bash
docker-compose up --build
```

Payload / Respuesta
-------------------

Endpoint: `GET /obtenercedula`

Respuesta (ejemplo):

```json
{
	"cedula": 8743920175
}
```

Postman
-------

Incluyo una colección de Postman para importar y probar el endpoint, y un environment con la variable `baseUrl` y `usuario`.

- Colección: `postman_collection.json`
- Environment: `postman_environment.json`

Importar la colección en Postman y usar la variable `{{baseUrl}}` (por defecto `http://localhost:8000`).

Notas
-----

El servicio no requiere autenticación; la variable `usuario` en el environment es meramente de ejemplo.

Despliegue continuo a Render (GitHub Actions)
-------------------------------------------

Sigue estos pasos para habilitar despliegue continuo hacia el servicio gratuito de Render usando el workflow de GitHub Actions incluido en el repositorio.

- **Archivo de workflow**: [.github/workflows/deploy-to-render.yml](.github/workflows/deploy-to-render.yml)

- **1) Crear cuenta y servicio en Render**: crea una cuenta gratuita en https://render.com y añade un nuevo **Web Service**. Puedes elegir desplegar usando el `Dockerfile` existente o eligiendo el entorno Python/Repository.

- **2) Obtener API Key de Render**:
	- En Render: `Account` → `API Keys` → `Generate API Key`.
	- Guarda esa clave: la usarás como `RENDER_API_KEY` en GitHub Secrets.

- **3) Obtener el Service ID**:
	- En el panel de tu servicio en Render ve a `Settings` → `Service ID` y cópialo.
	- Alternativamente puedes listar servicios vía API:

```bash
curl -H "Authorization: Bearer $RENDER_API_KEY" https://api.render.com/v1/services
```

- **4) Crear Secrets en GitHub**:
	- Ve a tu repo en GitHub → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`.
	- Añade dos secrets:
		- `RENDER_API_KEY`: la API key que obtuviste en Render.
		- `RENDER_SERVICE_ID`: el Service ID del servicio que creaste en Render.

- **5) Comprobar rama de despliegue**:
	- El workflow se ejecuta en pushes a la rama `main`. Asegúrate que tu rama principal se llame `main` o adapta el workflow.

- **6) Qué hace el workflow**:
	- Al hacer `push` a `main` el workflow instala dependencias (opcional) y hace una llamada a la API de Render para crear un nuevo `deploy` del servicio indicado.

- **Alternativa (recomendada)**: Render soporta integración directa con GitHub para despliegues automáticos (sin Actions). Si prefieres, conecta tu repositorio desde el dashboard de Render y activa Auto Deploy.

Con esto, cada push a `main` disparará un nuevo deploy en Render (si los `secrets` están configurados correctamente).

