# Vigenere--Trabalho-1-SC



#  Parte 1 - "Crifrador E Descifrador"

Aqui foi pedido para que um cifrador recebesse uma mensagem, e que essa mensagem
deve ser cifra segundo a cifra Vigenère, para que assim fosse criado um criptograma que
depois seria usado em um decifrador, que ao receber o criptograma e a chave decifra
segundo a cifra de Vigenère, assim recuperando a mensagem original. Esse foi feito em c++

## Como Rodar
1. Utilize um compilador de c++
2. Execute o código
3. Defina a mensagem e a senha: Você pode inserir qualquer mensagem que desejar, desde que não inclua parágrafos (ou seja, não use a tecla Enter para separar as linhas). Além disso, escolha uma senha sem acentos ou espaços. Por exemplo:
Senha:
```
clarice
```
```
O que eu bebi por você dá pra encher um navio E não teve barril que me fez esquecer O que eu bebi por você nunca artista bebeu Nem pirata bebeu nem ninguém vai beber O que eu bebi por você quase sempre era ruim E bem antes do fim eu já tava à mercê O que eu bebi por você me fazia tão mal Que já era normal acordar no bidê Cada dono de boteco e catador de lata Agora te sorri agradecido Se seu plano era contra o meu fígado Meu bem, você foi bem sucedido Parabéns pra você Cada dono de boteco e catador de lata Agora te sorri agradecido Se seu plano era contra o meu fígado Meu bem, você foi bem sucedido Parabéns pra você.
```
4. A mensagem cifrada e decifrada será exibida na tela.

# Descrição "Ataque"

Agora na parte 2 é requisitado que o programa recebe uma mensagem criptografada em inglês e uma em português. A senha dessas mensagens deve ser recuperada. Deve ser utilizado análise de frequência numérica para o ataque. Este foi feito em python. 
## Como usar

Este código tenta quebrar as mensagens criptografadas usando métodos de quebra de cifras Vigenere através de técnicas como o método de Kasiski para descobrir a chave para descriptografia.

Para quebrar a cifra Vigenere e descobrir a chave usada para criptografar uma mensagem, basta fornecer a mensagem criptografada. O script tentará determinar o tamanho da chave e, em seguida, quebrará a cifra usando uma combinação de análise de frequência de letras e o índice de coincidência.

Caso a chave encontrada não satisfaça a descriptografia, digite "n" para que o código encontre uma chave menor que possa ser correta.

## Como Rodar
1. Abra um terminal e encontre o arquivo.
2. Instale a biblioteca *unidecode*
```
pip install unidecode
```
3. Execute esse comando no terminal.
```
python Parte_2.py
```
4. Digite uma mensagem cifrada sem acentos. Desde que não inclua parágrafos (ou seja, não use a tecla Enter para separar as linhas). Exemplo:

Após aparecer "Digite a mensagem:", escreva:
```
q buv mw fgmi gwt zqne ui rvc pntpgv wx nrdks g yaf bgzg maizkp sfe dm hib pshcgggc o hcg iw mesq rst gotm pypna rzvmuea smdiw yed xkvcea smdiw yed vkrifed dcm dpbvz q uwp el jgfk aoi dqgg burag wgxpim gvc cuzu g fgx aebgw fz fzu gy ll trdc e oprtm q uwp el jgfk aoi dqgg xe wibmc eaf ucp sfe ai gvc yoiucp cnoilcv pz bzlg gcoa uwps fp bfbggq p crbchqc dv tcxc lgfzc xg doizk eicaumemfz sv agy rwaew gvc noebte q xel nkkcoo dmw fgx, vfkg jqt bvu uyepdzlq tccasmpw rca mwei eldr lqrq oe swviez e tivefzr um nevl axwte vp sfztm crrrlggkoo jm uiw alrvq itl cfvvvc z mvc hmildf ugy dpm, mwei hzi smo wwneuqfs rlrrjgru arr dqgg
```
5. Se o retorno não der chave e a mensagem original corretas aperte ‘D’. Caso contrário, aperte qualquer outra coisa. 

