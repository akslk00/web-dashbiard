import streamlit as st

#이미니 / 동영상을 화면에 보여주는 방법

from PIL import Image

def main():
    img = Image.open('./data/image_03.jpg')
    print(img)
    st.image(img)

    st.image(img,use_column_width=True)

    img_url='https://cdn.kormedi.com/wp-content/uploads/2023/10/gettyimages-a11228594.jpg.webp'
    st.image(img_url)

    #동영상
    video_file=open('./data/video1.mp4', 'rb')
    st.video(video_file)

    youvideo = 'https://youtu.be/Y1qei5ZBl7I'
    st.video(youvideo)

if __name__ == '__main__':
    main()