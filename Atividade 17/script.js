// 1. Carrega os projetos assim que a página abre
document.addEventListener("DOMContentLoaded", () => {
    atualizarDatalist();
});

// Função que lê o localStorage e renderiza as opções na tela
function atualizarDatalist() {
    const datalist = document.getElementById('projetosExistentes');
    
    // Pega os projetos salvos no navegador, ou cria uma lista inicial se estiver vazio
    let projetos = JSON.parse(localStorage.getItem('meusProjetos')) || ["Projeto Alpha", "Projeto Beta"];
    
    // Limpa a lista atual para não duplicar
    datalist.innerHTML = "";
    
    // Adiciona cada projeto como uma <option> dentro da <datalist>
    projetos.forEach(projeto => {
        const option = document.createElement('option');
        option.value = projeto;
        datalist.appendChild(option);
    });
}

// Função chamada ao clicar no botão "Avançar"
function gerenciarProjeto() {
    const input = document.getElementById('numeroInput');
    const valorDigitado = input.value.trim();

    if (valorDigitado === "") {
        alert("Por favor, selecione ou digite o nome de um projeto.");
        return;
    }

    // Pega a lista atual do localStorage
    let projetos = JSON.parse(localStorage.getItem('meusProjetos'));

    // Se o projeto digitado NÃO existir na lista, adiciona ele!
    if (!projetos.includes(valorDigitado)) {
        projetos.push(valorDigitado); // Adiciona na lista
        localStorage.setItem('meusProjetos', JSON.stringify(projetos)); // Salva no navegador
        alert(`Novo projeto "${valorDigitado}" criado com sucesso!`);
    } else {
        alert(`Entrando no projeto existente: "${valorDigitado}"`);
    }

    // Atualiza a lista visualmente antes de mudar de página
    atualizarDatalist();

    // Limpa o input e avança para a próxima página
    input.value = "";
    window.location.href = "2ndPagina.html";
}