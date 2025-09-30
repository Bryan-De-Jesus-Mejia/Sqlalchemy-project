from sqlalchemy import create_engine, update, MetaData, Table
from codes.databaseManagement import engine, clientes

metadata = MetaData()
metadata.reflect(bind=engine)
clientes = metadata.tables["clientes"]

def update_cliente(id: str, nombre: str, telefono: str, email: str, estado: str):
    with engine.connect() as conn:
        stmt = (
            update(clientes)
            .where(clientes.c.id == id)
            .values(nombre=nombre, telefono=telefono, email=email, estado=estado)
        )
        conn.execute(stmt)
        conn.commit()