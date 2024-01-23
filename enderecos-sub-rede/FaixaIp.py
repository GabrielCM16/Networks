
def retorna_endereço_rede(ip, redestr):
  mask = int(redestr)
  ip_binario = str()
  ip_decimal = str()
  ipp = list()
  cont = 0
  ip_octetos = ip.split('.')

  #transforma o ip separado por octetos em binarios em um str separando o "0b"
  for i in ip_octetos:
    ip_binario += bin(int(i))[2:].rjust(8, '0')

  # calcula a mascara do ip
  ip_binario = ip_binario[:mask] + '0' * (32 - mask)

  # convertendo o end de rede que esta em binario para decimal
  for i in range(0, 32, 8):
    if i <= 23:
      ip_decimal += f'{int(ip_binario[i:i+8], 2)}.'
      ipp.append(int(ip_binario[i:i+8], 2))
    else:
      ip_decimal += f'{int(ip_binario[i:i+8], 2)}'
      ipp.append(int(ip_binario[i:i+8], 2))

  return ipp



def retorna_broadcast(ip, redestr):
  mask = int(redestr)
  #calcula a mascara
  mascara = '1' * mask
  #funcao ljust coloca o numero necessarios de "0" a direita para deixar o ip valido (32 bits)
  mascara = mascara.ljust(32, "0")

  mak8 = list()
  #separa em uma lista o ip da mascara separando em octetos
  for i in range(0, 32, 8) :
    mak8.append(int(mascara[i: i+8]))

  #separando o ip em octetos
  ip8 = [int(i) for i in ip.split('.')]

  #endereco de broadcast ip ou (nao mask) (nega a mascara)
  #calcula o broadcast
  broadcast = list()
  for i in range(4):
    numero = (256 + (ip8[int(i)] | (~int(f'0b{mak8[int(i)]}', 2))))
    broadcast.append(numero)
  return broadcast



def retorna_faixa_ip(end_rede, broad):
  #final da rede = broadcast
  #começo da rede = network adress
  #for da network adress até o broadcast =  faixa de ips validos na rede

  #coloca em uma string somente com bits o começo da rede (network adress)
  bitsNetworkAdress = str()
  for bits in end_rede:
    #começa do 2 até o final pra tirar o "0b"
    bitsNetworkAdress += bin(bits)[2:].rjust(8, '0')

  #coloca em uma string somente com bits o final da rede (broadcast)
  bitsBroadCast = str()
  for bits in broad:
    #começa do 2 até o final pra tirar o "0b"
    bitsBroadCast += bin(bits)[2:].rjust(8, '0')

  #colocando pra int
  IntNetworkAdress = int(bitsNetworkAdress, 2)
  IntBroadcast = int(bitsBroadCast, 2)

   #ip possiveis = final do ip - começo do ip
  numerosIpValidos = IntBroadcast - IntNetworkAdress

  print("numeros de ip validos = ", numerosIpValidos - 1)

  #for do começo do ip até o final do ip
  for ip_valido in range(IntNetworkAdress + 1, IntBroadcast):
    #ip_valido é um int gigante precisa transformar em ip separado por octetos
    mak8 = list()
    #transforam para str e bin o ip e tira o 0b do bin
    ip_valido = str(bin(ip_valido))[2:]
    #separa em uma lista o ip separando em octetos e transformando para int novamente
    for i in range(0, 32, 8):
      num = int(ip_valido[i: i+8], 2)
      mak8.append(str(num))

    #mak8 é uma lista vamos transformar para str
    mak8Str = ".".join(mak8)

    yield mak8Str


#fim das funções

#começando a calcular

#ip qualquer
ip = '192.168.246.250'
rede = "16"

network_adress = retorna_endereço_rede(ip, rede) #endereço da rede
print("endereço de rede = " ,network_adress)

broadcast = retorna_broadcast(ip, rede) #broadcast
print('broadcast = ', broadcast)

#retorna_faixa_ip(network_adress, broadcast)
for ip in retorna_faixa_ip(network_adress, broadcast):
  print(ip)