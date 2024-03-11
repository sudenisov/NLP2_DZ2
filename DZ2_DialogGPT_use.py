from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr
import torch

title = "DZ2 DialogGPT"
description = "DialogGPT"
examples = [["Hello?"]]

class DialogGPTWrapper:
    def __init__(self, model_path="./DZ2model/DialogGPT_2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def predict(self, input, history=[]):
        # токенизировать новое предложение пользователя
        new_user_input_ids = self.tokenizer.encode(
            input + self.tokenizer.eos_token, return_tensors="pt"
        )

        # добавляю токены нового ввода пользователя в историю чата
        bot_input_ids = torch.cat([torch.LongTensor(history), new_user_input_ids], dim=-1)

        # генерирую ответы
        history = self.model.generate(
            bot_input_ids, max_length=4000, pad_token_id=self.tokenizer.eos_token_id
        ).tolist()

        # преобразовываю токены в текст, а затем разделяю ответы на строки
        response = self.tokenizer.decode(history[0]).split("<|endoftext|>")
        # преобразовываю в кортежи из списка
        response = [(response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)]
        return response, history

# Создаем экземпляр класса
dialog_gpt_wrapper = DialogGPTWrapper()

# Запускаем Gradio интерфейс
gr.Interface(
    fn=dialog_gpt_wrapper.predict,
    title=title,
    description=description,
    examples=examples,
    inputs=["text", "state"],
    outputs=["chatbot", "state"],
    theme="finlaymacklon/boxy_violet",
).launch()
