print('Calculadora de média')
print('Você quer culcular sua média:\n')
print('1-Bimestral')
print('2-Semestral')
print('3-Anual\n')
opcao = int(input('Digite a opção:'))

if opcao ==1:
    mensal = float(input('Digite sua nota mensal:'))
    trabalho = float(input('Digite sua nota de trabalho:'))
    bimestral = float(input('Digite sua nota bimestral:'))
    
    media = (mensal + trabalho + bimestral) / 2
    
    print("Sua média bimestral foi de {:.1f}!".format(media))
    
elif opcao ==2:
    bimestral1 = float(input('Digite sua nota do 1° bimestre:'))
    bimestral2 = float(input('Digite sua nota do 2° bimestre:'))
    
    media = (bimestral1 + bimestral2) / 2
    
    print('Sua nota do semestre foi {:.1f}!'.format(media))

elif opcao==3:
    semestre1 = float(input('Digite sua nota do 1° semestre:'))
    semestre2 = float(input('Digite sua nota do 2° semestre:'))
    
    media = (semestre1 + semestre2) / 2
    
    print('Sua nota final é {:.1f}!'.format(media))
    
else:
    print("Humm... Acredito que você tenha digitado a opção errada, tente novamente!")    