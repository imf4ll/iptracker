# Function that receives an ip as a parameter and validates it by returning True or False
def validates_ip(ip):
    if ip.count('.') != 3:
        return False
    else:
        caracteres = ip.split('.')
        for caracter in caracteres:
            if not caracter.isdigit():
                return False
            else:
                continue
        return True
