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

# Parte 2 -  "Ataque"

Agora na parte 2 é requisitado que o programa recebe uma mensagem criptografada em inglês e uma em português. A senha dessas mensagens deve ser recuperada. Deve ser utilizado análise de frequência numérica para o ataque. Este foi feito em python. 

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

```
q buv mw fgmi gwt zqne ui rvc pntpgv wx nrdks g yaf bgzg maizkp sfe dm hib pshcgggc o hcg iw mesq rst gotm pypna rzvmuea smdiw yed xkvcea smdiw yed vkrifed dcm dpbvz q uwp el jgfk aoi dqgg burag wgxpim gvc cuzu g fgx aebgw fz fzu gy ll trdc e oprtm q uwp el jgfk aoi dqgg xe wibmc eaf ucp sfe ai gvc yoiucp cnoilcv pz bzlg gcoa uwps fp bfbggq p crbchqc dv tcxc lgfzc xg doizk eicaumemfz sv agy rwaew gvc noebte q xel nkkcoo dmw fgx, vfkg jqt bvu uyepdzlq tccasmpw rca mwei eldr lqrq oe swviez e tivefzr um nevl axwte vp sfztm crrrlggkoo jm uiw alrvq itl cfvvvc z mvc hmildf ugy dpm, mwei hzi smo wwneuqfs rlrrjgru arr dqgg
```
Ou em inglês:
```
"mztufgmzozs" qgqgt'h owswt hb vqgifvtq ae grjusy, huae ugar jqkgfqk nzobq dgqq oav zczvvfs srgr, a ma hslgzr icanubisq sf hnwf hawth. nxfsx urlfwtu pgydrsgwxm zcbdqr hm futsjiyazu cwgz ym udcgzsth pzmbmway fwssf gz ak znkf aobhlq otr ewriyway fc vfbnurk qbfrwxanluct deaaf zc gzq rgm bx fvk anlov gg gg bzgm gaysy, zbkubm huae kgm fgysncj xqzz siwz kuffw fvgb v zmr zvbmsvz dbkewhzr. ek dxscsdozwbf ioy ghhqfoce, ek drol omg yicwdwuf, nfp w rcfl, ec o rbf'f gks n jqoyca la qubgazik saymuobt az ot oplujohl otsxs jzmh og jafvob zq octhegx wy ciwdknsyeubmzl gghcsvytsj pl otoz wf fah. o oz vabk kvlt quacwfwzwiw bcqszgz, otr lgg kub'g yqh g tbfp tgfroqzr. huae quazmzwzm vk ublsplqr zc vle fucgk iwzv n vqukbrjmhojr vugkofw fvgh tjaky ggjabmse ghsx hveq pah flady gugdh ut xaxzobt afg ncfl. fcafasysthf mesj hb zmjk o pgydkhvlujk gcadwz og ltsof uwmfz, huae vgg owqb zfnfedroalqr gbq jqdropwp kohu sz oxhvxuqooy gdugb gzmh lsrve ct jvldwuz nfp auqxwdm lfbe ubyspmds rwglxs hclk fvgh uwoyrs oq fvk gvvqzobrk mbj hrsd sgqu gfvkf gg evxsqk ajkf fudovg bx mhzsaluct. huw qbbwegzakbg oq tuggwdsj vnk ffgdcwp iy oyd xwqs gzug ob n nuqochk omizr, szr kgpsbwtu vl dswivjqg gqpwbhgbpw at zvr zmfyvrkf fkoyafm cs ndx gifnenzk hb wjdrovf mkgm, gzmh tcaw at zvr uaithyweg yhesubobt wrtufgk is vig ggfysynqg zveggun vrjq kozy whsx ozggbz hb gzs ywayxs yvvfubm uyayakf bx ewmbvxuqgbpw. u kuiyv yoqs gzug zvr wzr, hig oafrr pmb wy ggaxz ubtgubm, oav u kuiyv zsbse dqobs fg yotm tjqoz teaqbjg bmf hu req, ec o'zy kgtlse ltfuitz m tkk zgds mozwe tuf gzqa. ubr dmgz huazu hssgds o zrshs ech sxz zc ewmqz kvlt rogqsub, xwqaoirs, nfp gkzs-juunhrggg lsenaf, hssgds ech va sbseqfvobt az muie hakkf gg ywtwzals sm jgdry oav fvuitzfg, hck ltss ic szr yvbnq hnsz la guar uapcsotqr icefqf ut lggf sszgdm, gbq zadk huwk rognhbsgf sgdsbse se o yhnaz ct mbmd tobvlq hoar ydcabq la ragg. xdcs huae auarff ct, bbltwtu lgg ggm zsfhkff la ak. huw rcazrkf wtghdfg ech zgfr kvlt wthrff hu kbmzr cwyd oorayq eszhyw mh zvr wmfzv owrcxs zq rskh, nfp hns iwzcs mbm edoh jaxz hfvfs orz gzq dgwa gr o coee eisarj nfksmw. kca oew xsyg gzmb gblltwtu lgg qgb pgzqkwiw, ivozr a ooxfl gz, pxwzeubm kvlt xum qaehozywp txcz vqhgqueqbz.
```
5. Se o retorno não der chave e a mensagem original corretas aperte ‘D’. Caso contrário, aperte qualquer outra coisa. 

