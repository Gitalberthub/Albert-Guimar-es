def cifra(mensagem, crip_descrip):
    m = ''
    
    for i in range(len(mensagem)-1,-1,-1):
        m = m + (chr(ord(mensagem[i])+(crip_descrip * 979234)))
    return  m

def criptografar(mensagem):
    menscripto = cifra(mensagem, 1)
    return menscripto

def descriptografar(mensagem):
    mensdescripto = cifra(mensagem, -1)
    return mensdescripto

print(" >>>PROGRAMA DE CRIPTOGRAFIA<<<")

controle = 0

nome = input("\n Digite seu nome: ")
cargo = input(" Digite seu cargo: ")

if (cargo == "Inspetor") or (cargo == "inspetor"):
    trajes = input(" Você está devidamente trajado? (S/N)\n Opção selecionada: ")
    if (trajes == "s") or (trajes == "S"):
        op = "N"
        while op != "S" and op != "s":
         
            sel = int(input("\n Selecione:\n 1 - Para Criptografar uma mensagem.\n 2 - Para Descriptografar uma mensagem.\n 3 - Para Finalizar o Programa.\n Opção selecionada: "))

            if (sel == 1):
       
                mensagem = input("\n Escreva a mensagem que deseja criptografar:\n Mensagem: ")

                max = 128
                tam = len(mensagem)
                if tam <= max:
                    criptografar1 = criptografar(mensagem)
                    
                else:
                    print("\n Sua mensagem tem", tam, "caracteres", "somente 128 carateres permitidos, verifique!")
                    break

                controle +=1

                print(" A mensagem criptografada é: ", criptografar1)
        
            elif (sel == 2):
            
                sel2 = int(input("\n Selecione:\n 1 - Para Desctriptografar mensagem anteriormente digitada.\n 2 - Para Descriptografar uma nova mensagem.\n Opção selecionada: "))
      
                if sel2 == 1:
                    if controle == 0:
                        print("\n Nenhuma mensagem cripografada anteriormente. Verifique!")

                    else:                
                        if controle == 1:
                            descriptografar2 = descriptografar(criptografar1)
                            print("\n A mensagem descriptografa é: ",descriptografar2)                  
                
                if (sel2 == 2):
                    mensagem2 = input("\n Digite a mensagem a ser Descriptografada: ")
                    descriptografar3 = descriptografar(mensagem2)
                    print("\n A mensagem descriptografada é: ", descriptografar3)

                if (sel2 != 1 and sel2 != 2):
                    print("\n Digite uma opção válida!\n Selecione um número de 1 à 2.")
        

            elif (sel == 3):
                break
    
            else:
                print("\n Digito inválido!\n Selecione um número de 1 à 3.")
        
            op = input("\n Deseja finalizar o programa? (S/N)\n Opção selecionada: ")
    else:
        print("\n Vista-se corretamente para ter o Acesso liberado!")
else:
    print("\n Somente pessoas Autorizadas!" "\n O nome ", nome,", não está autorizado!")
    
print("\n Programa Finalizado com sucesso!")

