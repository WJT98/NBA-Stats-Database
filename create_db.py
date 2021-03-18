import db_func
import db_config
import psycopg2
from psycopg2 import pool
from psycopg2 import OperationalError, errorcodes, errors, Error
import sys

def main():
	try:
		conn = psycopg2.connect(user = db_config.user,
									password = db_config.password,
									host = db_config.host,
									port = db_config.port,
									database = db_config.database)
		if(conn):
			print("Connection created successfully")
		
		db_func.exec_query(conn, db_config.create_match_import_table)
		db_func.exec_query(conn, db_config.create_player_performance_import_table)
		db_func.exec_query(conn, db_config.create_match_table)
		db_func.exec_query(conn, db_config.create_team_table)
		db_func.exec_query(conn, db_config.create_player_performance_table)
		db_func.exec_query(conn, db_config.create_season_table)
		conn.commit()
	except Exception as err:
		conn = None
		print(err)
	finally:
		if (conn):
			conn.close()
			print("PostgreSQL connection is closed")


if __name__ == '__main__':
	main()