# git clone: Copiando um repositório existente

Para pegar o link, vá até o repositório remoto desejado e na parte à direita clique no botão **clone or download**, como mostrado na imagem abaixo.

![clone or download](img/p0003-0.png)

Vá até o diretório na sua máquina em que você deseja colocar o repositório e digite no terminal:

```
$ git clone <url_do_repositorio_que_deseja_copiar>
```

- **$** indica que você deve usar o **usuário comum** para fazer essa operação.
- digite a url do repositório sem os sinais **< >**.

Caso deseje copiar, além do branch padrão, algum outro branch do repositório, digite:

```
$ git fetch origin <nome_do_branch_remoto>:<nome_que_deseja_dar_para_o_branch_local>
```


tags: git, clone, fetch, repositório
