from flask import Flask
a=Flask("first")
@a.route("/")
def sai():
    return("praneeth")
a.run()
