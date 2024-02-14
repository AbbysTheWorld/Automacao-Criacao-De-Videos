import openai
import requests
import wget
import random
from pathlib import Path
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip,AudioFileClip,concatenate_videoclips,ColorClip
from gtts import gTTS
from time import sleep

chave_api = '' #Sua Chave API ChatGpt
openai.api_key = chave_api

def chatResponse(script:str):
    prompt = f"""
        Pegue o seguinte conjunto de ideias: [{script}]
        Agora com base nele , crie uma historia para um video curto(shorts).

        Preferências: Faça uma historia criativo que mantenha as pessoas vridadas no vídeo querendo sempre saber oque vai vir,
        tenha em mente uma historía direta,é permitido utilizar nomes fícticios para os personagens,objetos e etc da historia.

        Características no roteiro: Mande o roteiro direto sem palavras como 'certo irei fazer o roteiro' ou coisas relacionadas,
        alem de fazer um roteiro direto sem partes como 'pular para uma cena' ou 'cena 1:' e 'Essa é a história direta que você pode usar para o seu vídeo curto, 
        sem a necessidade de edições adicionais.Espero que goste e que ela mantenha as pessoas vidradas querendo saber o que vai acontecer a seguir.'

        Irei usar essa historia direta no meu video curto,sem quaisque edição. E tambem não quero a conclusão no roteiro exemplo de
        conclusão que eu não quero no video: 'Essa é a história direta que você pode usar para o seu vídeo curto, 
        sem a necessidade de edições adicionais.Espero que goste e que ela mantenha as pessoas vidradas querendo saber o 
        que vai acontecer a seguir.'

        Um exemplo de como eu quero essa historia tendo em base as seguintes ideias: [Espaço,Astrounauta,Apocalispe].
        Obs:Isso foram apenas ideias!

        "Seja bem vindo a historia do astronauta João que sobreviveu á um apocalispe espacial! A historia começa quando Jõao
        um astrounauta,foi para mais um dia de trabalho na estação espacial kalina,ao chegar no trabalho João percebeu que tinha algo
        estranho acontecendo com os dispositivos do trabalho dele e no geral no mundo todo...
        "

        Esse foi um exemplo básico e incompleto e eu quero que com base no conjunto de ideias e com base na historia você faça uma historia direta.

        Informações Adicionais ao script: A historia tem que ser bem explicada e ao mesmo tempo uma historia curta para que os
        telespectadores consigam assistir sem perder a vontande, A sua resposta será enviada a uma api onde ela ira transformar o
        texto em voz,então na sua resposta fale somente da historia e nada mais.

        Remova as seguintes frases na historia(se tiver):'Essa e a história direta que você pode usar para o seu vídeo curto, sem a necessidade de edições adicionais
        Espero que goste e que ela mantenha as pessoas vidradas querendo saber o que vai acontecer a seguir'
    """

    roteiro = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role':'user','content':prompt}
        ]
    )

    roteiro = roteiro.choices[0].message.content
    
    prompt2 = f"""
        Pegue o seguinte a seguinte historia: [{roteiro}]

        Agora com base nessa historia crie prompts de imagens.

        Exemplo usando a seguinte historia: "Era uma vez joão,um menino que adorava muita a natureza e todos os dias
        sempre ia para o topo das montanhas com os amigos deles e observava os animais,arvores e rios. "

        [" Imagens natureza,Imagens de arvores,Imagens animais,Imagens de pessoas felizes "]

        Esse foi um exemplo básico e incompleto porem com base nessa historia enviada por min e nesse exemplo quero que você crie prompts de imagens.

        Quero que o modelo da resposta seja direta igual esse exemplo: ["Imagens linda de floresta,Imagens linda do oceano,Imagens do Barco do luffy] sem quaisque adição de palavras como
        'certo,irei gerar prompts' ou algo relacionado a isso.
    """

    ideias = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role':'user','content':prompt2}
        ]
    ) 

    ideias = ideias.choices[0].message.content
    ideias_lista = ideias.replace('"','').replace('[','').replace(']','').replace('.','')
    ideias_lista = ideias_lista.split(',')
    limpar_roteiro()
    escrever_roteiro(roteiro)

    return {'roteiro':roteiro,'ideias':ideias_lista}

