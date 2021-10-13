# HOME

### Objetivos:

A página `home` tem como objetivo ser a primeira página que o usuário irá acessar, portanto ela contêm as informações que julgamos mais relevantes. São elas: um guia rápido sobre como o projeto funciona e o link para as bibliotecas.

### Código:

A primeira porção do código da página home é responsável por carregar a parte `static` do site(css, scripts de javascript) e algumas extensões. Além disso, assim como todas as páginas do site, a `home` é uma extensão da página(template django) `base`, logo ela tem a estrutura de blocks do Django, carregando o título, e as informações contidas na página `base`. Todo esse processo é realizado pelo framework Django, sendo um padrão de código presente em todas as páginas do site.

```python
{% extends 'site2016/base.html' %}
{% load static %}

{% block title %}
Manual C - PET-BCC UFSCar
{% endblock title %}

{% block head_extensions %}

{% endblock head_extensions %}
```

Na sequência temos a declaração do block `body`. Sendo o primeiro elemento deste bloco o título da página. Para tal, é usado o sistema de `grid` do framework CSS Semantic UI para manter a responsividade.
Neste caso, temos uma coluna com largura de 6 invertida(`inverted`), o que faz com que a coluna tenha um background com a cor definida pelo ID "fundo_azul_titulo". Além da cor, o ID carrega consigo mais algumas propriedades de CSS que fazem a formatação ficar correta para o título, sendo uma delas o `padding-top` que faz com que a coluna fique a abaixo da barra superior padrão do site.
Dentro desta coluna, há um título primário(`h1`) que será o título da página, ele é formatado com o esquema de títulos(`header`) do Semantic UI.

```html
<div class="ui grid">
  <div class="sixteen wide column">
    <header
      class="ui inverted masthead center aligned segment"
      id="fundo_azul_titulo"
    >
      <h1 class="ui inverted header">Manual C</h1>
    </header>
  </div>
</div>
```

##### Grid Semantic UI:

Como o `grid` do Semantic UI é algo muito recorrente nas demais práticas, aqui ficará a explicação básica de seu funcionamento e esta se aplica a todas as demais aparições desta ferramenta.
Basicamente, o `grid` funciona com base em colunas e linhas. Uma linha vai do começo da tela até o final da mesma, sendo as colunas dividas em 16, sendo uma coluna com largura de 16 equivalente a 100% da tela disponível. Logo, uma coluna com 14 de largura ocupará 14/16 de espaço na tela(aproximadamente 87,5% da tela disponível) e quanto menor a largura determinada, menor o percentual de espaço ocupado. Vale ressaltar que o `grid` é responsível, ou seja, 16 colunas são sempre 16 colunas da tela disponível, isso significa que a proporção é mantida em diferentes telas (mobile, desktop. etc.).
Para usar o `grid` é necessário "invocá-lo" com `ui grid` e dentro dele especificar o que se deseja em relação a colunas e linhas.

Agora, na porção `main` da página temos uma declaração de `section` na página que faz com que ela tenha uma formatação de segmento do Semantic UI trazendo o `id` "fundo_cinza" e suas propriedades e um papel de região.
Esta seção se inicia com a declaração do grid do Semantic, sendo o primeiro elemento posicionado em um espaço das 3 colunas iniciais da página(aquelas mais a esquerda). Este elemento é a barra lateral esquerda que é renderizada através de um template a parte somente para ela, isto se deve ao fato de a barra lateral estar presente em todas as páginas do projeto. Logo, para evitar que todas as páginas tivessem o código da barra lateral ela é feita separada em um arquivo html só para ela, e o arquivo é carregado em cada página.

```html
<section class="ui vertical stripe segment" id="fundo_cinza" role="region">
  <div class="ui stackable grid">
    <div class="three wide column">
      {% block sidebar_content %} {% include 'site2016/manualC/leftSidebar.html'
      %} {% endblock sidebar_content %}
    </div>
    <!-- código abaixo omitido para futura explicação -->
  </div>
</section>
```

Na sequência, os demais elementos são dispostos em 12 colunas contendo o Guia Rápido que é dividido em duas colunas, onde uma contem o título e o texto explicativo e a outra, o vídeo de funcionamento do projeto.

