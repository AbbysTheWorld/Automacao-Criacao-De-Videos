import random
from backend.scripts import chatResponse,obter_videos_por_tema,baixar_videos,textToVoice,mesclar_audio
from pathlib import Path

def fazer_video(ideias:str):
    print('Processo Inicializado')

    print('Pegando Roteiro')
    resposta_chatGpt = chatResponse(ideias)
    roteiro,lista_ideias = resposta_chatGpt['roteiro'],resposta_chatGpt['ideias']
    numero_aleatorio = random.randint(0,len(lista_ideias))

    try:ideia_aleatoria_imagem = lista_ideias[numero_aleatorio]
    except:ideia_aleatoria_imagem = lista_ideias[numero_aleatorio-1]

    print('Pegando vídeos')
    videos = obter_videos_por_tema(ideia_aleatoria_imagem, 'SUA CHAVE API DO PEXELS', 15)

    baixar_videos(videos,'./videos')
    textToVoice('TextsAndAudio/roteiro.txt',lang='pt-br',outputName='AudioRoteiro')
    mesclar_audio('videos/0.mp4', 'TextsAndAudio/audioRoteiro.mp3', 'videos')
 
    return 'Vídeo finalizado. Salvo em C:/Users/joaor/Downloads'