                    Para ativar o ambiente virtual

Abra o CMD na pasta raiz do projeto.
Execute os comandos abaixo para criar e ativar o ambiente.
python -m pip install virtualenv

python -m venv venv

pip install --upgrade pip

.\venv\scripts\activate

Depois instale suas dependências já dentro do ambiente virtual.

pip install -r requirements.txt

Sobre a política de execução do Windows rode o comando abaixo no powershell como admin.

Set-ExecutionPolicy AllSigned

                Para usar o flask

$env:FLASK_APP="main"


Tutoriais utilizados:

https://www.youtube.com/watch?v=OqwZGkif3ro&t=2s

https://www.youtube.com/watch?v=rGT5lG71pMQ

https://pt.stackoverflow.com/questions/399556/problema-em-ativar-o-ambiente-virtual-com-pipenv

https://www.youtube.com/watch?v=9Z8fR35r7oY

https://www.youtube.com/watch?v=DjCd_e0ymhI