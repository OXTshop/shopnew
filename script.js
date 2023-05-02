function buscarProdutos() {
    var input = document.getElementById('inputPesquisa');
    var filter = input.value.toUpperCase();
    var ul = document.getElementById('listaProdutos');
    var li = ul.getElementsByTagName('li');

    // Loop através dos itens da lista de produtos
    for (var i = 0; i < li.length; i++) {
        var h3 = li[i].getElementsByTagName('h3')[0];
        var txtValue = h3.textContent || h3.innerText;

        // Se o valor de pesquisa estiver presente no nome do produto, exibe o item, caso contrário, oculta
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = '';
        } else {
            li[i].style.display = 'none';
        }
    }
}
