import mysql.connector


class Db:
    def __init__(self):
        self.name = "tetris_db"
        self.host = "localhost"
        self.user = "root"
        self.password = "PythonHunters"
        self.db = mysql.connector.connect(host=self.host,user = self.user,password =self.password,database =self.name)

    def add_player(self,name):
        mycursor = self.db.cursor()
        sql = "INSERT INTO jugador (idJugador, Nombre) VALUES (%s, %s)"
        val = ("NULL", name)
        mycursor.execute(sql, val)
        self.db.commit()
        mycursor.close()
    def add_score(self,idjugador, score):
        mycursor = self.db.cursor()
        sql = "INSERT INTO puntaje (idPuntaje, dificultad,puntaje,Jugador_idJugador) VALUES (%s, %s,%s,%s)"
        val = ("NULL", "Normal",score,idjugador)
        mycursor.execute(sql, val)
        self.db.commit()
        mycursor.close()

    def get_id_user(self, name):
        mycursor = self.db.cursor()
        sql = "SELECT idJugador FROM jugador WHERE Nombre = %s"
        mycursor.execute(sql, (name,))
        result = mycursor.fetchone()
        mycursor.close()

        if result:
            return result[0]  # Devuelve el idJugador si se encuentra
        else:
            return None  # Devuelve None si no se encuentra un usuario con el nombre dado

    def check_name_exists(self,name):
        cursor = self.db.cursor()

        # Consulta SQL para verificar si el nombre existe en la tabla
        sql = "SELECT COUNT(*) FROM jugador WHERE Nombre = %s"
        cursor.execute(sql, (name,))

        # Obtener el resultado de la consulta
        result = cursor.fetchone()

        # Cerrar el cursor
        cursor.close()

        # Si el resultado es mayor que 0, el nombre existe
        return result[0] > 0

    def cargar_datos(self,tabla):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT jugador.Nombre AS NombreJugador, puntaje.puntaje AS Puntaje FROM jugador INNER JOIN puntaje ON jugador.idJugador = puntaje.Jugador_idJugador ORDER BY puntaje.puntaje DESC LIMIT 10")
        datos = cursor.fetchall()

        for row in tabla.get_children():
            tabla.delete(row)

        for dato in datos:
            tabla.insert('', 'end', values=(dato[0], dato[1]))

