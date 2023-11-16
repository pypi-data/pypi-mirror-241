import traceback
from typing import Union
from urllib import parse

import pandas as pd
import geopandas as gpd
from dotenv import load_dotenv
from pydantic import BaseModel
from shapely import wkb, wkt
from sqlalchemy import Engine, create_engine, Select, text, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Query

from digitalarztools.utils.logger import da_logger

load_dotenv()


class DBString(BaseModel):
    host: str
    user: str
    password: str
    name: str
    port: str


class DBParams:
    engine: str  # postgresql,sqlite
    con_str: Union[str, DBString]  # either provide file_path or DBString

    def __init__(self, engine: str, con_str: Union[dict, DBString]):
        self.engine = engine
        self.con_str = DBString(**con_str) if isinstance(con_str, dict) else con_str


class DBManager:
    engine: Engine

    def __init__(self, db_info: Union[DBParams, Engine]):
        if isinstance(db_info, Engine):
            self.engine: Engine = db_info
        else:
            self.engine: Engine = self.create_sql_alchemy_engine(db_info)
        if self.engine is None:
            raise Exception("Enable to create sql alchemy engine")

    def get_engine(self):
        return self.engine

    # def get_connection(self):
    #     return self.engine.connect()
    def get_session(self):
        # for session in self.session.registry():
        #     session.close()
        Session = sessionmaker(bind=self.engine)
        session = Session()
        # query = "SELECT count(pid) FROM pg_stat_activity WHERE datname = current_database() AND state = 'idle'"
        # count = self.execute_query_as_one(query)
        # print("no of client is", count)
        # if count > 10:
        #     sql = text("""
        #         SELECT pg_terminate_backend(pid)
        #         FROM pg_stat_activity
        #         WHERE datname = current_database()
        #           AND state = 'idle'
        #     """)
        #     session.execute(sql)
        #     session.commit()
        return session

    @staticmethod
    def create_sql_alchemy_engine(config: DBParams) -> Engine:
        try:
            if config.engine in ["sqlite"]:
                db_string = f'{config.engine}:///{config.con_str}'
            else:
                params = config.con_str
                db_string = f'{config.engine}://{params.user}:{parse.quote(params.password)}@{params.host}:{params.port}/{params.name}'
            return create_engine(db_string, echo=True)
        except Exception as e:
            # da_logger.error()
            traceback.print_exc()

    @classmethod
    def create_postgres_engine(cls, db_str: Union[DBString, dict]):
        if isinstance(db_str, dict):
            db_str = DBString(**db_str)
        params = DBParams(engine='postgresql+psycopg2', con_str=db_str)
        return cls.create_sql_alchemy_engine(params)

    def exists(self, stmt: Select):
        """
        :param stmt: Select Stmt
        :return:
        """
        with self.get_session() as session:
            return session.execute(stmt).first() is not None

    def get_sqlalchemy_table(self, table_name, schema_name='public') -> Table:
        try:
            metadata = MetaData()
            tbl: Table = Table(
                table_name,
                metadata,
                # autoload=True,
                autoload_with=self.engine,
                schema=schema_name
            )
            return tbl
        except Exception as e:
            da_logger.error(str(e))
            return None

    def create_xyz_cache_table(self, table_name: str):
        meta_data = MetaData()
        xyz_table = Table(table_name, meta_data,
                          Column('id', Integer, primary_key=True, autoincrement=True),
                          Column('x', Integer),
                          Column('y', Integer),
                          Column('z', Integer),
                          Column('mvt', String))
        meta_data.create_all(self.engine)
        return xyz_table

    def execute_query_as_one(self, query: [str, Select]):
        result = None
        if isinstance(query, Select):
            with self.get_session() as session:
                row = session.execute(query).first()
                return row[0] if row is not None else None
        else:
            with self.get_session() as session:
                rs = session.execute(text(query))
                if rs.returns_rows:
                    res = rs.fetchone()
                    if res:
                        result = res[0]
                session.close()
        return result

    def execute_query_as_df(self, query: Union[str, Select]) -> pd.DataFrame:
        with self.get_session() as session:
            if isinstance(query, Select):
                rs = session.execute(query)
            else:
                rs = session.execute(text(query))
            df = pd.DataFrame(rs.fetchall())
            if not df.empty:
                df.columns = rs.keys()
            return df

    def get_query_data(self, query: Union[Table, Select, str]):
        """
           :param query: Table or Select Stmt
               Select(xyz_table.c.mvt).select_from(xyz_table).where(xyz_table.c.x == x, xyz_table.c.y == y, xyz_table.c.z == z)
           # :param limit_value:
           :return:
       """
        with self.get_session() as session:
            if isinstance(query, Table):
                qs = session.query(query)
                return qs.all()
            # elif isinstance(query, Query):
            #     # rs = session.execute(query).all()
            #     # rs = query.all()
            #     # return [row.__dict__ for row in query.all()]
            #     # Convert the SQLAlchemy model instances to a list of dictionaries
            #     data_dicts = [obj.__dict__ for obj in query.all()]
            #
            #     # Remove the '_sa_instance_state' key from each dictionary
            #     data_dicts = [{k: v for k, v in d.items() if k != '_sa_instance_state'} for d in data_dicts]
            #
            #     return data_dicts
            elif isinstance(query, Select):
                rs = session.execute(query)
                return rs.fetchall()
            else:
                rs = session.execute(text(query))
                return rs.fetchall()

    def execute_dml(self, stmt):
        """
        :param stmt:  like xyz_table.insert().values(x=x, y=y, z=z, mvt=res) or dml string
        :return:
        """
        res = None
        try:
            with self.get_session() as session:
                if isinstance(stmt, str):
                    stmt = text(stmt)
                session.execute(stmt)
                session.commit()
                session.close_all()
                return True
        except Exception as e:
            print(traceback.print_exc())
            # print("Cannot perform DDL operation")
        return False

    def execute_ddl(self, stmt):
        try:
            with self.get_session() as session:
                if isinstance(stmt, str):
                    stmt = text(stmt)
                res = session.execute(stmt)
                session.commit()
                print("DDL performed successfully")
                session.close_all()
                return True
        except Exception as e:
            traceback.print_exc()
            # print("Cannot perform DDL operation")
            return False

    def table_to_df(self, tbl: Union[Table, str, Select]):
        """
        Table or Select Stmt
            Example Select(xyz_table.c.mvt).select_from(xyz_table).where(xyz_table.c.x == x, xyz_table.c.y == y, xyz_table.c.z == z)
        :param tbl:
        :param limit:
        :return:

        """
        if isinstance(tbl, str):
            tbl = self.get_sqlalchemy_table(tbl)
        # geom_cols = self.get_geometry_cols(tbl)
        data = self.get_query_data(tbl)
        # geom_col = geom_cols[0]
        # srid = self.get_geom_col_srid(tbl, geom_col)
        return pd.DataFrame(data)


