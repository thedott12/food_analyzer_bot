import openai
import aiohttp
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

PROMPT_TEMPLATE = """
Определи по фотографии и описанию КБЖУ (калории, белки, жиры, углеводы), примерный вес и состав блюда или продукта. 
Также оцени, относится ли еда к категории "здоровой" (укажи "Да" или "Нет" и кратко поясни причину). 
Выведи результат в следующем формате:

Калории: ХХХ ккал  
Белки: ХХ г  
Жиры: ХХ г  
Углеводы: ХХ г  
Вес: ХХ г  
Состав: (список ингредиентов)
Здоровое питание: Да/Нет (пояснение)
"""

async def analyze_food(image_url: str, description: str = "") -> str:
    user_content = PROMPT_TEMPLATE
    if description:
        user_content += f"\nОписание от пользователя: {description}"

    response = await openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "Ты — эксперт по питанию. Отвечай строго по фактам."},
            {"role": "user", "content": [
                {"type": "text", "text": user_content},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]}
        ],
        max_tokens=512,
        temperature=0.2,
    )
    return response.choices[0].message.content
