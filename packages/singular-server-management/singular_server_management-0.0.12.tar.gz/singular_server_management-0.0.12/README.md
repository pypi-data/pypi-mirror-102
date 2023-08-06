# SINGULAR SERVER MANAGEMENT #

# CONFIGURAÇÃO INICIAL DO SERVIDOR

_INGORE ESTE PONTO CASO SEJA UM SERVIDOR JÁ EM USO_
Instale o python, postgres, libs de relatórios e o nginx:

`sudo apt-get install git postgresql postgresql-contrib nginx curl libpq-dev build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
`

Garanta que o arquivo de dependências esteja 100% atualizado (`requirements.txt`) e já adicione o `gunicorn`, mesmo que não seja usado em desenvolvimento.

#VISÃO GERAL
Há disponível os seguintes comandos:

`update_project project_name host user git_user_password --server_password senha --key_file caminho_da_chave --websocket --cronjob`

`build_project project_name host port user  git_user_password --server_password senha --key_file caminho_da_chave --websocket --cronjob`

#WEBHOOKS
Há a possibilidade de vincular um webhook de push no bitbucket, apontando para a url `/webhooks/push_request` e incluindo os urlpatterns do arquivo routes.py no urlpatterns do projeto `[*routes.urlpatterns]` 

# Configurações
Adicione as seguintes variáveis no arquivo de configurações (`settings.py`)

`ADMINS = [(nome,email),]`

`DEFAULT_FROM_EMAIL = EMAIL`

`SERVER_SETTINGS = {
    'PROJECT_NAME': config('PROJECT_NAME'),
    'HOST': config('SERVER_HOST'),
    'USER': config('SERVER_USER'),
    'GIT_PASSWORD': config('GIT_PASSWORD'),
    'KEY_FILE': config('KEY_FILE'),
}
`