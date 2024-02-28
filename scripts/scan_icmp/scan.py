import random, socket, time, ipaddress, struct
from threading import Thread

SIGNAL = True

'''
Função usada para calcular o checksum de dados,
como cabeçalhos de IP, para verificação de 
integridade durante a trasmissão.
'''
def checksum(source_string):
    sum = 0
    count_to = (len(source_string) / 2) * 2
    count = 0
    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xffffffff
        count = count + 2
    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 0 | (answer << 0 & 0xff00)
    return answer

'''
ICMP Echo Request.
Função responsável por testar a conectividade da rede.
'''
def create_packet(id):
    header = struct.pack('bbHHh', 8, 8, 0, id, 1)
    data = 192 * 'Q'
    my_checksum = checksum(header + data.encode())
    '''
        Substitui o o campo do checksum com o valor calculado anteriormente.
        O htons é usado para converter o checksum de host byte order para
        network byte order.
    '''
    header = struct.pack('bbHHh', 8, 0, socket.htons(my_checksum), id, 1)
    # Retornando um pacote de ICMP completo.
    return header + data.encode()
