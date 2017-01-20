import MySQLdb as mdb
from bottle import FormsDict
from hashlib import md5

# connection to database project2
def connect():
    """makes a connection to MySQL database.
    @return a mysqldb connection
    """
    
    #TODO: fill out function parameters
    
    return mdb.connect(host="localhost",
                       user="dyang35",
                       passwd="ebc7ec58f81295d3024407cc2379d6248c1b97f2d3eac00ff5ee75495a2f6f49",
                       db="project2");

def createUser(username, password):
    """ creates a row in table named user 
    @param username: username of user
    @param password: password of user
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query creates a row in table user

    istmt = "INSERT INTO users (username, password, passwordhash) VALUES (%s, %s, %s)"
    m = md5()
    m.update(password)
    cur.execute(istmt, (username, password, m.digest()))

    db_rw.commit()

def validateUser(username, password):
    """ validates if username,password pair provided by user is correct or not
    @param username: username of user
    @param password: password of user
    @return True if validation was successful, False otherwise.
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query selects a row from table user
    vstmt = "SELECT * FROM users where username = %(username)s AND password = %(password)s"
    cur.execute(vstmt, {'username':username, 'password':password })
    if cur.rowcount < 1:
        return False
    return True

def fetchUser(username):
    """ checks if there exists given username in table users or not
    if user exists return (id, username) pair
    if user does not exist return None
    @param username: the username of a user
    @return The row which has username is equal to provided input
    """

    db_rw = connect()
    cur = db_rw.cursor(mdb.cursors.DictCursor)
    print username
    #TODO: Implement a prepared statement so that this query selects a id and username of the row which has column username = username
    fstmt = "SELECT id, username FROM users where username = %(username)s"
    cur.execute(fstmt, {'username':username})
    if cur.rowcount < 1:
        return None
    return FormsDict(cur.fetchone())

def addHistory(user_id, query):
    """ adds a query from user with id=user_id into table named history
    @param user_id: integer id of user
    @param query: the query user has given as input
    """

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statment using cur.execute() so that this query inserts a row in table history
    istmt2 = "INSERT INTO history (user_id, query) VALUES (%s, %s)"
    queryString = (user_id, query)
    #cur.execute(istmt2, {'user_id':user_id, 'query':query})
    cur.execute(istmt2, queryString)
    db_rw.commit()

#grabs last 15 queries made by user with id=user_id from table named history
def getHistory(user_id):
    """ grabs last 15 distinct queries made by user with id=user_id from 
    table named history
    @param user_id: integer id of user
    @return a first column of a row which MUST be query
    """    

    db_rw = connect()
    cur = db_rw.cursor()
    #TODO: Implement a prepared statement using cur.execute() so that this query selects 15 distinct queries from table history
    sstmt2 = "SELECT query FROM history where user_id = %(user_id)s ORDER BY id DESC LIMIT 15"
    cur.execute(sstmt2, {'user_id': user_id})
    rows = cur.fetchall();
    return [row[0] for row in rows]
