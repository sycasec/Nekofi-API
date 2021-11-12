import sqlalchemy as nkSQL
import databases as db

metadata = nkSQL.MetaData()
database_url = "sqlite:///./neko.db"

nekoDB = db.Database(database_url)

kofiTable = nkSQL.Table(
    "Nekofi_Products",
    metadata,
    nkSQL.Column("id", nkSQL.Integer, primary_key=True),
    nkSQL.Column("title", nkSQL.String(50)),
    nkSQL.Column("description", nkSQL.String(500)),
    nkSQL.Column("price", nkSQL.Float),
    nkSQL.Column("isAvailable", nkSQL.Boolean)
)

engine = nkSQL.create_engine(database_url, connect_args={"check_same_thread": False})

