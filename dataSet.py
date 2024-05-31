import sqlite3
import pandas as pd



class doDataBase:
    def __init__(self,conn):

        self.conn = sqlite3.connect(conn)

    def create_dataBase(self):
        df = pd.read_csv('pokedex.csv')


        c = self.conn.cursor()
        c.execute('''CREATE TABLE Pokemon
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               status            TEXT     NOT NULL,
               type_1            TEXT     NOT NULL,
               type_2            TEXT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);''')
        self.conn.commit()

	# abilities_number	ability_1	ability_2	ability_hidden	total_points	hp	attack	defense	sp_attack	sp_defense	speed	catch_rate	base_friendship	base_experience	against_normal	against_fire	against_water	against_electric	against_grass	against_ice	against_fight	against_poison	against_ground	against_flying	against_psychic	against_bug	against_rock	against_ghost	against_dragon	against_dark	against_steel	against_fairy
