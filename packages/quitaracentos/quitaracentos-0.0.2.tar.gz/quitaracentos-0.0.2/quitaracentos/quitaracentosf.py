def quitaracentos(cadena):
  '''
  str->str
  OBJ: Quitar los acentos encontrados en el idioma español de una cadena (exceptuando la ñ)
  OBJ: Remove the accents found in the Spanish language from a string (except the ñ)
  '''
  mapa_acentos=str.maketrans({'á':'a','é':'e','í':'i','ó':'o','ú':'u','Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U','ü':'u','Ü':'U'})
  cadena=cadena.translate(mapa_acentos)
  return cadena