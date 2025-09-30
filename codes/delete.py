from sqlalchemy import create_engine, update, MetaData, Table,delete,and_
from codes.databaseManagement import engine, clientes

metadata = MetaData()
metadata.reflect(bind=engine)
clientes = metadata.tables["clientes"]

def delete_cliente(id: str, nombre: str):
    with engine.begin() as conn:
        stmt = delete(clientes).where(and_(clientes.c.id == id, clientes.c.nombre == nombre))
        conn.execute(stmt)
        print("Cliente Eliminado")