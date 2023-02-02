## Leitura de Código de Segurança Energisa

### Intro
Para a realizacao do projeto de energia solar, precisamos estabelecer uma automacao para fazer o download das contas de energia automaticamente. Para tal, a Energisa utiliza um sistema de autenticacao por email.
O objetivo desse requisito eh ler o codigo de seguranca que foi enviado por email, e toda vez que um novo codigo de seguranca chegar, deve ser impresso na tela junto com o seu codigo.
### Requisitos
- Deve ser desenvolvido em Python3
- O processo deve ser continuo, e deve escutar qualquer e-mail que chegue para o e-mail exemplosolar@gmail.com , senha `bigorna123`
- Ao chegar um email do remetente `sergio@yourecm.com` ou outro email utilizado para teste, com o titulo `Fwd: Código de segurança da Energisa`, ele deve:
	- Imprimir o nome do usuario (no caso de exemplo, FERNANDA BRITO BANDEIRA)
	- Imprimir o codigo de seguranca na tela (no caso de exemplo, 3740)
	- O codigo deve estar bem estruturado e simples, seguindo pelo menos as diretrizes PEP 8.


## Instalação das dependências usando pip:

- IMAP4: ```pip install imaplib```
- Celery: ```pip install -U Celery```
- É necessário estar executando o Redis na porta 6379, basta iniciá-lo: ```docker run --name redis -d redis```
