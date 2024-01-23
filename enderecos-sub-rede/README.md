
## Desenvolva uma aplicação em Python que retorne todos os possíveis endereços para hosts em uma sub-rede.

** Deve ser desenvolvida uma função chamada hosts_addr, que possui dois parâmetros
* um endereço IP (string) válido na sub rede e a máscara de rede, em notação de / (string).
* A função deve gerar todos os endereços IP possíveis de serem utilizados em hosts na sub-rede.


Protótipo:

def hosts_addr(ip, mask):
...
<código aqui>
Um exemplo de chamada da função seria:
ip = '192.168.246.250'
mask = '24'
for ip in hosts_addr(ip, mask):
print(ip)
A saída na tela deve ser:

192.168.246.1
192.168.246.2
192.168.246.3
...
192.168.246.252
192.168.246.253
192.168.246.254

Neste exemplo serão retornados todos os endereços IP válidos para hosts na subrede. Observe
que o endereço da rede e o endereço de broadcast são omitidos, visto que não são válidos para
hosts.

Outros exemplos
Entradas:

ip="192.168.246.250"
mask="16"

Saída:

192.168.0.1
192.168.0.2
192.168.0.3
...
192.168.255.252
192.168.255.253
192.168.255.254

Entradas:

ip="192.168.246.250"
mask="8"

Saída:

192.0.0.1
192.0.0.2
192.0.0.3
...
192.255.255.252
192.255.255.253
192.255.255.254
