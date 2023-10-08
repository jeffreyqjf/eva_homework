from flask import Flask, request
import sqlite3
from flask import g
app = Flask(__name__)
app.config["database"] = "data.db"

@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['database'])


@app.route("/ping")
def ping():
    cursor = g.db.cursor()

    result = '''{
                "code": 0, 
                "msg": "pong", 
                "data": "helloword"
                }'''
    cursor.execute("insert into user values (?,?,?)")  # 然鹅数据库内容并没有设置
    g.db.commit()
    g.db.close()
    return result  # 也没有用render_template


@app.route("/check", methods=["get","post"])
def check():
    #  处理post发送过来的请求可能要看HTML的相关标签
    #get 用于用户填写表单，即设备，post用于处理
    cursor = g.db.cursor()
    source = request.form.get('source')  # 这里要求相关HTML
    if source == "EVA":
        result = """{code": 0, "msg": "", "data": none,source": "{0}","isChecked": true}""".format(source)
        cursor.execute("insert into user values (?,?,?)")  # 然鹅数据库内容并没有设置
        g.db.commit()
        g.db.close()
    else:
        result = """{"code": 100,"msg": "Server not authorized","data":"","isChecked": false}"""
        cursor.execute("insert into user values (?,?,?)")  # 然鹅数据库内容并没有设置
        g.db.commit()
        g.db.close()
    return result


@app.route("/status", methods=["get", "post"])
def status():
    cursor = g.db.cursor()
    #  处理post发送过来的请求可能要看HTML的相关标签
    #  get 用于用户填写表单，即设备，post用于处理
    source = request.form.get('source')  # 这里要求相关HTML
    if source == "EVA":
        result = """{code": 0, "msg": "", "data": none,source": "{0}","lastTime": "1984/10/01 11:45:14","isDisconnected": true,"hitokoto": "你好呀，祝你满绩每一天}""".format(source)
        cursor.execute("insert into user values (?,?,?)")  # 然鹅数据库内容并没有设置
        g.db.commit()
        g.db.close()
    return result


if __name__ == "__main__":
    app.run()

