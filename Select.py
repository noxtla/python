import pymysql

try:
	conexion = pymysql.connect(host='remotemysql.com',
                             user='OuiwI9pjP2',
                             password='bKehdD6r9l',
                             db='OuiwI9pjP2')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			cursor.execute("SELECT numTel FROM alumnos;")

			# Con fetchall traemos todas las filas
			peliculas = cursor.fetchall()

			num = list(sum(peliculas,()))
			print (num)

	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
