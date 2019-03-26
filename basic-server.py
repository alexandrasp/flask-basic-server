from flask import Flask
import time

app = Flask(__name__)

#tokenize
@app.route('/TokenServices.svc/REST/tokenize', methods=['GET', 'POST'])
def exception_time_out_toke():
    time.sleep(40)
    return 'Ai!'

#detokenize

@app.route('/TokenServices.svc/REST/detokenize', methods=['GET', 'POST'])
def exception_time_out_detoke():
    return 'clap!!'

if __name__ == '__main__':
    app.run(host='127.0.0.1')