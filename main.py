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


def _int_to_roman(num: int) -> str:
    """Convierte un entero positivo a número romano (clásico).

    Soporta por lo pronto hasta 3999, suficiente para 50..100.
    """
    val = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    res = ""
    for v, s in val:
        while num >= v:
            res += s
            num -= v
    return res


@app.get("/obtenerromano")
def obtener_romano():
    """Devuelve aleatoriamente un número entero entre 50 y 100 y su representación romana."""
    numero = random.randint(50, 100)
    romano = _int_to_roman(numero)
    return {"numero": numero, "romano": romano}


@app.get("/", include_in_schema=False)
def root():
    """Sirve `swagger.html` en la raíz para evitar usar `/swagger` manualmente."""
    return FileResponse("swagger.html", media_type="text/html")


@app.get("/doble/{numero}")
def doble(numero: int):
    """Recibe un número entero en la ruta y devuelve el mismo multiplicado por 2."""
    return {"numero": numero, "doble": numero * 2}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
