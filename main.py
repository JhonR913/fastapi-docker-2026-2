from fastapi import FastAPI
import random
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/obtenercedula")
def obtener_cedula():
    """Devuelve un número entero aleatorio de 10 dígitos.

    Rango: 1000000000 .. 9999999999 (evita ceros iniciales).
    """
    numero = random.randint(1000000000, 9999999999)
    return {"cedula": numero}


@app.get("/swagger", include_in_schema=False)
def swagger_html():
    return FileResponse("swagger.html", media_type="text/html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
