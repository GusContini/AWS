import requests
import json

def test_message_classification(message, categories):
    # URL da sua API Gateway
    api_url = "https://iqzolzrrni.execute-api.us-east-1.amazonaws.com/dev/message-classification"

    # Prepare a payload para a requisição POST
    payload = {
        "message": message,
        "categories": categories
    }
    
    # Faça a requisição POST
    response = requests.post(api_url, json=payload)

    # Verifique o código de status da resposta
    if response.status_code == 200:
        print("Classificação de mensagem realizada com sucesso!")
        result = response.json()
        print("Resposta da API:", result)
        
        # Extraia o conteúdo da resposta (opcional)
        message_content = result.get('body')  
        print("Conteúdo da mensagem:", message_content)

    else:
        print("Erro na classificação de mensagem:", response.status_code)
        print("Resposta da API:", response.text)  # Imprima a resposta da API em caso de erro

if __name__ == "__main__":
    # Exemplo de uso
    test_message = "Joe Biden and Donald Trump are candidates to the most import office of the world"
    test_categories = ["Esporte", "Política", "Tecnologia"]

    test_message_classification(test_message, test_categories)