```html
<div class="twelve wide column">
  <div class="row">
    <div class="ui padded basic segment">
      <div class="ui two column stackable center aligned grid">
        <div class="column">
          <h2 class="ui center aligned aligned header manC_laranja">
            Guia Rápido
          </h2>
          <div class="justificado">
            Ao lado esquerdo temos uma barra de navegação que te expõe links
            para as bibliotecas. Mais abaixo também há links para as bibliotecas
            da linguagem C juntamente com uma breve descrição sobre o que cada
            uma disponibiliza. C.
          </div>
        </div>
        <div class="column">
          <div class="ui basic segment">
            <video width="500" height="180" controls>
              <source
                src="../../../static/site2016/videos/gravacao_manualc.webm"
                type="video/webm"
              />
              Your browser does not support the video tag.
            </video>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- código abaixo omitido para futura explicação -->
</div>
```

Logo abaixo, temos um divisor de tela para separar a tela em 2 porções. Sendo que na sequência, vem na tela a lista com as bibliotecas disponíveis para consulta. A lista é uma grande linha(ocupa todo o espaço disponível, 12 linhas no caso), que é composta pelo título e pela formatação de lista relaxada do Semantic. Sendo que, ela é divida em `item`'s cada um deles é composto por um conteúdo que é o link para as funções da biblioteca e uma descrição daquela biblioteca. Tal estrutura se de items se repete para cada biblioteca presente no site finalizando o conteúdo presente do template da página home.

```html
<div class="ui divider"></div>
        <div class="row">
          <h2 class="ui center aligned aligned header manC_laranja">
            Bibliotecas
          </h2>
          <div class="ui relaxed divided list">
            <!-- assert inicio -->
            <div class="item">
              <div class="content">
                <a class="manC_laranja odd" href="{% url 'assert_h' %}">
                  <h3>assert.h</h3>
                </a>
                <div class="description justificado">Na biblioteca &ltassert.h&gt tem apenas uma função: assert(), a qual pode ser usada para verificar a veracidade de uma expressão durante a execução do programa e interromper a execução do programa com uma mensagem de diagnóstico em caso de falha. </div>
              </div>
            </div>
            <!-- continuação da lista -->
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
{% endblock %}
```

# SOBRE

### Objetivos:

A página sobre tem por objetivo trazer mais informações do projeto para o usuário. Trazendo nela, o objetivo do projeto, nosso público alvo, um guia rápido sobre a navegação no site, links com contatos nossos para receber sugestões e os professores que colaboraram com o projeto.

### Código:

O código começa com o padrão de título presente em todo o restante do site. Na sequência, tem-se a declaração da porção `main` da página, o primeiro elemento é a barra lateral esquerda que segue o padrão presente no restante do site. Os próximos elementos são dispostos dentro de uma coluna de largura 12, o Guia Rápido e Público Alvo são dispostos numa linha(`row`) que é dividida em 2 colunas, na qual cada coluna vai receber um dos 2 elementos citados. Os elementos em si, são compostos por um `basic segment`(segmento básico sem informação) com um título que é alinhado a esquerda e um texto justificado explicativo logo abaixo.
``` html
{% extends 'site2016/base.html' %}
{% load static %}

{% block title %}
Manual C - PET-BCC UFSCar
{% endblock title %}

{% block head_extensions %}

{% endblock head_extensions %}

{% block body %}
<div class="ui grid">
  <div class="sixteen wide column">
    <header class="ui inverted masthead center aligned segment" id="fundo_azul_titulo">
      <h1 class="ui inverted header">
        Manual C
      </h1>
    </header>
  </div>
</div>
<main role="main" class="main_manC">
  <section class="ui vertical stripe segment" id="fundo_cinza" role="region">
    <div class="ui relaxed grid">
      <div class="three wide column">
        <div class="ui sticky">
          {% block sidebar_content %}
            {% include 'site2016/manualC/leftSidebar.html' %}
          {% endblock sidebar_content %}
        </div>
      </div>
      <div class="twelve wide column">
        <div class="ui relaxed grid">
          <div class="two column row">
            <div class="column">
              <div class="ui basic segment">
                <h2 class="ui left aligned aligned header manC_laranja">
                  Objetivo
                </h2>
                <div class="justificado">
                  A ideia do projeto é fornecer uma guia simples e objetivo para
                  a linguagem de programação C. Contendo a maioria das
                  bibliotecas e funções da linguagem.
                </div>
              </div>
            </div>
            <div class="column">
              <div class="ui basic segment">
                <h2 class="ui left aligned aligned header manC_laranja">
                  Público Alvo
                </h2>
                <div class="justificado">
                  Nosso público alvo são programadores o e pessoas que possuem
                  um conhecimento básico sobre a linguagem e precisam de um
                  lugar para consultas sobre a linguagem C.
                </div>
              </div>
            </div>
          </div>
        </div>
```

