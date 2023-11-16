import sqlalchemy as sql
from datetime import datetime


def save_results(url, domain, tagcount):
    """Check data in tags.db: update if exists, insert if not."""
    connection = engine.connect()
    try:
        check = tagcounter_db.select().where(tagcounter_db.c.url == url)
        check_result = connection.execute(check).scalar()  # returns True / False
        if check_result:
            update_data = tagcounter_db.update().where(tagcounter_db.c.url
                                                       == url).values(
                                                       site_name=domain,
                                                       url=url,
                                                       date_time=datetime.now(),
                                                       tagcount=tagcount)
            connection.execute(update_data)
            print("Data successfully updated!")
        else:
            insert_data = tagcounter_db.insert().values(
                          site_name=domain,
                          url=url,
                          date_time=datetime.now(),
                          tagcount=tagcount)
            connection.execute(insert_data)
            print("Data successfully loaded into Database!")
    finally:
        connection.close()


def select_from_db(full_url):
    """Connect to DB and execute select."""
    select_data = (sql.select(tagcounter_db.c.tagcount).where
                   (tagcounter_db.c.url == full_url))
    connection = engine.connect()
    results = connection.execute(select_data).fetchall()
    connection.close()

    return results[0][0]                              # extract pickled object from the results list


# вот здесь была ошибка - каждый раз создавало таблицу заново: :memory: вместо tags.db название бд
engine = sql.create_engine('sqlite:///tags.db', echo=True)
metadata = sql.MetaData()
tagcounter_db = sql.Table('tagcounter_db', metadata,
                          sql.Column('site_name', sql.String(60)),
                          sql.Column('url', sql.String(250)),
                          sql.Column('date_time', sql.String(60)),
                          sql.Column('tagcount', sql.Integer)
                          )
metadata.create_all(engine)
