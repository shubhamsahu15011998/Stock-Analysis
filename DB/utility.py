from DB import SQLSession


class DBUtils:

    @classmethod
    def bulk_upsert(cls, objs):
        session = SQLSession.get_session()  # Get session
        try:
            if objs:
                list(map(session.merge, objs))
                session.commit()
                print(f"Successfully Upserted {len(objs)} {objs[0].__class__.__name__}s")
            else:
                print("Can't insert an empty list")
        except Exception as e:
            session.rollback()
            print(f"Error adding symbol: {str(e)}")
        finally:
            session.close()

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