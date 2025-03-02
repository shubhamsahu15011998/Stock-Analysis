from DB import SQLSession
from sqlalchemy.dialects.postgresql import insert


class DBUtils:

    @classmethod
    def bulk_upsert(cls, table_obj, data, primary_key):
        if not data:
            print("No data provided for upsert.")
            return

        engine = SQLSession.get_database_connection()
        with engine.connect() as conn:
            try:
                stmt = insert(table_obj).values(data)
                upsert_stmt = stmt.on_conflict_do_update(
                    index_elements=primary_key,
                    set_={col: stmt.excluded[col] for col in data[0] if col not in primary_key}
                )
                conn.execute(upsert_stmt.execution_options(batch_parameters=True))  # Optimize bulk execution
                conn.commit()
                print(f"Successfully upserted {len(data)} records into {table_obj.name}")
            except Exception as e:
                conn.rollback()
                print(f"Error in upsert: {str(e)}")


    @classmethod
    def bulk_update(cls, mapper, mapping):
        session = SQLSession.get_session()  # Get session
        try:
            session.bulk_update_mappings(mapper, mapping)
            session.commit()
            print(f"Successfully Inserted {len(mapping)} {mapper.__name__}s")#{symbol.trading_symbol}")
        except Exception as e:
            session.rollback()
            print(f"Error adding symbol: {str(e)}")
        finally:
            session.close()