import psycopg2

"""
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1 % of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5 % errors
"""

def dbconnect():
    "Returns a live connection"

    try:
        db = psycopg2.connect(database='news')
        db.reset()
        c = db.cursor()

        return (db, c)
    except:
        print("I am unable to connect to the database")
        return None


def get_logs():
    """Return all posts from the 'database', most recent first."""

    db, c = dbconnect()

    c.execute('SELECT * FROM log')

    return c.fetchall()
    db.close()

print(get_logs())