Depois tem-se o Guia Rápido que vem na sequência de um divisor de tela, o elemento é um segmento básico também, mas que ocupa 100% da tela disponibilizada pelo grid. Dentro dele há um vídeo com dimensões 720x400 e uma `div` com uma legenda para o vídeo. 
```html
<div class="ui divider"></div>
        <div class="ui padded basic segment">
          <div class="ui stackable center aligned grid">
            <div class="column">
              <h2 class="ui center aligned header manC_laranja">
                Guia Rápido
              </h2>
              <div class="ui basic segment">
                <video width="720" height="400" controls>
                  <source src="../../../static/site2016/videos/gravacao_manualc.webm" type="video/webm">
                Your browser does not support the video tag.
                </video>
              </div>
              <div>
                Caso tenha dúvidas sobre a navegação, assista o vídeo acima. Nele são demonstrados formas de navegar pelo site para consultas. 
              </div>
            </div>
          </div>
        </div>
```

Por fim, há mais dois segmentos que contêm as Sugestões e os Colaboradores, eles seguem a formatação de grid apresentado em Objetivos e Público Alvo. A parte de sugestões é composto por uma sequência de segmentos que linkam os possíveis meios de contato. Em colaboradores temos uma divisão do segmento em duas colunas, na qual uma suportará a foto do professor em questão e a outra um texto descritivo sobre o professor. Isso encerra o conteúdo presente na `main`.
```html
<div class="ui divider"></div>
        <div class="ui relaxed grid">
          <div class="two column row">
            <div class="column">
              <div class="ui basic segment">
                <h2 class="ui left aligned aligned header manC_laranja">
                  Sugestões
                </h2>
                <div class="row">
                  <div class="justificado">
                    Em caso de dúvidas sobre as bibliotecas ou funções, ou sugestões entre em contato conosco por:
                  </div>
                </div>
                <div class="ui basic segment"><a class="ui left aligned aligned header manC_laranja_escuro" href="https://www.facebook.com/petbcc">
                  Facebook 
                </a> </div>
                <div class="ui basic segment"><a class="ui left aligned aligned header manC_laranja odd" href="https://www.instagram.com/petbcc.ufscar/">
                  Instagram 
                </a> </div>
                <div class="ui basic segment"><a class="ui left aligned aligned header manC_laranja_escuro">
                  petbcc@ufscar.br 
                </a> </div>
                <div class="ui basic segment"><a class="ui left aligned aligned header manC_laranja odd" href="https://github.com/petbccufscar/sitepetbcc">
                   Repositório GitHub
                </a> </div>
              </div>
            </div>
            <div class="column">
              <div class="ui basic segment">
                <h2 class="ui left aligned aligned header manC_laranja">
                  Colaboradores
                </h2>
              </div>
              <div class="ui centered grid">
                <div class="two column row">
                  <div class="column">
                    <img class="ui medium circular image" src="../../../static/site2016/images/jander_manC.png">
                  </div>
                  <div class="column">
                    <h3 class="ui header manC_laranja">Prof. Dr. Jander Moreira</h3>
                    <div class="justificado">
                      Durante a realização do projeto contamos com a ajuda do Professor Doutor Jander Moreira para revisão das bibliotecas pesquisadas e disponibilizadas.
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
```

# Página principal de um cabeçalho

### Obtjetivos
A página princiapal de cada cabeçalho é um forma de o usuário poder ver e acessar cada função presente naquele cabeçalho. Além disso, ela pode servir como uma forma de consulta rápida já que os links para cada função contêm uma explicação curta sobre retorno e os parâmetros da função em questão.

