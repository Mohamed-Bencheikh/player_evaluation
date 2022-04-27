import mysql.connector

cnx = mysql.connector.connect(user ='root',password='mbcmysql', host='localhost',database='test')
cr = cnx.cursor(buffered=False)
def insertData(mid,pid,ev):
    query = f"""INSERT INTO PLAYERS (num_match,num_player,evaluation) VALUES ({mid},{pid},{ev})"""
    cr.execute(query) 
    cnx.commit()
               
def getLastMatch(pid):
    last_match = 0
    cr.execute(f"""select num_match from players where num_player = {pid} and 
        num_match = (select max(num_match) from players where num_player={pid})
    """)
    for row in cr:
        last_match = row[0]
    return last_match