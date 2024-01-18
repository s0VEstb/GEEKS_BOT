import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('my_hw_db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print(f"DataBase connected")
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name,)
        )
        self.connection.commit()

    def sql_insert_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, tg_id, 1,)
        )
        self.connection.commit()


    def sql_select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()



    def sql_update_ban_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_TABLE_QUERY,
            (tg_id,)
        )
        self.connection.commit()


    def sql_insert_profile(self, tg_id, nickname, bio, age, gender, hobby, zodiac_sign, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_USER_QUERY,
            (None, tg_id, nickname, bio, age, gender, hobby, zodiac_sign, photo,)
        )
        self.connection.commit()

    def sql_select_id_profile(self, tg):
        self.cursor.execute(sql_queries.SELECT_PROFILE_USER_QUERY, (tg,))
        row = self.cursor.fetchone()
        return row
