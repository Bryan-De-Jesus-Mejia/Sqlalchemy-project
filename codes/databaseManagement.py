from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import os

# Crear motor hacia archivo SQLite
engine = create_engine("sqlite:///instances/app.db", echo=True)

# Definir metadata y tabla clientes
metadata = MetaData()

clientes = Table(
    "clientes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", String),
    Column("telefono", String),
    Column("email", String),
    Column("estado", String),
)

# Crear la tabla en la base de datos
metadata.create_all(engine)

print("Base de datos creada")
