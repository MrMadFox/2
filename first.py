from flask import Flask
a=Flask(__name__)
@a.route("/")
def sai():
    return("praneeth")
a.run()
if __name__=="__main__":
    a.run()
