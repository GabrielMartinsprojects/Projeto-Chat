# Titulo Hashzap
# Botao iniciar chat
#     popup janela na frente da tela
#     titulo bem vindo ao Haszap
#     Campo de texto , Escreva seu nome no chat
#     Botao : entrar no chat
        # sumir vom o titulo hashzap
        # fecha a janela
        # carregar o chat
        #     carregar as mensagens ja enviadas
        #     campo: digite suas mensagens
        #     botao de enviar
# importa o flet
import flet as ft
def main(pagina):
        def enviar_msg_tunel(mensagem):
                texto_chat = ft.Text(mensagem)
                chat.controls.append(texto_chat)
                pagina.update()

        pagina.pubsub.subscribe(enviar_msg_tunel)

        titulo = ft.Text("Chat criado por Gabriel Martins.")

        def entrar_chat(evento):
                janela.open = False
                pagina.remove(titulo)
                pagina.remove(botao_iniciar)
                pagina.add(chat)
                pagina.add(linha_mensagem)
                nome_user = campo_nome_usuario.value
                if nome_user == "Gabriel":
                        mensagem = "Meu irmãozinho entrou no chat"
                elif nome_user == "Millena":
                        mensagem = "ALERTA! ALERTA! Sensor de gatinha gótica detectou que Millena entrou no chat"
                elif nome_user == "Gustavo":
                        mensagem = "O melhor primo do mundo entrou no chat"
                elif nome_user == "ADM":
                        mensagem = "Cuidado palhaço, O ADM tá na área"
                elif nome_user == "Zion":
                        mensagem = "O hombre mais lindo entrou no chat"
                elif nome_user == "Natal":
                        mensagem = "Jimin entrou no chat?! Ah não... é Natal"
                elif nome_user == "Elisa" or "Lisa":
                        mensagem = "A fror Lisoca entrou no site familia. xey d´agua"
                elif nome_user == "Thiago" or "Chip":
                        mensagem = "O maior player de Escuras almas que conheço entrou no chat. Senhor Thiago"
                elif nome_user == "Diane":
                        mensagem = "Diane, A gloriosa, entrou no chat"
                elif nome_user == "Mirella":
                        mensagem = "Meireles tá aqui, eae Meirelles."
                elif nome_user == "Renalão" or "Renaly" or "Renali" or "Renally":
                        mensagem = "A bixa mais trans entrou no chat, Renalão"
                elif nome_user == "Sanji":
                        mensagem = "Poisé... o tenebroso Sanji entrou no chat"
                elif nome_user == "Arthur":
                        mensagem = "Qual dos dois ArthurS seria você?"
                elif nome_user == "Arthur Fabiano":
                        mensagem = "Tutu entrou no chat boy"
                elif nome_user == "Arthur Antunes":
                        mensagem == "Eae meu filosofo?"
                elif nome_user == "Gabru":
                        mensagem == "Gabru? Ah mlq ;>"
                elif nome_user == "Laura" or "Laurinha":
                        mensagem = "Oi laurinhazinha"
                elif nome_user == "JoJo" or "jojo" or "Jojo" or "JoJo Bizare Adventure" or "JBA":
                        mensagem = "Melhor anime de todos entrou no chat?"
                elif nome_user == "Naruto" or "naruto":
                        "Esse é o Anime favorito da minha namorada"
                else : mensagem = ft.Text(f"{nome_user}: entrou no chat, Diga OI ;)")
                pagina.pubsub.send_all(mensagem)
                pagina.update()
        def iniciar_chat(evento):
                pagina.dialog = janela
                janela.open = True
                pagina.update()
        botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
        chat = ft.Column()
        campo_nome_usuario = ft.TextField(label="Escreva o nome que será visualizado no chat")
        def enviar_msg(evento):
                texto_msg = campo_mensagem.value
                nome_user = campo_nome_usuario.value
                mensagem = f"{nome_user}: {texto_msg}"
                pagina.pubsub.send_all(mensagem)

                campo_mensagem.value = ""
                pagina.update() 
        campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_msg)
        
        botao_enviar_msg = ft.ElevatedButton("Enviar", on_click=enviar_msg)
        linha_mensagem = ft.Row([campo_mensagem , botao_enviar_msg])
        titulo_janela = ft.Text("Bem vindo ao GabrielZap")

        
        botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
        janela = ft.AlertDialog(
                title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])
#     criar todas as funções
        # cria elemento e colocar na pagina
        pagina.add(titulo)
        pagina.add(botao_iniciar)
        pagina.update()
ft.app(main, view=ft.WEB_BROWSER)
# rodar o app