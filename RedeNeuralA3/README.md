<h1><strong> 🎞 Rede Neural - Avaliação de Filmes</strong></h1>

<p>Esse é um projeto de uma rede neural criada e treinada para realizar a 
tarefa classificação de filmes em "bom" ou "ruim".</p>

<h2>Entendendo a lógica de uma Rede Neural</h2>
<p><Strong>Rede neural</Strong> é um método de inteligência artificial que ensina computadores a processar dados de forma semelhante ao cérebro 
humano. É um tipo de processo de machine learning, que usa <strong>nós ou neurônios</strong> interconectados em uma estrutura em camadas, semelhante ao cérebro humano.
Uma rede neural artificial (ou RNA) é composta por vários neurônios, cujo funcionamento é bastante simples. Geralmente, os neurônios são conectadas por canais de comunicação 
que estão associados a determinado <strong>peso</strong>. As unidades fazem operações apenas sobre seus dados locais, que são entradas recebidas pelas suas conexões.</p>

<p>As arquiteturas neurais são tipicamente organizadas entre <strong>camadas</strong>, e cada camada está conectada com a camada anterior:</p>
<ul>
    <li>Camada de Entrada: onde os padrões são apresentados à rede;</li>
    <li>Camadas Intermediárias ou Ocultas: onde é feita a maior parte do processamento, através das conexões ponderadas; podem ser consideradas como extratoras de características;</li>
    <li>Camada de Saída: onde o resultado final é concluído e apresentado.</li>
</ul>

<h2><strong>Explicando a Rede Neural do código</strong></h2>

<p>A rede neural presente neste projeto tem o intúito único de avaliar filmes através de notas. Durante o processamento, a rede neural determinará a qualidade de um filme 
    em "bom" ou "ruim", sendo "bom" uma nota final acima de 7 e "ruim" uma nota final abaixo de 7.</p>

<p>Como dito anteriormente, RNAs (rede neural artificial) possuem uma característica distinta em sua arquitetura. Sua disposição se da em forma de camadas de processamento. No código, fizemos o uso 
de 3 camadas:</p>
<ul>
    <li>A primeira camada 'layers.Input(shape=(1,))' é a camada de entrada. Ela espera um vetor de entrada de tamanho 1.</li>
    <li>A segunda camada 'layers.Dense(4, activation='relu')' é a camada oculta da rede neural. Ela possui 4 neurônios e utiliza a função de ativação ReLU.</li>
    <li>A terceira e última camada 'layers.Dense(1, activation='sigmoid')' é a camada de saída da rede neural. Ela possui 1 neurônio e utiliza a função de ativação sigmóide.</li>
</ul>

<p>Durante toda a fase inicial de preparação da rede, cada neurônio é responsável por ajustar seus pesos através de cálculos matemáticos. Ao realizar essa etapa, a rede garante maior acurácia e estabilidade durante o treinamento 
de dados, pois todos os neurônios estarão calibrados e prontos para a chegadas dos dados de validação.</p>

<p>Todo o cálculo executado nos neurônios presentes nas camadas envolve puramente <strong>álgebra linear</strong>, eles fazem operações de multiplicações de pesos pelas entradas e viés.
Por exemplo, nas camadas layers.Dense (intermediária e de saída), cada neurônio está conectado aos neurônios da camada anterior através de um conjunto de pesos, formando uma matriz.
Durante a forwardpropagation e na backpropagation, operação de multiplicação de matrizes e vetores são feitas para calcular as saídas de rede e ajustar os pesos dos neurônios.
Todos os calculos de matrizes e vetores são necessários para preparar os neurônios para o treinamento com os dados de teste, para evitar perdas deeficiência e possíveis erros.</p>

<p>Após, é realizado o treinamento do modelo da rede neural. Ali, a rede ajusta todos os pesos nas camadas através do algoritmo de descida de gradiente, que é feito com cálculos de derivadas e operações 
de algebra linear. Nesta etapa, os dados recebidos se dividem em dados de treinamento e dados de validação. Os dados de treinamento são aplicados primeiro para calibrar os pesos para os dados de teste, é nesse ponto que a rede neural 
irá se preparar e aprender a processar os tipos de dados que serão enviados futuramente. Em adição, temos os dados de validação, que são enviados a rede logo após os dados de treinamento para ajudar a garantir a assertividade das respostas retornadas.</p>

