from flask import Flask, render_template, url_for
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost', user='root', password='Han19981130..', port=3306, db='museum')


@app.route('/')
def collections():  # put application's code here
    return render_template('collections.html')


@app.route('/anthropology')
def anthropology():
    cur = conn.cursor()
    sql = "SELECT * FROM anthropology limit 30"
    cur.execute(sql)
    ant_collections = cur.fetchall()
    return render_template('anthropology.html', ant_collections=ant_collections)


@app.route('/detail/<string:id>', methods=["GET", "POST"])
def detail(id):
    cur = conn.cursor()
    sql = "SELECT * FROM anthropology where AccessionNumber= '{}';".format(str(id))
    cur.execute(sql)
    details = cur.fetchall()

    return render_template("detail.html", details=list(details)[0])


@app.route('/archery')
def archery():
    cur = conn.cursor()
    sql = "SELECT * FROM archery limit 30"
    cur.execute(sql)
    arc_collections = cur.fetchall()
    return render_template('archery.html', arc_collections=arc_collections)


@app.route('/egyptology')
def egyptology():
    cur = conn.cursor()
    sql = "SELECT * FROM egyptology limit 30"
    cur.execute(sql)
    egy_collections = cur.fetchall()
    return render_template('egyptology.html', egy_collections=egy_collections)


if __name__ == '__main__':
    app.run()
