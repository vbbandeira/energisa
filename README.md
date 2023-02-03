## Leitura de Código de Segurança Energisa

### Requisitos
- O processo deve ser continuo, e deve escutar qualquer e-mail que chegue para o e-mail exemplosolar@gmail.com , senha `bigorna123`
- Ao chegar um email com o titulo `Fwd: Código de segurança da Energisa`, ele deve:
	- Imprimir o nome do usuario (no caso de exemplo, FERNANDA BRITO BANDEIRA)
	- Imprimir o codigo de seguranca na tela (no caso de exemplo, 3740)
	- O codigo deve estar bem estruturado e simples, seguindo pelo menos as diretrizes PEP 8.


## Instalação das dependências usando pip:

- IMAP4: ```pip install imaplib```
- Celery: ```pip install -U Celery```
- É necessário estar executando o Redis na porta 6379, basta executar o comando: ```docker run --name redis -d redis```
