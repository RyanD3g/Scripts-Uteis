alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
palavra = input("Digite a palavra para ela ser criptografada: ");
i = 0;
j = 0;
z = 0;
f = 0;
nome = "";
proxLetra = "";
for letra in palavra:
    f = 0;
    if letra in alfabeto:
        for l in alfabeto:
            if l == letra:
                z = f + 3;
                if z == 26:
                    z = 0;
                elif z == 27:
                    z = 1;
                elif z == 28:
                    z = 2;
                elif z == 29:
                    z = 3; 
                proxLetra = alfabeto[z];
            f = f + 1
        i = j + 3;
        nome = nome + proxLetra;
    j = j + 1
print(nome);
        