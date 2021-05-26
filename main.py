#!/usr/bin/env python
# encoding: utf-8
'''
@author: donngchao
@file: main.py
@time: 2021/5/25 1:12 下午
@desc: This file will help you compare two different files
'''

from flask import Flask, render_template, request
import difflib
from flask import Response

app = Flask(__name__)


@app.route('/')
def upload_file():
    return render_template("input.html")


@app.route('/compare', methods=['POST', 'GET'])
def compare():
    file1 = request.form['file1']
    file2 = request.form['file2']
    text1_line = file1.splitlines()
    text2_line = file2.splitlines()
    d = difflib.HtmlDiff()
    if request.method == 'POST':
        return Response(d.make_file(text1_line, text2_line), mimetype="text/html")
    return Response(d.make_file(text1_line, text2_line), mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
