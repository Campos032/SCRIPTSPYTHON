# Para criar um novo versionamento passar o comando git init
# git add . # Prepara as alterações para commitar
# git commit -m "primeiro commit" # Irá adicionar as alterações intitulando o commit com o nome que você passar nas ""
# git status # Retorna no terminal os status das alterações atuais
# git add Git_GitHub.py # Irá commitar apenas o arquivo que você deseja, intitulando-os commits diferentemente
# git log # Visualizar histórico de commits
# git diff # Mostra as alterações do atual arquivo em relação ao antigo commit
# git restore Git_GitHub.py # Descarta todas as alterações no arquivo atual
# Criando e Mesclando Branches(outras ramificações)
# git branch # Nos mostra em qual branch estamos
# git checkout master # Está movendo para uma nova branch, master é o nome da brach que você deseja ir ou criar
# git checkout -b nome_da_minha_branch # Está movendo para uma nova branch, levando todas as alterações da branch atual
# git merge nome_da_minha_branch  # Dentro da sua branch master, você passa esse comando para mesclar as alterações da
    # sua outra branch a sua branch master, ou a outra branch que você tenha
# Repositórios Remotos(Repository Remotes) Ex:GitHub, GitLab e etc.
# Dentro do GitHub criar um novo projeto(repository)
# git remote add origin https://github.com/Campos032/desktop-tutorial # Adiciona um nomo repository remote, o apelidando
    # como origin, então para você utilizar os comando acima você deverá sempre se referir ao remote repository origin
    # Por exemplo, você pode usar git pull origin master para puxar as alterações do ramo "master" do repositório remoto
    # chamado "origin",
# git push origin nome_da_minha_branch # Fazendo isso, a nossa branch será adicionada ao repository remote
# git pull origin nome_da_minha_branch # Fazendo isso você irá pegar as alterações do repository remote para o seu pc
# git fetch # Atualiza o local com o repository remote