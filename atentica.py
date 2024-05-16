import requests
import base64
import json
 
# URL da API
api_url = "https://gateway.apiserpro.serpro.gov.br/viodec-trial/v1/decode"

# Token de autenticação do ambiente Trial (substitua se necessário)
bearer_token = "bearer 06aef429-a981-3ec5-a1f8-71d38d86481e"

# Cabeçalho da requisição
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/octet-stream"
}

# Exemplo de conteúdo binário para decodificação (substitua pelos seus dados)
#data = b"/home/charles/SemanaTI/qrcode-trial.bin"

image = open('/home/charles/SemanaTI/qrcode-trial.bin', 'rb') #open binary file in read mode
image_read = image.read()
image_64_encode = base64.b64encode(image_read)





# Enviando a requisição POST
response = requests.post(api_url, headers=headers, data=image_read)

# Verificando o status da resposta
if response.status_code == 200:
    # Decodificando o JSON da resposta (se aplicável)
    try:
        decoded_data = json.loads(response.content)
        print(decoded_data)
    except json.JSONDecodeError:
        # O conteúdo da resposta pode não ser JSON
        print(response.content)
else:
    # Erro na requisição
    print(f"Erro na requisição: {response.status_code}")
    
  
print(response.content)


print(image)

print(response.content)
print(f"Erro na requisição: {response.status_code}")
    

