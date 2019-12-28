import pymysql
def insert(args,args2,args3):
	try:
		conexion = pymysql.connect(host='remotemysql.com',
		                             user='OuiwI9pjP2',
		                             password='bKehdD6r9l',
		                             db='OuiwI9pjP2')
		try:
			with conexion.cursor() as cursor:
				consulta = "INSERT INTO alumnos (nombre,apellido,codigo) VALUES (%s,%s,%s);"
				#Podemos llamar muchas veces a .execute con datos distintos
				val = (args,args2,args3)
				cursor.execute(consulta, (val))
			conexion.commit()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
