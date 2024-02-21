import sys
import subprocess
import os

def verificar_mod3_vazio():
    # Executa o xmodmap e captura a saída
    resultado = os.popen('xmodmap').read()
    # Verifica se esta vazio na saída
    return "Scroll_Lock (0x4e)" not in resultado

def remove_tecla_scroll_lock():
    if sys.platform.startswith('linux'):
        if not verificar_mod3_vazio():
            os.system("xmodmap -e 'remove mod3 = Scroll_Lock'")

def configurar_teclado():
    if sys.platform.startswith('linux'):
        if verificar_mod3_vazio():
            print("Executando código de configuração do teclado...")
            os.system("xmodmap -e 'add mod3 = Scroll_Lock'")
            print("Configuração de teclado concluído.")
        else:
            print("Tecla Scroll Lock encontra-se já configurada.")

if __name__ == "__main__":
    configurar_teclado()