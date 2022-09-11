__`(vale para qualquer tipo de arquivo com qualquer extensão)`__

Para __inicializar__ o repositório
_`git init`_

Foi criada uma pastinha __`.git`__ (é ali que toda a mágica acontece)

 
para colocar __apenas__ o arquivo modificado na área de __`stagging`__
_`git add README.md`_


Cria uma __nova branch__ para o projeto e já entra nela com o checkout
_`git checkout -b "novo-botao"`_


Colocamos a nossa alteração em __`stagging`__ (vale para __branch principal__ também)
_`git add .`_


Commitamos com (vale para __branch principal__ também)
_`git commit -m "novo botão"`_


Para enviar na __branch principal__
_`git push origin main`_


Para enviar __fora da branch principal__ 
_`git push origin novo-botao`_ 
