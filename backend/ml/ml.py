from ml.addons import get_message_tokens  # , txt2embeddings, search_results
from ml.SETTINGS import (
    SYSTEM_PROMPT_HR,
    SYSTEM_PROMPT_HR_WITH_TEMPLATE,
    BOT_TOKEN,
    LINEBREAK_TOKEN,
    PROMPT_HR_CONTEXT,
    PROMPT_HR_WITH_TEMPLATE_CONTEXT,
)  # , TABLE_NAME, DEVICE
from llama_cpp import Llama


def interact_hr(
    model: Llama,
    content: str,
    is_llama: bool,
    top_k: int = 30,
    top_p: float = 0.9,
    temperature: float = 0.6,
    repeat_penalty: float = 1.1,
):
    """
    Взаимодействие с моделью на основе LLAMA для генерации ответов на пользовательские запросы.

    Параметры:
    - model_path (str): Путь к предварительно обученной модели LLAMA.
    - user_prompt (str): Пользовательский запрос для генерации ответа.
    - n_ctx (int): Максимальная длина контекста.
    - top_k (int): Количество наиболее вероятных токенов для рассмотрения в генерации.
    - top_p (float): Порог отсечения для выбора токенов в генерации на основе вероятностей.
    - temperature (float): Параметр температуры для разнообразия в генерации.
    - repeat_penalty (float): Штраф за повторение токенов в генерации.

    Возвращает:
    str: Сгенерированный ответ на основе пользовательского запроса.

    Пример использования:
    ```python
    model_path = "path/to/model"
    user_prompt = "Привет, как дела?"
    response = interact(model_path, user_prompt)
    ```

    Подробности:
    - Функция использует модель LLAMA для генерации ответов на пользовательские запросы.
    - Задает параметры генерации, такие как ограничения токенов, температура и штраф за повторения.
    - Генерирует ответ на основе пользовательского запроса и возвращает его в виде строки.
    """

    sys_prompt = SYSTEM_PROMPT_HR
    user_message = PROMPT_HR_CONTEXT.format(content)

    system_message = {"role": "system", "content": sys_prompt}
    user_message = {"role": "user", "content": user_message}

    # Для Mistral
    tokens = []
    tokens.extend(get_message_tokens(model, **system_message))
    tokens.extend(get_message_tokens(model, **user_message))
    tokens.extend([model.token_bos(), BOT_TOKEN, LINEBREAK_TOKEN])
    token_str = ""

    # Для Llama 3
    messages = []
    messages.append(system_message)
    messages.append(user_message)
    if is_llama:
        for part in model.create_chat_completion(
            messages,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repeat_penalty=repeat_penalty,
            stream=True,
        ):
            delta = part["choices"][0]["delta"]
            if "content" in delta:
                token_str += delta["content"]
    else:
        generator = model.generate(
            tokens,
            top_k=top_k,
            top_p=top_p,
            temp=temperature,
            repeat_penalty=repeat_penalty,
        )

        # Преобразование токенов в строку
        for token in generator:
            token_str += model.detokenize([token]).decode("utf-8", errors="ignore")
            tokens.append(token)

            if token == model.token_eos():
                break

    return token_str


def interact_hr_with_template(
    model: Llama,
    request: str,
    content: str,
    is_llama: bool,
    top_k: int = 30,
    top_p: float = 0.9,
    temperature: float = 0.6,
    repeat_penalty: float = 1.1,
):
    """
    Взаимодействие с моделью на основе LLAMA для генерации ответов на пользовательские запросы.

    Параметры:
    - model_path (str): Путь к предварительно обученной модели LLAMA.
    - user_prompt (str): Пользовательский запрос для генерации ответа.
    - n_ctx (int): Максимальная длина контекста.
    - top_k (int): Количество наиболее вероятных токенов для рассмотрения в генерации.
    - top_p (float): Порог отсечения для выбора токенов в генерации на основе вероятностей.
    - temperature (float): Параметр температуры для разнообразия в генерации.
    - repeat_penalty (float): Штраф за повторение токенов в генерации.

    Возвращает:
    str: Сгенерированный ответ на основе пользовательского запроса.

    Пример использования:
    ```python
    model_path = "path/to/model"
    user_prompt = "Привет, как дела?"
    response = interact(model_path, user_prompt)
    ```

    Подробности:
    - Функция использует модель LLAMA для генерации ответов на пользовательские запросы.
    - Задает параметры генерации, такие как ограничения токенов, температура и штраф за повторения.
    - Генерирует ответ на основе пользовательского запроса и возвращает его в виде строки.
    """

    sys_prompt = SYSTEM_PROMPT_HR_WITH_TEMPLATE.format(request)
    user_message = PROMPT_HR_WITH_TEMPLATE_CONTEXT.format(content)

    system_message = {"role": "system", "content": sys_prompt}
    user_message = {"role": "user", "content": user_message}
    tokens = []
    tokens.extend(get_message_tokens(model, **system_message))
    tokens.extend(get_message_tokens(model, **user_message))
    tokens.extend([model.token_bos(), BOT_TOKEN, LINEBREAK_TOKEN])
    token_str = ""

    # Для Llama 3
    messages = []
    messages.append(system_message)
    messages.append(user_message)
    
    if is_llama:
        for part in model.create_chat_completion(
            messages,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repeat_penalty=repeat_penalty,
            stream=True,
        ):
            delta = part["choices"][0]["delta"]
            if "content" in delta:
                token_str += delta["content"]
    else:
        generator = model.generate(
            tokens,
            top_k=top_k,
            top_p=top_p,
            temp=temperature,
            repeat_penalty=repeat_penalty,
        )

        # Преобразование токенов в строку
        for token in generator:
            token_str += model.detokenize([token]).decode("utf-8", errors="ignore")
            tokens.append(token)

            if token == model.token_eos():
                break

    return token_str


# def request2similiars(question, tokenizer, model, client, limit=10):
#     embedding = txt2embeddings(question, tokenizer, model, DEVICE)
#     documents = search_results(client, TABLE_NAME, embedding[0], limit=limit)
#     context = "\n\n".join([document["text"] for document in documents])
#     return context