### Código
O início da página seque a mesma estrutura das demais paǵinas citadas. 
``` html
{% extends 'site2016/base.html' %}
{% load static %}

{% block title %}
Math.h - Manual C
{% endblock title %}

{% block head_extensions %}

{% endblock head_extensions %}

{% block body %}
<div class="ui grid">
  <div class="sixteen wide column manC_title">
    <header class="ui inverted masthead center aligned segment" id="fundo_azul_titulo">
      <h1 class="ui inverted header">
        &ltmath.h&gt
      </h1>
    </header>
  </div>
</div>
<main role="main" class="main_manC">
  <section class="ui vertical stripe segment" id="fundo_cinza" role="region">
    <div class="ui stackable centered grid container">
      <div class="one wide column">
        {% block sidebar_content %} 
        {% include 'site2016/manualC/leftSidebar.html' %} 
        {% endblock %}
      </div>
```
Na sequêncida tem-se um descrição do cabeçalho que é composta por um título e um paragrafo. Depois da descrição inicia-se uma lista contendo os links para cada função daquele cabeçalho. Cada link é um item da lista, sendo eles compostos por uma tag `a`(link) que é um título terciário e duas descrições, uma sendo sobre o retorno da função e outra, sobre o que aquela função deve receber como parâmetro. Essa estrutura se repete para cada função.
Para exemplificar, utilizou-se os códigos da `math.h`.
``` html
<div class="twelve wide column">
        <div class="ui centered vertical padded segment">
          <h1 class="manC_laranja">Descrição:</h1>
          <p class="justificado">
            Na biblioteca <b class="manC_laranja_escuro">&ltmath.h&gt</b> estão
            contidas diversas funções matemáticas básicas, com ela podemos
            trabalhar com funções trigonométricas, funções para cálculo de raiz
            quadrada, valor absoluto, entre outras. Esta listagem apresenta as seguintes
            funções conforme definidas pelo padrão C99. A inclusão das funções da
            biblioteca matemática são feitas com a opção de compilação <b>-lm</b>. Vale
            lembrar que todas as funções dessa biblioteca retornam valores do
            tipo double. Veremos, a seguir, todas elas.
          </p>
        </div>
        <div class="ui large left aligned huge header manC_laranja">
          <h1>Funções:</h1>
        </div>
        <div class="ui very relaxed divided list">
          <div class="item">
            <div class="content">
              <a class="manC_laranja odd" href="{% url 'math_funcoes' %}#acos">
                <h3>double acos(double x)</h3>
              </a>
              <div class="description">
                RETORNA: o cosseno de um ângulo; isto é, um número entre -1 e 1,
                tal que -1&lt=cosseno&lt=1
              </div>
              <div class="description">
                RECEBE: o ângulo, em radianos, do cosseno que foi informado como
                parâmetro ou NaN se o argumento estiver fora do domínio de
                entrada.
              </div>
            </div>
          </div>
          <div class="item">
            <div class="content">
              <a
                class="manC_laranja_escuro"
                href="{% url 'math_funcoes' %}#asin"
              >
                <h3>double asin(double x)</h3>
              </a>
              <div class="description">
                RETORNA: o seno de um ângulo, tal que, -1 &lt= seno &lt= 1.
              </div>
              <div class="description">
                RECEBE: o ângulo, em radianos, cujo seno foi informado como
                parâmetro ou NaN se o argumento estiver fora do domínio de
                entrada.
              </div>
            </div>
          </div>
          <!-- Demais items da biblioteca -->
```
Por fim encerra-se a página com a segunda barra lateral, esta contem os links para cada função. Ela tem como objetivo ser mais uma forma rápida de navegação pelo site. Estando ela fixada, a mesma sempre estará na tela do usuário possibilitando que uma determinada função seja acessada com apenas um clique. A barra lateral em si segue a mesma arquitetura de código da primeira barra lateral.
```html
<div class="one wide column">
        {% block sidebar_content2 %} 
        {% include 'site2016/manualC/math/rightSidebar.html' %} 
        {% endblock %}
      </div>
    </div>
  </section>
</main>
```

# Página de funções

### Objetivos
A página de funções contem uma explicação mais detalhada sobre cada função, contendo exemplos de uso e saída esperada do terminal. Ela tem como objetivo, facilitar o entendimento e usi de uma determinada função.

### Código

