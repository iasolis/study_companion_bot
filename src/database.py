import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    # --- add func ---
    def add_acc(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))

    def add_direction(self, user_id, direction_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'user_directions' ('user_id', 'direction_id') VALUES (?,?)",
                                       (user_id, direction_id,))

    def add_likes(self, user_id_liked, user_id_was_liked):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'likes' ('id_liked', 'id_was_liked') VALUES (?,?)",
                                       (user_id_liked, user_id_was_liked,))

    # --- set func ---
    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET nickname = ? WHERE user_id = ?", (nickname, user_id,))

    def set_age(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET age = ? WHERE user_id = ?", (age, user_id,))

    def set_summary(self, user_id, summary):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET summary = ? WHERE user_id = ? ", (summary, user_id,))

    def set_acc_image(self, user_id, image_id):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET image_id = ?WHERE user_id = ? ", (image_id, user_id,))

    def set_status_acc(self, user_id, status_acc):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' set  status_acc = ? WHERE user_id = ? ",
                                       (status_acc, user_id,))

    # --- check func ---
    def check_acc_exist(self, user_id):
        with self.connection:
            exist = self.cursor.execute("SELECT * FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()
            return exist

    def check_status_acc(self, user_id):
        with self.connection:
            status = self.cursor.execute("SELECT status_acc FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()
            return status

    # --- get func ---
    def get_acc_info(self, user_id):
        with self.connection:
            acc_info = self.cursor.execute("SELECT image_id, nickname,age,summary FROM 'users' WHERE user_id = ?",
                                           (user_id,)).fetchone()
            return acc_info

    def get_directions(self, user_id):
        with self.connection:
            directions = self.cursor.execute("SELECT direction_id FROM 'user_directions' WHERE user_id = ?",
                                           (user_id,)).fetchall()
            return directions

    def get_active_user_id(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM 'users' WHERE  status_acc = ?", (1,)).fetchall()

    def get_likes(self, user_id_was_liked):
        with self.connection:
            return self.cursor.execute("SELECT id_liked FROM 'likes' WHERE id_was_liked = ?", (user_id_was_liked,)).fetchone()

    # --- del func ---
    def del_directions(self, user_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM 'user_directions' WHERE user_id = ?", (user_id,))

    def del_likes(self, user_id_liked, user_id_was_liked):
        with self.connection:
            return self.cursor.execute("DELETE FROM 'likes' WHERE id_liked = ? AND id_was_liked = ? ", (user_id_liked, user_id_was_liked))



