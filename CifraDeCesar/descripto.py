alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
passe = input("Digite a palavra a ser desencripitada: ");

proxLetra = "";
nome = "";

a = 0;
b = 0;

for letra in passe:
    if letra in alfabeto:
        a = 0;
        for l in alfabeto:
            if l == letra:
                b = a - 3; 
                proxLetra = alfabeto[b];
            a = a + 1;
        nome = nome + proxLetra;
print(nome);
