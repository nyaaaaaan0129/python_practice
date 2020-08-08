bot_dict = {'こんにちは': 'コンニチハ'}
command = 'おはよう'
response = ''
for key in bot_dict:
    if key in command:
        response = bot_dict[key]
        break
if not response:
    response = '何ヲ言ッテルカ、ワカラナイ'