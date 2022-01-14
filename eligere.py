import streamlit as st
from PIL import Image

#iniciando o app
img = Image.open('1641836729109.png')

st.image(img)

st.subheader('Preencha os campos abaixo com as características do seu viveiro e '
'veja quais espécies são ideais para que você inicie sua produção com sucesso!')
#input
ph = st.slider('Defina o Ph da água do viveiro', min_value=0, max_value=14)
salinidade = st.radio('Selecione a salinidade da água do seu viveiro', ('Água potável', 'Água salgada'))
temperatura = st.slider('Define a temperatura da água do seu viveiro', min_value=0, max_value=40)

if ph<6 or ph>8:
  st.warning('Para obter sucesso em sua criação, o pH da água do seu viveiro deve estar entre 6 e 8. Faça a manutenção corretamente do ambiente para iniciar sua produção na frente!')
else:
  if salinidade == 'Água potável':
    if temperatura >= 18 and temperatura < 22:
      esp1, esp2 = st.columns(2)
      with esp1:
        st.subheader('Carpa comum')
        carpa = Image.open('carpa.png')
        st.image(carpa)
        st.markdown('Essa espécie é mais produzida nas regiões Sul e Sudeste. Ela pode ' 
                  'chegar a mais de 1,2 metro e 40 kg, porém, normalmente é comercializada '
                  'ainda pequena — entre 1 e 6 kg. Carpas são capazes de sobreviver em diversos '
                  'ambientes aquáticos, incluindo água salobra ou com pouca oferta de oxigênio.')
      with esp2:
        st.subheader('Matrinxã')
        matrinxa = Image.open('matrinxa.png')
        st.image(matrinxa)
        st.markdown('Produzida principalmente nas regiões Centro-Oeste e Norte, é uma '
        'espécie que chama atenção dos criadores por conta da sua grande rusticidade, '
        'rápido crescimento e alto valor comercial. Em termos de tamanho, chega a 70cm '
        'de comprimento e 8,6 quilos.')
    elif temperatura >= 22 and temperatura < 28:
      pirapitinga, pintado, jundiá = st.columns(3)
      with pirapitinga:
        st.subheader('Pirapitinga')
        pirati = Image.open('pirapitinga.png')
        st.image(pirati)
        st.markdown('Essa espécie é mais produzida na região Norte, é o terceiro maior '
        'peixe de escamas da Amazônia. A pirapitinga é um peixe muito importante no '
        'mercado nacional. Isso se deve ao fato de ele ser um peixe grande, que normalmente '
        'chega aos 14 quilos em idade adulta. Além disso, possui fácil adaptação às condições '
        'naturais, como água e alimentação.')
      with pintado:
        st.subheader('Pintado')
        pintado = Image.open('pintado (2).png')
        st.image(pintado)
        st.markdown('As regiões Centro-Oeste e Sudeste são as campeãs de produção desta '
        'espécie no Brasil. É um peixe de couro, tendo seu sabor apreciado por seus consumidores.'
        ' Pode alcançar pesos próximos a 80 kg e quase 2m de comprimento. Um fato curioso é '
        'que esse peixe pode ser utilizado no controle de população de tilápias em açudes e tanques.')
      with jundiá:
        st.subheader('Jundiá')
        jundia = Image.open('jundia.png')
        st.image(jundia)
        st.markdown('Com grande apreço na região Sul do país, essa espécie se destaca por ser '
        'uma das mais promissoras no cultivo por meio da Aquicultura, uma vez que apresenta '
        'rápido crescimento, fácil adaptação à criação intensiva, alta rusticidade, fácil '
        'indução à reprodução com alta taxa de fecundação, possuindo ainda carne saborosa de '
        'baixo teor de gordura e poucas espinhas. Pode atingir 50cm de comprimento e 3 kg.')
      piau_açu, curimbatá, matrinxã = st.columns(3)
      with piau_açu:
        st.subheader('Piau-açu')
        piau = Image.open('piauacu.png')
        st.image(piau)
        st.markdown('É um peixe de escamas geralmente produzido na região sudeste que '
        'pode alcançar até 60 cm de comprimento total e pesar até 5 Kg. Possui um ' 
        'rápido crescimento, podendo ser fonte de renda por meio do comércio de carne '
        'e de exemplares vivos para pesque e pague.')
      with curimbatá:
        st.subheader('Curimbatá')
        curimb = Image.open('curimbatá.png')
        st.image(curimb)
        st.markdown('Produzidos comunmente nas regiões Norte e Centro-Oeste, onde os '
        'machos podem pesar mais de 5kg e chegar aos 58cm e as fêmeas ultrapassam '
        'os 70 cm e pesam mais de 6 quilos em alguns casos. São robustos, prolíficos '
        'e longevos, podendo chegar a viver por até 10 anos.')
      with matrinxã:
        st.subheader('Matrinxã')
        matrinxa = Image.open('matrinxa.png')
        st.image(matrinxa)
        st.markdown('Produzida principalmente nas regiões Centro-Oeste e Norte, é uma '
        'espécie que chama atenção dos criadores por conta da sua grande rusticidade, '
        'rápido crescimento e alto valor comercial. Em termos de tamanho, chega a 70cm '
        'de comprimento e 8,6 quilos.')
    elif temperatura >= 28 and temperatura <= 30:
      tilápia, pacu, tambaqui = st.columns(3)
      with tilápia:
        st.subheader('Tilápia')
        tilap = Image.open('tilapia.png')
        st.image(tilap)
        st.markdown('\n Essa espécie é produzida principalmente nas regiões Nordeste, '
        'Sudeste e Sul do Brasil. Se reproduz facilmente e crescem com rapidez, '
        'apresentando grande rusticidade, fácil manejo e alto nível de rusticidade.'
        ' Além disso, possui carne de ótima qualidade, poucas espinhas e saboroso')
      with pacu:
          st.subheader('Pacu')
          pacu = Image.open('pacu.png')
          st.image(pacu)
          st.markdown('Sua produção é maior nas regiões Centro-Oeste e Sudeste, ' 
          'sendo um peixe de escamas pequenas e numerosas, sua carne é considerada muito ' 
          'saborosa e por conta disso é muito comercializado. Ele pode alcançar mais de 70cm ' 
          'de comprimento e pesar até 20Kg.')
      with tambaqui:
        st.subheader('Tambaqui')
        tambaqui = Image.open('tambaqui.png')
        st.image(tambaqui)
        st.markdown('Espécie mais produzida na região Norte, sendo o segundo maior peixe de '
        'escama do Brasil e sua reprodução artificial vem sendo feita com sucesso. O '
        'tambaqui é a espécie mais intensamente pescada na região Amazônica, inclusive '
        'sua carne é exportada para outros países.')
      pirarucu, tambatinga, matrinxã = st.columns(3)
      with pirarucu:
        st.subheader('Pirarucu')
        piraru = Image.open('pirarucu.png')
        st.image(piraru)
        st.markdown('É o maior peixe de escamas do Brasil e, devido à sua excelente '
        'carne, é considerado “o Bacalhau Brasileiro”. Sua maior produção encontra-se '
        'na região norte do país. O peixe não tem espinhos em “y” '
        'e é um peixe com boa comercialização, o que indica uma ótima oportunidade para '
        'quem quer entrar no mercado. Pode atingir até 2,10m de comprimento e 112Kg de peso.')
      with tambatinga:
        st.subheader('Tambatinga')
        tambat = Image.open('tambatinga.png')
        st.image(tambat)
        st.markdown('Essa espécie é mais produzida na região Norte, e possui um ótimo '
        'desempenho produtivo. Além disso a tambatinga, apresenta cabeça menor que '
        'o tambaqui e o tambacu, o que lhe confere um melhor rendimento de carcaça, '
        'ou seja, tem maior quantidade de carne e rendimento de filé em relação às '
        'espécies comentadas. Sua faixa de peso é de 800 gramas a 1,2kg.')
      with matrinxã:
        st.subheader('Matrinxã')
        matrinxa = Image.open('matrinxa.png')
        st.image(matrinxa)
        st.markdown('Produzida principalmente nas regiões Centro-Oeste e Norte, é uma '
        'espécie que chama atenção dos criadores por conta da sua grande rusticidade, '
        'rápido crescimento e alto valor comercial. Em termos de tamanho, chega a 70cm '
        'de comprimento e 8,6 quilos.')
    else:
      st.error('Não encontrada espécie compatível. Tente novamente!')
  elif salinidade == 'Água salgada':
    if temperatura > 9 and temperatura <= 18:
      salmão, ff = st.columns(2)
      with salmão:
        st.subheader('Salmão do atlântico')
        salmão = Image.open('salmão.png')
        st.image(salmão)
        st.markdown('É um peixe muito conhecido e consumido no mundo todo. Essa espécie '
        'não é encontrada de forma natural no Brasil, sendo originária da costa leste '
        'da América do Norte. Sua cor, textura e sabor único, fazem do salmão um dos '
        'pescados mais consumidos no Brasil. Costuma medir entre 60 e 110 cm e mesmo '
        'chegar aos 150cm.')
      with ff:
        st.subheader('')
    elif  temperatura >= 20 and temperatura <= 30:
      beijupirá, garoupa, robalo = st.columns(3)
      with beijupirá:
        st.subheader('Beijupirá')
        beiju = Image.open('beijupira.png')
        st.image(beiju)
        st.markdown('Sua produção ganha destaque na região Nordeste, onde em condições '
        'normais de cultivo, o peixe pode chegar a 10 kg em 16 meses, além de apresentar '
        'facilidade para desovar em cativeiro, resposta positiva à vacinação e boa '
        'adaptabilidade ao ambiente de confinamento. Seu comércio é mais popular em '
        'países como EUA e Bélgica, porém, tem ganhado destaque no Brasil nos últimos anos.')
      with garoupa:
        st.subheader('Garoupa')
        garoupa = Image.open('garoupa.png')
        st.image(garoupa)
        st.markdown('Essa espécie é encontrada no mundo todo, porém, no Brasil, a região '
        'de maior produção é a Sudeste. Ela é considerada uma das mais valorizadas pelos '
        'consumidores nacionais, por isso, tem alto valor no mercado podendo atingir '
        'US $60,00/kg. O peixe pode chegar a medir até um pouco mais de 1,5 metro e '
        'atingir 60 quilos, apresentando características interessantes para a produção em cativeiro.')
      with robalo:
        st.subheader('Robalo')
        robalo = Image.open('robalo.png')
        st.image(robalo)
        st.markdown('Esta espécie é uma ótima opção para produção na região Nordeste. '
        'Reverenciado pelos Chefs de Cozinha mais renomados por sua nobreza, textura'
        ' e versatilidade, além de ser amado por quem o saboreia. Entre as espécies' 
        'marinhas e estuarinas, o grupo desse peixe é o que possui maiores possibilidades'
        ' de crescimento no que diz respeito ao volume de produção.')
    else:
      st.error('Não encontrada espécie compatível. Tente novamente!')
st.write('__________________________________________________________________________________')
logo, somos, contato = st.columns(3)
with logo:
  redondo = Image.open('logo redondo.png')
  st.image(redondo, width=275)
with somos:
  st.markdown('**QUEM SOMOS**')
  st.markdown('Com o incentivo da disciplina de Fundamentos da Computação,'
  ' EligerePISCES é um aplicativo criado por alunos da Universidade Federal'
  ' do Maranhão (UFMA), matriculados no curso de Engenharia de Pesca, que buscam'
  ' se desenvolver a partir da ciência e tecnologia. O intuito é facilitar e progredir'
  ' a piscicultura dos produtores brasileiros no momento de definir a espécie de criação.')
with contato:
  st.markdown('**ENTRE EM CONTATO CONOSCO**')
  insta = Image.open('insta.png')
  st.image(insta, width=100)
  st.markdown('[@eligere_pisces](https://www.instagram.com/eligere_pisces/)')
  email = Image.open('email.png')
  st.image(email, width=100)
  st.markdown('[eligerepisces@gmail.com](<mailto: eligerepisces@gmail.com>)')