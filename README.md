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

