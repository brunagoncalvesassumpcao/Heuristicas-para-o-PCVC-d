Este é um trabalho de iniciação científica desenvolvido por Bruna Gonçalves Assumpção, sobre as ordens do orientador
Silvio Alexandre de Araujo, entre outubro de 2025 e outubro de 2026 na instituição UNESP - Ibilce. O presente
trabalho foi realizado com apoio da Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP), Brasil.
Processo n° 2025/09548-6. As opiniões, hipóteses e conclusões ou recomendações expressas neste material são
de responsabilidade do(s) autor(es) e não necessariamente refletem a visão da FAPESP.
---------------------------------------------------------------------------------------------------------------

Este trabalho consistiu em desenvolver duas heurísticas construtivas que resolvem o PCVC-d, baseadas em adaptações
das famosas heurísticas do vizinho mais próximo e de inserção, que resolvem o PCV.

Além disso, implementamos meta-heurísticas baseadas em VND e ILS para melhorar os reultados obtidos a partir das
heurísticas construtivas.

Para testar os métodos desenvolvidos, utilizamos instâncias da TSPlib.

Os resultados estão dispostos em três tabelas: "Resultados_heurísticas_construtivas", "Resultados_VND" e "Resultados_ILS".

A seguir, descrevemos o funcionamento e integração dos arquivos deste repositório:


"nn_d_relaxado" e "insercao_d_relaxada" resolvem o PCVC-d a partir de adaptações de heurísticas construtivas.


"rodar_nn" e "rodar_insercao" utilizam de "funcoes_auxiliares" para ler os parâmetros da pasta "Instâncias" e aplicar as funções "nn_d_relaxado" e "insercao_d_relaxada" 
sobre eles, os resultados são, respectivamente, inseridos nas pastas "Resultados_nn" e "Resultados_insercao".


"vnd_funcao" e "ils_funcao" melhoram soluções iniciais. Diferente de "nn_d_relaxado" e "insercao_d_relaxada", que precisam dos parâmetros: matriz, d e P,
"vnd_funcao" e "ils_funcao" precisam de caminho inicial, matriz, d e P.

"juntar_arquivos" junta as informações de "Instâncias" e "Resultados_insercao" no arquivo "info_insercao", e junta os arquivos de "Instancias" e "Resultados_nn" no 
arquivo "info_nn". "info_insercao" e "info_nn" servem como parâmetros pra "vnd_funcao" e "ils_funcao"


"rodar_vnd" e "rodar_ils" utilizam de "funcoes_auxiliares" para ler os parâmetros das pastas "info_nn" e "info_insercao" e aplicar nestes as funções "vnd_funcao" e 
"ils_funcao". Os resultados são colocados em "ResultadosILS_nn", "ResultadosILS_insercao", "ResultadosVND_nn" e "ResultadosVND_insercao".

"cria_tabelas" da origem a "Resultados_heurísticas_construtivas" usando as informações de "Resultados_insercao" e "Resultados_nn". Da origem a "Resultados_ILS" usando
as informações de "ResultadosILS_nn" e "ResultadosILS_insercao". Da origem a "Resultados_VND usando as informações de "ResultadosVND_nn" e "ResultadosVND_insercao".



("verificar_factibilidade" foi usado na costrução das funções "vnd_funcao", "ils_funcao", "nn_d_relaxado" e "insercao_d_relaxado", pra verificar erros)




































