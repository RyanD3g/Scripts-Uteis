import re;
import random;

def ConstructorPassword(function):
    def wrapper():
        simbols = ["!","@", "#", "%", '&', "*", "()", ":", "_", "~", ";", "."];
        generated = False;
        print("======= VERIFICADOR DE SENHAS ======= \n");
        returnData = function();
        print("\n=====================================\n");
        if len(re.findall(re.compile("[A-Z]"), returnData)) == 0:
            caractereChanged = random.randint(0, len(returnData) - 1)
            returnData = re.sub(returnData[caractereChanged], returnData[caractereChanged].upper(), returnData);
            generated = True;
        if len(re.findall(re.compile("\d"), returnData)) == 0:
            returnData = returnData + str(random.randint(17,900)) + str(random.randint(92,700));
            generated = True;
        if(len(re.findall(re.compile("\W"), returnData))) == 0:
            caracSpecial = returnData[random.randint(0, len(returnData) - 1)] + simbols[random.randint(0, len(simbols) - 1)] + simbols[random.randint(0, len(simbols) - 1)];
            returnData = re.sub(returnData[random.randint(0, len(returnData) - 1)], caracSpecial, returnData);
            generated = True;
        return [generated, returnData];
    return wrapper;

@ConstructorPassword
def password_Generator():
    password = input("Digite sua senha: ");
    return password;

execute = password_Generator();

if execute[0]:
    print("===== SENHA GERADA PELA MAQUINA =====");
    print(f"\n{execute[1]}");
else:
    print("==== PARABÉNS! SUA SENHA É FORTE ====");
    print(f"\n{execute[1]}");
print("\n=====================================");