from flask import  Flask, render_template, request, redirect
from tp_module import trabajo, potencia

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title='Evaluacion U2')


@app.route('/exec_trabajo', methods=['POST'])
def execute()->'html':
    f = float(request.form['f'])
    d = float(request.form['d'])
    title = 'El resultado es: '
    result = trabajo(f, d)
    return render_template('result.html',
                                 the_title=title,
                                 the_f=f,
                                 the_d=d,
                                 the_result=result, )


if __name__ == '__main__':
    app.run(port=5001)

