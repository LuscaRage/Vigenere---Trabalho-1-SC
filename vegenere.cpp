#include <iostream>
#include <string>
using namespace std;

string senhaRepetida(string senha, string mensagem) { // gera a repetição de senha no local correto
    int tamanhoSenha = senha.size();
    int tamanhoMensagem = mensagem.size();
    string senhaGerada = "";

    for (int i = 0, j = 0; i < tamanhoMensagem; i++) {
        char charMensagem = mensagem[i];
        if (isalpha(charMensagem)) {
            char charSenha = senha[j % tamanhoSenha];
            senhaGerada += isupper(charMensagem) ? toupper(charSenha) : tolower(charSenha);
            j++;
        } else {
            senhaGerada += charMensagem; // Manter caracteres não alfabéticos inalterados
        }
    }
    return senhaGerada;
}

string geraCriptograma(string senha, string mensagem) {
    int tamanhoMensagem = mensagem.size();
    string senhaGerada = senhaRepetida(senha, mensagem);
    string criptograma;

    for (int i = 0; i < tamanhoMensagem; i++) { // gera o criptograma utilizando a senha gerada
        char charMensagem = mensagem[i];
        if ((charMensagem >= 65 && charMensagem <= 90) || (charMensagem >= 97 && charMensagem <= 122)) {
            int shift = isupper(charMensagem) ? 'A' : 'a';
            char charCifrado = ((charMensagem - shift + senhaGerada[i] - shift + 26) % 26) + shift;
            criptograma += charCifrado;
        } else {
            criptograma += charMensagem; // Manter caracteres não alfabéticos inalterados
        }
    }

    return criptograma;
}

string decifraCriptograma(string senha, string criptograma) { // descptografa utilizando a senha
    int tamanhoCriptograma = criptograma.size();
    string senhaGerada = senhaRepetida(senha, criptograma);
    string mensagemDecifrada;

    for (int i = 0; i < tamanhoCriptograma; i++) {
        char charCifrado = criptograma[i];
        if (isalpha(charCifrado)) {
            int shift = isupper(charCifrado) ? 'A' : 'a';
            char charDecifrado = ((charCifrado - shift - senhaGerada[i] + shift + 26) % 26) + shift;
            mensagemDecifrada += charDecifrado;

        } else {
            mensagemDecifrada += charCifrado; // Manter caracteres não alfabéticos inalterados
        }
    }

    return mensagemDecifrada;
}

int main() {
    string senha, mensagem;
    cout << "Digite a senha: ";
    getline(cin, senha);
    cout << "Digite a mensagem: ";
    getline(cin, mensagem);
    cout << "\n\n";
    string criptograma = geraCriptograma(senha, mensagem);
    cout << "Criptograma: " << criptograma << "\n\n";
    string mensagemDecifrada = decifraCriptograma(senha, criptograma);
    cout << "Mensagem Decifrada: " << mensagemDecifrada << endl;

    return 0;
}
