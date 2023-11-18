# QUITADOR DE ACENTOS

© 2023 FerdinandoPH

Descripción: Este programa quita los acentos españoles de una palabra o frase, dejando la ñ. Es un programa muy simplón, pero es una forma rápida y eficiente de quitar los acentos dejando la ñ y no tener que preocuparse de tronchos largos de escribir como regex cada vez que necesites quitar los acentos

Instálalo con ```pip install quitaracentos```.

Description: This program removes the spanish accents from a word or phrase, leaving the ñ. It's a very simple program, but it's a fast and effective way of removing accents leaving the ñ, without having to worry about long, complicated stuff like regex every time.

Install it with ```pip install quitaracentos```.

## Ejemplo/Example
```
  from quitaracentos import quitaracentos

  print(quitaracentos("áÁéÉíÍóÓúÚüÜñÑ")) # -> aAeEiIoOuUuUñÑ
```
