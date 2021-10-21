from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey, você mesmo seu gay! ♦ {}

Bem vindo(a) ao {}

♦ Sou um bot que faz extrair imagens para textos ♦

E pelo fim, mais uma jornada de um boi apertando start neu 😑
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("♦ 𝕮𝖗𝖎𝖆𝖉𝖔𝖗 ♦", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx")],
        [InlineKeyboardButton(text="♦ Retornar ao inicial ♦", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("♦ 𝕮𝖗𝖎𝖆𝖉𝖔𝖗 ♦", url="https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx")
        ],
        [
            InlineKeyboardButton("Como me usar ❔", callback_data="help"),
            InlineKeyboardButton("🧐 Sobre eu é ❔🧐", callback_data="about")
        ],
        [InlineKeyboardButton("⚙️ Canal ⚙️", url="https://t.me/RabiscoS_MeuS_77")],
        [InlineKeyboardButton("⚙️ Grupo ⚙️", url="https://t.me/blazer808_Stay")],
    ]

    # Help Message
    HELP = """
Você realmente precisa de ajuda porra? 🧐

Basta enviar uma imagem... O resto eu que faço, beleza?

Nota : Então, seu gay... Pode enviar qualquer quantidade de imagens de uma só vez, e funcionará com a mesma velocidade de download e extração.

Tenha-se vergonha na cara, e faça certo infeliz🤬.
    """

    # About Message
    ABOUT = """
**Sobre eu é 🤔** 

Bot criado pelos Baianor's @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx ~ @PV_D0_M30_D3M0N12YNH0_P4ND4

Baianor : [Baianor](https://t.me/xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx)

Estrutura : [Pyrogram](docs.pyrogram.org)

Idioma : [Python](www.python.org)

Desenvolvedor : @xPV_D4_M34_S4Y0R1_D3M0N_CR4ZZYx
    """
