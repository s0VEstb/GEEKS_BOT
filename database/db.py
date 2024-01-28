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
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_COMPLAINTS_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_USERS)
        self.connection.execute(sql_queries.CREATE_ANIME_TABLE_QUERY)

        #self.connection.execute(sql_queries.ALTER_USER_TABLE_QUERY)
        #self.connection.execute(sql_queries.ALTER_USER_TABLE_QUERY_V2)
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None, 0)
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
        self.cursor.execute(sql_queries.SELECT_TG_ID_USER_QUERY, (tg,))
        row = self.cursor.fetchone()
        return row

    def sql_select_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'bio': row[3],
            'age': row[4],
            'gender': row[5],
            'hobby': row[6],
            'zodiac_sign': row[7],
            'photo': row[8],
        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker)
        )
        self.connection.commit()

    def sql_insert_dislike(self, owner, disliker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker)
        )
        self.connection.commit()

    def sql_select_all_profiles(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'bio': row[3],
            'age': row[4],
            'gender': row[5],
            'hobby': row[6],
            'zodiac_sign': row[7],
            'photo': row[8],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LIKER_LEFT_JOIN_PROFILE_QUERY,
            (owner, owner, owner,)
        ).fetchall()

    def sql_select_complainted_profile(self, username):
        self.cursor.execute(sql_queries.SELECT_COMPLAINTS_QUERY, (username,))
        un = self.cursor.fetchone()
        return un

    def sql_select_id_from_username_profile(self, username):
        self.cursor.execute(sql_queries.SELECT_TG_ID_USERNAME_QUERY, (username,))
        usernam = self.cursor.fetchone()
        return usernam

    def sql_delete_profile(self, tg_id):
        self.cursor.execute(sql_queries.DELETE_PROFILE_QUERY, (tg_id,))
        self.connection.commit()


    def sql_select_complaint_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'bad_user_telegram_id': row[2],
            'reason': row[3],
            'bad_count': row[4]
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_COMPLAINTS_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_bad_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_COMPLAINTS_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_bad_user(self, complained_user, bad_user, reason,):
        self.cursor.execute(
            sql_queries.INSERT_BAD_USER_QUERY,
            (None, complained_user, bad_user, reason, 1,)
        )
        self.connection.commit()

    def sql_select_referrals_menu(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'balance': row[0],
            'total_referrals': row[1],
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERRAL_USER_QUERY,
            (owner,)
        ).fetchone()

    def sql_select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2],
            'first_name': row[3],
            'last_name': row[4],
            'reference_link': row[5],
            'balance': row[6],

        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_link(self, link, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_TABLE_QUERY,
            (link, tg_id,)
        )
        self.connection.commit()


    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2],
            'first_name': row[3],
            'last_name': row[4],
            'reference_link': row[5],
            'balance': row[6],

        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_insert_referral(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral,)
        )
        self.connection.commit()


    def sql_update_balance(self, owner):
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (owner,)
        )
        self.connection.commit()

    def sql_select_referrals_button(self, tg_id):
        return self.cursor.execute(
            sql_queries.SELECT_REFERRALS_BUTTON_QUERY,
            (tg_id,)
        ).fetchall()

    def sql_insert_anime_link(self, link):
        self.cursor.execute(
            sql_queries.INSERT_ANIME_QUERY,
            (None, link,)
        )
        self.connection.commit()

