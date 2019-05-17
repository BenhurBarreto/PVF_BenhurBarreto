#-------Benhur Barreto dos Santos-------
#--------Prova Exercicio ViaFlow--------
#----------Inicio 16/05/2019------------
#--Data da Ultima alteracao:17/05/2019--

#funcoes criadas para as operacoes por DEF, declaradas anterior ao loop principal do programa.
#foram criadas na intecao de dar mais clareza e entendimento ao codigo
def soma(num1,num2):
	return num1 + num2
def subtracao(num1,num2):
	return num1 - num2
def multiplicacao(num1,num2):
	return num1 * num2
def divisao (num1,num2):
	return num1 / num2

continua = 's' #variavel que da condicao de funcionamento ao loop principal. So ira funcionar se o valor for 's', de 'sim'.

while (continua == 's'): #loop principal

	print("\n")
	print("Selecione um operador para o uso da Calculadora:\n")
	print("\t'+' ou \n\t'-' ou \n\t'*' ou \n\t'/'.\n")
	
	while True: # loop de selecao do operador de calculo. O programa sai do loop ate que uma das condicoes propostas seja aceita.

		selecao = raw_input("Operador: ")
		#print("\n")

		if selecao == '+': 
			print("Operador de SOMA '+' valido.\n")
			break #quando a operacao e valida, o break quebra o loop e a execucao do codigo segue adiante.
	
		elif selecao == '-': 
			print("Operador de SUBTRACAO '-' valido.\n")
			break
	
		elif selecao == '*': 
			print("Operador MULTIPLICACAO '*' valido.\n")
			break
	
		elif selecao == '/': 
			print("Operador de DIVISAO '/' valido.\n")
			break
		else: 
			print("Operador invalido. Por favor, utilize operadores validos.") #caso o operador informe uma operacao invalida, loop permanece.
	
	while True: #primeiro loop de verificacao do 1 numero digitado(numerador). Caracteres ou qualquer informacao diferente de um numero, nao sera considerado.
	
		num1 = raw_input("Numero 1: ")
		#e neste TRY que a verificacao e feita. Se foi digitado um caractere invalido, o python vai ter problemas na conversao para float.
		#isto vai quebrar a condicao de funcionamento do TRY e vai sergui na EXCEPT, informando ao usuario pelo PRINT que e um numero invalido.
		#como esta no loop, so saira deste ponto se for digitado um numero real.
		try: 
			val = float(num1)
			print("Numero Valido.\n")
			n1 = float(num1)
			break
		except ValueError:
			print("Numero Invalido. Digite novamente.")
	
	while True:
	
		num2 = raw_input("Numero 2: ")
		#similar ao loop anterior, o 2 numero(denominador da operacao) agrega uma funcao a mais. Quando for uma divisao, o zero nao e aceito.
		try:
			val = float(num2)
			if (val != 0 and selecao == '/'): #IF que funciona apenas na operacoes de divisao '/', garantindo que o numero seja valido.
				print("Numero Valido.\n")
				n2 = float(num2)
				break
			elif (val == 0 and selecao == '/'): #ELIF que funciona para informar ao usuario que o zero nao e permitido.
				print("A divisao por ZERO nao e' aceita. Digite novamente.")
			else:
				print("Numero Valido.\n") #ELIF que funciona nas operacoes de '+', '-' e '*'.
				n2 = float(num2)
				break
		except ValueError: #caso seja um caractere invalido, o EXCEPT vai reagir e informar o usuario.
			print("Numero Invalido. Digite novamente.")
	
	#ja com as informacoes necessarias para fazer uma operacao, as condicoes de IF e ELIF atuam conforme a escolha do usuario.
	if selecao == '+': 
		resultado = soma(n1,n2)
		print "Resultado: %r + %r = %r\n" % (num1,num2,resultado)
	
	elif selecao == '-':
		resultado = subtracao(n1,n2)
		print "Resultado: %r - %r = %r\n" % (num1,num2,resultado)
	
	elif selecao == '*': 
		resultado = multiplicacao(n1,n2)
		print "Resultado: %r * %r = %r\n" % (num1,num2,resultado)
	
	elif selecao == '/': 
		resultado = divisao(n1,n2)
		print "Resultado: %r / %r = %r\n" % (num1,num2,resultado)
	
	#por fim, o programa pergunta ao usuario se o mesmo tem interesse em continuar usando-o.
	#as opcoes disponiveis para continuar e 's' de sim ou, 'n' de nao. Qualquer caractere diferente nao sera aceito.
	continua = raw_input("Deseja efetuar mais um ca'culo? s/n: ")
	while True:
		if continua == 's': break
		elif continua == 'n': break
		else: 
			continua = raw_input("Digite s ou n para selecionar se deseja continuar no programa. s/n: ")
	print("#################################################################")