O conteúdo desta página começa igual as demais.
```html
{% extends 'site2016/base.html' %}
{% load static %}

{% block title %}
Funções &ltmath.h&gt - Manual C
{% endblock title %}

{% block head_extensions %}

{% endblock head_extensions %}

{% block body %}
<div class="ui stackable centered grid">
	<div class="row">
		<div class="one wide left floated column">
			{% block sidebar_content %}
			{% include 'site2016/manualC/leftSidebar.html' %}
			{% endblock %}
		</div>
```
A porção `main` começa com as funções, antes de cada função vem um `a`(link) com uma id para a função respectiva, isso é linkado a barra lateral direita fazendo com que, ao clicar em um link de função, o usuário seja direcionado para a exata porção da página de funções que a função acessada está. Na sequência cada função conta com um título na formatação de título de página, dentro dos títulos há uma formatação com tag `b` que faz com que os tipo(double, int, char, etc) fiquem com uma formatação diferente do resto do nome da função. Foi feito dessa forma, pois o tipo não é de fato usado nas funções em código, mas eles estão presentes no título para ilustrar qual é o tipo de dado que é retornado e recebido pela função. Na sequência em forma de parágrafos vem a expecificação do que a função recebe e retorna.
```html
<main role="main">
				<a id="acos"></a>
				<header class="ui inverted masthead center aligned segment manC_header" id="fundo_azul_titulo" id="acos">
					<h1 class="ui inverted header">
						<!-- Tirei o id, para ficar lowercase -->
						<b class="fundo_azul_titulo_manC">double</b> acos(<b class="fundo_azul_titulo_manC">double</b> x)
					</h1>
				</header>
				<section class="ui vertical stripe segment" role="region">
					<div class="ui stackable centered grid container">
						<div class="twelve wide column">
							<p class="justificado"><b class="manC_laranja_escuro">Recebe:</b>
								o cosseno de um ângulo; isto é, um número entre -1 e 1 → -1<=cosseno<=1.</p>
									<p class="justificado"><b class="manC_laranja_escuro">Retorna:</b>
										o ângulo, em radianos, do cosseno que foi informado como parâmetro ou NaN se o argumento estiver
										fora do domínio de entrada.</p>
```
Na sequência tem-se os exemplos de código e a saída do terminal, ambos são formatados através de da ferramente `highlight.js`. Eles possuem uma estrutura onde se declara uma tag `<pre>` e dentro dela se coloca uma tag `code` com a classe da formatação desejada, dentro da tag `code` é disposto o código a ser exibido. Lembrando que o código deve vir com a indentação desejada, e não seguindo a identação do resto do arquivo, pois ele é exibido com a exata identação em que ele está presente no arquivo.
Essa estrutura se repete para cada função. Como exemplo de código foi utilizado uma função do cabeçalho `math.h` foi uti
```html
<div class="ui horizontal divider"><b class="manC_laranja_escuro">Exemplo de uso da função</b>:</div>
									<div class="ui container">
										<pre>
									<code class="c">
//EXEMPLO ACOS()

#include &ltstdio.h&gt									
#include &ltmath.h&gt
	
int main() {
	double cosseno;
	scanf("%lf", &cosseno);
	printf("o angulo cujo cosseno eh %.3lf, eh %.3lf aproximadamente", cosseno,
	<a href="/mathfuncoes/#asin" style="text-decoration: underline;">acos</a>(cosseno));
	return 0;
}		
									</code>
								</pre>
									</div>
									<div class="ui horizontal divider"><b class="manC_laranja_escuro">Saída do
											terminal</b>:</div>
									<div class="ui container">
										<pre>
									<code class="hljs console">
			>clang-7 -pthread -lm -o main main.c
			>./main
			0.5
			o angulo cujo consseno eh 0.500, eh 1.047 aproximadamente
									</code>
								</pre>
									</div>
						</div>
					</div>
```

# Links para mais informações:

- ##### Documentação Django: [Django](https://docs.djangoproject.com/pt-br/3.2/)

  - Django estrutura de blocos: [`blocks`](https://stackoverflow.com/questions/53383602/what-is-block-content-and-endblock-content-for-in-django)

  - Django estrutura de templates: [`templates`](https://docs.djangoproject.com/en/3.2/topics/templates/)

- ##### Documentação do framework CSS: [SemanticUI](https://semantic-ui.com/)
  - Mais informações sobre o funcionamento do grid: [`grid`](https://semantic-ui.com/collections/grid.html)

- ##### Formatação de exemplo de uso e saída de terminal: [highlight.js] (https://highlightjs.org/)