class GeoDBManager(DBManager):
    @staticmethod
    def get_geometry_cols(table: Table) -> list:
        geom_cols = [col for col in list(table.columns) if 'geometry' in str(col.type)]
        return geom_cols

    def get_geom_col_srid(self, tbl, geom_col):
        with self.get_session() as session:
            res = session.query(tbl.c[geom_col].st_srid()).first()
            return res[0] if len(res) > 0 else 0

    @staticmethod
    def data_to_gdf(data, geom_col, srid=0, is_wkb=True):
        # data = list(data)
        # data = [row for row in data]
        if len(data) > 0:
            gdf = gpd.GeoDataFrame(data)
            gdf = gdf.dropna(axis=0)
            if is_wkb:
                gdf["geom"] = gdf[geom_col].apply(lambda x: wkb.loads(x, hex=True))
            else:
                gdf["geom"] = gdf[geom_col].apply(lambda x: wkt.loads(str(x)))
            if geom_col != "geom":
                gdf = gdf.drop(geom_col, axis=1)
            gdf = gdf.set_geometry("geom")
            if srid != 0:
                gdf.crs = srid
            return gdf
        else:
            return gpd.GeoDataFrame()

    def table_to_gdf(self, tbl: Union[Table, str], geom_col="geom", limit=-1):
        if isinstance(tbl, str):
            tbl = self.get_sqlalchemy_table(tbl)
        # geom_cols = self.get_geometry_cols(tbl)
        # data = self.get_all_data(tbl, limit)
        query = Select(tbl).query()
        data = self.get_query_data(query)
        # geom_col = geom_cols[0]
        srid = self.get_geom_col_srid(tbl, geom_col)
        return self.data_to_gdf(data, geom_col, srid)

    def execute_query_as_gdf(self, query, srid, geom_col='geom', is_wkb=True):
        data = self.get_query_data(query)
        # if data and len(data) > 0:
        return self.data_to_gdf(data, geom_col, srid, is_wkb)
