def rgb_to_hsv(r, g, b):
  
    # Os valores R, G, B são dividos por 255
    # Para mudar o range de 0..255 para 0..1:
    r, g, b = r / 255.0, g / 255.0, b / 255.0
  
    # h, s, v = hue, saturation, value
    cmax = max(r, g, b)    # máximo do r, g, b
    cmin = min(r, g, b)    # mínimo do r, g, b
    diff = cmax-cmin       # diferença entre cmax e cmin.
  
    # Se cmax e cmin são iguais, então h = 0
    if cmax == cmin: 
        h = 0
      
    # Se cmax é igual ao r, então computa o h:
    elif cmax == r: 
        h = (60 * ((g - b) / diff) + 360) % 360
  
    # Se cmax é igual ao g, então computa o h:
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
  
    # Se cmax é igual ao b, então computa o h:
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
  
    # Se cmax igual a zero:
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
  
    # Computar o v
    v = cmax * 100
    return h, s, v
  
print(rgb_to_hsv(129, 88, 47))