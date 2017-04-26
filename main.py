from flask import Flask, render_template
import thermo
app = Flask(__name__)

# TODO implement variables as methods

state = 'heat'
set_temp = 72
in_temp = 69
out_temp = 55

while state != 'off':

    if state == 'heat':
        thermo.heat(set_temp, in_temp)
    if state == 'cool':
        thermo.cool(set_temp, in_temp)
    elif ():
        pass

@app.route('/')
def render_static():

    return render_template("thermo.html", state=state, set_temp=set_temp, in_temp=in_temp, out_temp=out_temp )

if __name__ == "__main__":
    app.run()
