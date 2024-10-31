#importação do opencv-python
import cv2

#criar uma variável para camera
cap = cv2.VideoCapture(0)

# enquanto a camera estiver aberta
while cap.isOpened():
    # sucesso-booleana (verificar se o frame esta vazio)
    # frame - captura
    sucesso, frame = cap.read()
    # realizar a verificação
    # sucesso = 1   fracaso = 0
    if not sucesso:
        print("ignorando o frame vazio da camêra")
        continue
    # carregar nosso frame - com título
    cv2.imshow('Camera',frame)
    # bitwise - tabela ASC II
    # 10 milissegundos
    # ord() - retorna o valor Unicode (ou ASC II)
    # o valor 0xFF é tabela ASC II estendida
    if cv2.waitKey(10) & 0xFF == ord('c'):
        break
# fechando a captura
cap.release()
# fechando todas janelas
cv2.destroyAllWindows()

