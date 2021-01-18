<h1 align="center">Desafio Digistarts </h1>
<h3 align="center">Web Service REST</h3>



<h2 align="center">Como Usar</h2>
<div style="border-style: double ; margin-bottom: 100px;">

<h5>Limite:</h5>
<p>O primeiro valor passado tem que ser o limite por verbo <em>POST</em> <code>http://127.0.0.1:5000/limit/<></code>por endpoint.
<br>
Exemplo <code>http://127.0.0.1:5000/limit/<5></code> será definido o valor de até 5 números aceitos
</p>
<p>
Esse valor será o valor de limite quando a quantidade de número alcançar o limite ira retornar uma lista com os valores únicos e
ordenados em ordem crescente
</p>
<b>1<=N<=1000</b>

<h5>Enviando:</h5>
<p> Os valores são passados via JSON <code>{"number":valor}</code> o valor precisa ser do tipo inteiro na url <code>http://127.0.0.1:5000/</code>
com o verbo <em>POST</em>
</p>
<p>
Você também pode consultar todos os valores que foram passados com o verbo <em>GET</em> na url <code>http://127.0.0.1:5000/</code>.
<br>retornará lista JSON com os valores dentro
<br>Exemplo:
<br>
<code>
[
    <br>&nbsp&nbsp{"number"}:5,&nbsp{"number"}:7 <br>
]
</code>

</p>
<b>-1000<=K<=1000</b>


<h5>Modificando:</h5>
<p>
Os valores podem ser modificados com o verbo <em>PUT</em> na url <code>http://127.0.0.1:5000/id/<></code> você deverá informa o <b>id</b> de que deseja modificar no endpoint. <br>
Enviar um JSON <code>{"number":valor}</code> com o valor que deseja colocar no lugar.   <br>
Se nenhuma <b>id</b> for encontrada será criada uma JSON com o valor no <b>id</b> passado
</p>

<h5>Deletando:</h5>
<p>
Os valores podem ser deletados com o verbo <em>DELET</em> na url <code>http://127.0.0.1:5000/id/<></code> você deverá informa o <b>id</b> de que deseja deletar no endpoint. <br>
</p>

<h5>Filtrando:</h5>
<p>
Você também pode filtrar a pesquisa pegando apenas o valor do <b>id</b> desejado através do da url <code>http://127.0.0.1:5000/id/<></code>
</p>
</div>
<h2 align="center">Erros</h2>
<div style="margin-bottom: 100px;" >
<p>
Para automatização todos os erros terão a chave <i>message</i> com o erro informado no valor do JSON
</p>
<ul>

<li>
Tentando inserir/modificar/deletar um valor antes de definir o valor de limite: codigo de status 400 <b>BAD REQUEST</b>
</li>
<li>
Tentando acessar uma <b>id</b> não valida: codigo de status 404 <b>NOT REQUEST</b>
</li>
</ul>
</div>


<h2 align="center">Informações</h2>
<ul>
<li style="margin:10px">
    Tive que fazer bastante uso da função (Global) mesmo sabendo que não é uma boa prática, pois não havia banco de dados para pegar id ou salvar os numeros
</li>
<li style="margin:10px">
    Foram rodados testes no Postman
</li>
<li style="margin:10px">
    Usei a biblioteca flask-restfull pois o flask puro não lida muito bem com os verbos PUT e DELETE
</li>
<li style="margin:10px">
    Não tive muito tempo para escrever mais testes
</li>
</ul>

