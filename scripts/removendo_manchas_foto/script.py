import cv2

image = cv2.imread("/home/greg/Imagens/imagem.jpeg")

# Aplicar um filtro de mediana para suavizar a imagem
image_smoothed = cv2.medianBlur(image, 5)

# Preencher as áreas danificadas usando a função inpaint
mask = cv2.cvtColor(image_smoothed, cv2.COLOR_BGR2GRAY)
dst = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Ajustar contraste
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
lab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
lab_planes = list(cv2.split(lab))
lab_planes[0] = clahe.apply(lab_planes[0])
lab = cv2.merge(lab_planes)
result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

# Exibir a imagem reparada
cv2.imshow('Imagem Reparada', result)
cv2.waitKey(0)
cv2.destroyAllWindows()