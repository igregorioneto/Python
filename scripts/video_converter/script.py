from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(input_file, output_file):
    try:
        # carregar o arquivo AVI
        video = VideoFileClip(input_file)

        # Total de frames
        total_frames = video.reader.nframes

        # Função callback para acompanhar o processo de conversão
        def update_progress(frame, total_frames):
            progress = min((frame + 1) / total_frames, 1.0)
            print(f"Progresso de conversão: {progress * 100:.2f}%")

        # Converte cada frame individualmente e acompanha o progresso
        for i, frame in enumerate(video.iter_frames()):
            update_progress(i, total_frames)

        # Salvar o arquivo MP4 e acompanhar o progresso
        video.write_videofile(output_file, codec="libx264")

        print("Conversão concluída com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {e}")

if __name__ == "__main__":
    # Caminho do arquivo de entrada AVI
    input_file = "/home/greg/Downloads/Toma Lá Dá Cá [2ªTemporada]By - Anarky.69/Toma Lá Dá Cá - Ep.15.avi"

    # Caminho para salvar o arquivo no formato MP4
    output_file = "/home/greg/Downloads/Toma Lá Dá Cá - Ep.15.mp4"

    # Chamando a função para converter o arquivo
    convert_avi_to_mp4(input_file, output_file)