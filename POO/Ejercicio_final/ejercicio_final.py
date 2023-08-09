import openai

openai.api_key = "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"
system_rol = """Haz de cuenta que eres un analizador de sentimientos
Yo te paso sentimientos y tu analizas el sentimiento de los mensajes y me das una respuesta con al menos un caracter y como máximo 4 caracteres, SOLO RESPUESTAS NUMÉRICAS, donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
Puedes ir entre esos rangos, es decir 0.3, -0.5 etc. Tambien son validos.
(Puedes responder solo con ints o floats)"""

message = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.7 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37" #esta linea es para darle un color al texto
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;33m" + "Algo Negativo" + "\x1b[0;37"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33" + "Neutral" + "\x1b[0;37"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32" + "Algo positivo" + "\x1b[0;37"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32" + "Positivo" + "\x1b[0;37"
        elif polaridad > 0.9:
            return "\x1b[1;32" + "Muy Positivo" + "\x1b[0;37"
        else:
            return "\x1b[1;31" + "Muy Negativo" + "\x1b[0;37"

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDime Algo: " + "\x1b[0;37")
    message.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message,
        max_tokens = 8
    )
    respuesta = completion.choices[0].message["content"]
    message.append({"role": "assistant", "content": respuesta})
    
    sentiminto = analizador.analizar_sentimiento(float(respuesta))
    print(sentiminto)