from moviepy.editor import VideoFileClip
import os


def video_to_gif(input_path, output_path, max_duration=10):
  
    if not os.path.exists(input_path):
        print(f"Erè: Fichye videyo {input_path} pa ekziste.")
        return
    
    valid_extensions = ['.mp4', '.avi', '.mov']
    if not any(input_path.lower().endswith(ext) for ext in valid_extensions):
        print("Erè: Ekstansyon videyo a pa sipòte.")
        return
    
    video_clip = VideoFileClip(input_path)
    
    if video_clip.duration > max_duration:
        print(f"Erè: Videyo a dwe 10 segonn maksimòm. Videyo a gen {video_clip.duration} segonn.")
        return
    
    video_gif = video_clip.to_gif(output_path)
    
    video_clip.close()
    
    print(f"Videyo a konvèti an fòma GIF ak siksè: {output_path}")


if __name__ == "__main__":
    video_to_gif("input.mp4", "output.gif")
