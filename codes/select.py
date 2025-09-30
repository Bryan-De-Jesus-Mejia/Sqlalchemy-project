from sqlalchemy import create_engine, MetaData, Table, select
from codes.databaseManagement import engine

metadata = MetaData()
metadata.reflect(bind=engine)
clientes = metadata.tables["clientes"]

def select_cliente(nombre: str):
    with engine.connect() as conn:
        if nombre is None:
            result = conn.execute(select(clientes))
        else:
            result = conn.execute(
                select(clientes).where(clientes.c.nombre.ilike(f"%{nombre}%"))
            )
        return result.fetchall()
