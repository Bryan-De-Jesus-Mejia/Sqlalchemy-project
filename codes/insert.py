from sqlalchemy import insert
from codes.databaseManagement import engine, clientes

def insert_cliente(nombre: str, telefono: str, email: str, estado: str) -> None:
    with engine.connect() as conn:
        data = insert(clientes).values(
            nombre=nombre,
            telefono=telefono,
            email=email,
            estado=estado
        )
        conn.execute(data)
        conn.commit()