def obter_videos_por_tema(tema, chave_api,quantidade):
    endpoint = "https://api.pexels.com/videos/search"
    
    parametros = {
        'query': tema,
        'per_page': quantidade 
    }
    
    headers = {
        'Authorization': chave_api
    }
    
    resposta = requests.get(endpoint, params=parametros, headers=headers)
    
    if resposta.status_code == 200:
        videos_json = resposta.json()['videos']
        urls_videos = []
        for video in videos_json:
            urls_videos.append(video['video_files'][0]['link'])

        return urls_videos
    else:
        print("Erro ao buscar vídeos:", resposta.text)
        return None

def baixar_videos(videos, pasta_destino):
        try:
            video = videos[random.randint(0,len(videos))]
        except:
            video = videos[random.randint(0,len(videos)) - 1]

        url = video
        try:
            for arquivo in Path('./videos').iterdir():
                if arquivo:
                    arquivo.unlink()

            print(f"Baixando vídeo...")
            wget.download(url, out=pasta_destino)
            print(" Vídeo baixado com sucesso!")
        except Exception as e:
            print(f"Erro ao baixar o vídeo 1: {e}")

        for i,arquivo in enumerate(Path('./videos').iterdir()):
            arquivo.rename(Path(f'./videos/{i}.mp4'))

def limpar_roteiro():
    with open('TextsAndAudio/roteiro.txt','w') as txt:
        txt.write('')

def escrever_roteiro(script:str):
    limpar_roteiro()
    test=[]
    tests1=[]
    with open('TextsAndAudio/roteiro.txt','a',encoding='Windows 1252') as txt:
        txt.write(script)
            
    with open('TextsAndAudio/roteiro.txt','r',encoding='Windows 1252') as arquivo:
        for linha in arquivo:
            if(linha == '\n'):
                pass
            else:
                test.append(linha)
    
    text_full = ''.join(test)

    with open('TextsAndAudio/roteiro.txt','w',encoding='Windows 1252') as arquivo:
        arquivo.write(text_full)

    with open('TextsAndAudio/roteiro.txt','r',encoding='Windows 1252') as arquivo:
        for text in arquivo:
            if '.' in text:
                tests1.append(text.replace('.','\n'))

    limpar_roteiro()
    with open('TextsAndAudio/roteiro.txt','a',encoding='Windows 1252') as arquivo:
        for text in tests1:
                arquivo.write(text)

def textToVoice(arquivo_roteiro,lang:str,outputName:str):

    with open(arquivo_roteiro, 'r', encoding='Windows 1252') as file:
        roteiro = file.read()

    speech = gTTS(text=roteiro,lang=lang,slow=False,tld='com.au')
    speech.save('TextsAndAudio/{}'.format(outputName+'.mp3'))
    print('Audio Salvo com sucesso')

def mesclar_audio(video_path, audio_path, pasta_destino):
    video_original = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    duracao_video,duracao_audio = int(video_original.duration) , int(audio.duration)
    num_repeticoes = int(duracao_audio / duracao_video) + 1
    videos_repetidos = [video_original] * num_repeticoes

    print('Repetição de Vídeo Inicializada')
    video_repetido = concatenate_videoclips(videos_repetidos)
    video_repetido.write_videofile(f"{pasta_destino}/video_repetido.mp4", codec='libx264', fps=video_original.fps,threads=2)
    print('Repetição de Vídeo Finalizada')

    sleep(2)
    
    print('Adição de Audio Inicializada')
    video_original_repetido = VideoFileClip(f"{pasta_destino}/video_repetido.mp4")
    video_com_audio = video_original_repetido.set_audio(audio)
    video_com_audio.write_videofile(f"{pasta_destino}/video_audio.mp4", codec='libx264', fps=video_original_repetido.fps,threads=2)
    print('Adição de Audio Finalizada')
