from flask import Flask,jsonify
from flask import request
SUCCESS_CODE=0
SYSTEM_ERRCODE     = 11
PARAMS_ERRCODE     = 21

app = Flask(__name__)

@app.route('/shopee/test')
def test():
    try:
        req = request.args
        if "a" in req and "b" in req and req["a"].isdigit() and isinstance(req["b"],basestring):
        
            err_code = SUCCESS_CODE
            ref = "1111"
            err_msg = "success"
        else:
            err_code = PARAMS_ERRCODE
            ref = "222"
            err_msg = "params error"
    except:
        err_code = SYSTEM_ERRCODE
        ref = "333"
        err_msg = "system err"
    rsp = {"err_code":err_code,"err_msg":err_msg,"reference":ref}
    return jsonify(rsp) 
