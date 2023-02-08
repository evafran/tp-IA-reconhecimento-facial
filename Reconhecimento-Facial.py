import cv2 
import mediapipe as mp

webcam = cv2.VideoCapture(0)  # para conectar o python com a nossa webcam.

# ativando a solução de reconhecimento de rosto
reconhecimento_rosto = mp.solutions.face_detection
desenho = mp.solutions.drawing_utils  # ativando a solução de desenho
# criando o item que consegue ler uma imagem e reconhecer os rostos ali dentro
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()

while webcam.isOpened():
    validacao, frame = webcam.read()  # lê a imagem da webcam
    if not validacao:
        break
    imagem = frame
    # usa o reconhecedor para criar uma lista com os rostos reconhecidos
    lista_rostos = reconhecedor_rosto.process(imagem)

    if lista_rostos.detections:  # caso algum rosto tenha sido reconhecido
        for rosto in lista_rostos.detections:  # para cada rosto que foi reconhecido
            desenho.draw_detection(imagem, rosto)  # desenha o rosto na imagem

    # mostra a imagem da webcam para a gente
    cv2.imshow("Rostos na sua webcam", imagem)
    if cv2.waitKey(5) == 27:  # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam
        break
webcam.release()  # encerra a conexão com a webcam
cv2.destroyAllWindows()  # fecha a janela que mostra o que a webcam está vendo