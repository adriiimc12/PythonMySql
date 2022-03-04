def obtener_conexion2():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='prueba_db' )

def insertar_usuario(username, first_name, last_name, gender):
    conexion = obtener_conexion2()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO user_details(username, first_name, last_name, gender) VALUES (%s, %s, %s ,%s)",
        (username, first_name, last_name, gender))
    conexion.commit()
    conexion.close()
    
def eliminar_usuario(user_id):
    conexion = obtener_conexion2()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM user_details WHERE user_id = %s", (user_id,))
    conexion.commit()
    conexion.close()

def obtener_usuario_por_id(user_id):
    conexion = obtener_conexion2()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT user_id, username, first_name, last_name, gender FROM user_details WHERE user_id = %s", (user_id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_usuario(username, first_name, last_name, gender, user_id):
    conexion = obtener_conexion2()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE user_details SET username = %s, first_name = %s, last_name = %s WHERE user_id = %s",
                       (username, first_name, last_name, gender, user_id))
    conexion.commit()
    conexion.close()

actualizar_usuario("Maria19", "Maria", "Rodriguez", "female", 47)