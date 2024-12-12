import requests

def get_user_avatar(user_id, token):
    url = f"https://discord.com/api/v10/users/{user_id}"
    
    headers = {
        "Authorization": f"Bot {token}",  # Use "Bot {token}" para um bot ou "Bearer {token}" para OAuth2
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        avatar_hash = user_data.get('avatar')
        
        if avatar_hash:
            avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png"
            return avatar_url
        else:
            return "User has no avatar"
    else:
        return f"Error: {response.status_code}"

# Exemplo de uso:
user_id = '1049052714966978682'  # Substitua pelo ID do usuário do Discord
token = 'MTMwMzcyODMyOTY4OTM5OTI5Nw.GS5TJb.8yExgyd0nBzm6fB1RBDd2JzGryMI8c_f8ObZX0'  # Substitua pelo token do bot

avatar_url = get_user_avatar(user_id, token)
print("Avatar URL:", avatar_url)
