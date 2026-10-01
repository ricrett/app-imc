from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/equipe')
def equipe ():
    return render_template ('equipe.html')

@app.route('/', methods=['GET', 'POST'])
def calculadora ():
    erros = []
    imc = 0.00
    faixa = None 
    nome = None
    peso = 0.00 
    altura = 0.00


    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        peso = request.form.get('peso', '').strip()
        altura = request.form.get('altura', '').strip()

        if not nome:
            erros.append('É obrigatório inserir o nome!')
        if not peso:
            erros.append('É obrigatório inserir o peso!')
        if not altura:
            erros.append('É obrigatório inserir a altura!') 
        

        if erros:
            for erro in erros:
                flash(erro, 'danger')
            return render_template('index.html',
                                nome=nome,
                                peso=peso,
                                altura=altura,
                                ) 

        if not erros:      
            imc = float(peso) / (float(altura) * float(altura))

            if imc <= 18.5:
                faixa = "Abaixo do Peso"
            elif imc >= 18.5 and imc < 25:
                faixa = "Peso Normal"
            elif imc >= 25 and imc < 30:
                faixa = "Sobrepeso"
            elif imc > 30:
                faixa = "Obesidade"
            
    
    return render_template ('index.html', erros=erros, nome=nome, peso=peso, altura=altura, imc=imc, faixa=faixa)

if __name__ == '__main__':
    app.run(debug=True)