<p>Por fim, a rede faz previsões com novos dados recebidos, realizando as mesmas operações de álgebra linear para calcular as ativações das camadas. E finalmente, tem o resultado final de cada avaliação de filme.</p>

<h2><strong>Ajuste de pesos da camada intermediária</strong></h2>

<p>Durante a etapa de processamento da camada intermediária, cada neurônio realiza combinações dos pesos através de uma multiplicação de matriz (pesos) por vetor (entradas). 
    Na camada intermediária/oculta com ativação ReLU '(layers.Dense(4, activation='relu'))', a multiplicação de matriz e vetor funciona dessa forma:</p>
<ol>
    <li>vamos supor que a entrada seja um vetor de tamanho 1 (layers.Input(shape=(1,)))</li>
    <li>a camada oculta possui 4 neurônios, cada um com seu conjunto de pesos e um viés associado</li>
    <li>os pesos de uma camada densa são representados como uma matriz, onde cada linha representa os pesos de um neurônio</li>
    <li>se tivermos uma entrada de dimensão (1,) e 4 neurônios na camada oculta, teremos uma matriz de pesos com dimensão (1, 4)</li>
    <li>a forwardpropagation, a entrada é multiplicada pelos pesos dessa camada e, em seguida, somados os viéses</li>
</ol>
<p>Essa operação é uma multiplicação de matriz por vetor, onde o vetor de entrada é multiplicado pela matriz da camada densa.</p>

<p>Quando a rede neural inicia, os viéses, assim como os pesos, são inicializados com valores aleatórios pequenos. 
Ao longo do treinamento, assim como os pesos, os viéses são ajustados iterativamente pelo algoritmo de otimização para 
minimizar a diferença entre as previsões do modelo e as labels verdadeiras dos dados de treinamento.
O <strong>viés</strong> é necessário para melhorar a capacidade da rede neural de aprender e generalizar a partir dos dados, 
permitindo um ajuste mais flexível da função de ativação e dos limites de decisão, e seu valor é ajustado durante o treinamento da rede.</p>

<p>Se fossemos fazer a estrutura de cálculo na mão, ficaria da seguinte forma:</p>
<ul>
    <li>entrada = np.array([2])- os dados de entrada</li>
    <li>pesos_camada_oculta = np.random.rand(1, 4) - o peso da camada oculta com 4 neurônios</li>
    <li>vieses_camada_oculta = np.random.rand(4) - viés da camada oculta, um para cada neurônio</li>
</ul>
<p>Neste ponto, "entrada" é um vetor de dimensão 1. O "pesos_camada_oculta" representa os pesos da camada oculta, e "vieses_camada_oculta" são os vieses associados a cada neurônio.</p>

<p>O calculo de matriz por vetor (entrada pelo peso) + o viés é aprensentado com a seguinte estrutura:</p>
<ol>
    <li>saida_camada_oculta = np.dot(entrada, pesos_camada_oculta) + vieses_camada_oculta - multiplicação de matriz por vetor (entrada pelos pesos) e adição dos vieses</li>
    <li>saida_camada_oculta_relu = np.maximum(0, saida_camada_oculta) - aplicação da função de ativação ReLU</li>
    <li>print("Saída da camada oculta (ReLU):", saida_camada_oculta_relu)</li>
</ol>
<p>Nessa estrutura, utilizo o numpy para facilitar nos cálculos. A função np.dot() é utilizada para realizar 
a multiplicação de matriz por vetor, e a função np.maximum() é utilizada para aplicar a função de ativação ReLU aos resultados da multiplicação.</p>


<h2>Ativação ReLU</h2>

<p>Quando definimos as camadas, nos adicionados um parâmetro adicional para aprimorar ainda mais a eficiência da rede.
A função de ativação ReLU (Rectified Linear Unit) é uma função usada especialmente em camadas intermediárias (camadas ocultas). 
Ela é simples, mas extremamente eficaz e resolve alguns problemas das funções de ativação mais antigas, como a função sigmoide (que também ta sendo usada no código).</p>

<p>A função ReLU se da pela função:<p></p>
<ul>
    <li>F(x)=max(0,x)</li>
</ul>
<p>Ou seja, para qualquer valor de entrada X, a função ReLU retorna X se X for maior que 0. Em síntese, ela "zera" todos 
os valores negativos e mantém os valores positivos como estão. Nessa rede neural, o X na função ReLU é 
definido pelo resultado da multiplicação da matriz pelo vetor e a adição do viés.</p>
