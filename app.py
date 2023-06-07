from flask import Flask,render_template
import sqlite3
import gunicorn

app = Flask(__name__)


@app.route('/index1')
def index():
    infos = []
    con = sqlite3.connect("book250.db")
    cur = con.cursor()
    sql = "select * from book2 limit 0,10"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)

    score = []  #评分
    num = []    #每个评分所统计出的书数量
    con = sqlite3.connect("book250.db")
    cur = con.cursor()
    sql = "select 得分,count(得分) from book2 group by 得分"
    data1 = cur.execute(sql)
    for item in data1:
        score.append(item[0])
        num.append(item[1])


    datalist = []
    con = sqlite3.connect("book250.db")
    cur = con.cursor()
    sql = "select 得分,sum(评价人数) from book2 group by 得分"
    data2 = cur.execute(sql)
    for item in data2:
        datalist.append([item[0],item[1]])

    cur.close()
    con.close()

    return render_template("index.html", infos=infos,score=score,num=num,datalist=datalist)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

