import ffmpeg
import os


def video_to_gif():

    for file in os.listdir('video'):
        
        if file.endswith(('.mp4', '.MP4')):
            
            file_name =  file.split('.')[0]
            
            gif_file = file_name + '.gif'

            vtg = ffmpeg.input(f'video/{file}')

            vtg = ffmpeg.filter(vtg, 'fps', fps=2)

            vtg = ffmpeg.output(vtg, f'gif/{gif_file}')

            ffmpeg.run(vtg)

        else:
            print('Bad extension in the file ! :)')


def main():
    video_to_gif()


if __name__ == '__main__':
    main()