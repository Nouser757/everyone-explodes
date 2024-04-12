from ktools import Edge, a1z26, rangify
import pygame
import math

title = ['PASTFEELING', 'PASTLANGUAGE', 'PASTTHEDESIREFORUNDERSTANDING', 'PASTMEANING']

patterns = [[
  #red1
  '000010000'
  '000000000'
  '000111000'
  '000000000'
  '001111100'
  '000000000'
  '011111110'
  '000000000'
  '111111111',
  #red2
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '001111100'
  '000010000'
  '111010111'
  '001111100',
  #red3
  '001111100'
  '111010111'
  '000010000'
  '001111100'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #red4
  '000000000'
  '111000101'
  '101000101'
  '101010101'
  '101111101'
  '101010101'
  '101000101'
  '101000111'
  '000000000'
],[
  #orange1
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000000000'
  '111111111',
  #orange2
  '111111111'
  '000000000'
  '111111111'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #orange3
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000000000'
  '111111111'
  '000000000'
  '000000000'
  '000000000',
  #orange4
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000000000'
  '111111111'
  '000000000'
  '000000000'
],[
  #yellow1
  '001010100'
  '001010100'
  '001010100'
  '000000000'
  '001010100'
  '000000000'
  '001010100'
  '001010100'
  '001010100',
  #yellow2
  '000000000'
  '000000111'
  '000000101'
  '111110111'
  '000010000'
  '111011111'
  '101000000'
  '111000000'
  '000000000',
  #yellow3
  '110010011'
  '100000001'
  '000111000'
  '001000100'
  '101000101'
  '001000100'
  '000111000'
  '100000001'
  '110010011'
],[
  #chartreuse1
  '101000011'
  '101000010'
  '100000011'
  '101000000'
  '100000001'
  '010100000'
  '110000111'
  '001100000'
  '101011111',
  #chartreuse2
  '110000101'
  '010000101'
  '110000001'
  '000000101'
  '100000001'
  '000001010'
  '111000011'
  '000001100'
  '111110101'
],[
  #lime1
  '001110111'
  '000000000'
  '010111111'
  '010000000'
  '011010111'
  '010000000'
  '010111111'
  '000000000'
  '001110111',
  #lime2
  '111011100'
  '000000000'
  '111111010'
  '000000010'
  '111010110'
  '000000010'
  '111111010'
  '000000000'
  '111011100'
],[
  #green1
  '000000011'
  '011111010'
  '010001010'
  '010111110'
  '010101010'
  '011111010'
  '010100010'
  '010111110'
  '110000000',
  #green2
  '001101100'
  '001101100'
  '110010011'
  '110000011'
  '001000100'
  '110000011'
  '110010011'
  '001101100'
  '001101100'
],[
  #teal1
  '111000111'
  '111111111'
  '110000011'
  '010101010'
  '010010010'
  '010101010'
  '110000011'
  '111111111'
  '111000111',
  #teal2
  '101000101'
  '011100010'
  '101000111'
  '000010010'
  '000111000'
  '010010000'
  '111000101'
  '010001110'
  '101000101'
],[
  #cyan1
  '000010001'
  '000000000'
  '000000000'
  '010000000'
  '101000100'
  '010000000'
  '000001010'
  '000000000'
  '100010101',
  #cyan2
  '100010000'
  '000000000'
  '000000000'
  '000000010'
  '001000101'
  '000000010'
  '010100000'
  '000000000'
  '101010001'
],[
  #blue1
  '000000110'
  '000001001'
  '000001001'
  '000000110'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #blue2
  '000000000'
  '000000000'
  '000000000'
  '011000000'
  '100100000'
  '100100000'
  '011000000'
  '000000000'
  '000000000',
  #blue3
  '000000000'
  '000000000'
  '000000110'
  '000001001'
  '000001001'
  '000000110'
  '000000000'
  '000000000'
  '000000000',
  #blue4
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '011000000'
  '100100000'
  '100100000'
  '011000000',
],[
  #violet1
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '100000001'
  '111111111',
  #violet2
  '000111000'
  '000101000'
  '000101000'
  '000101000'
  '000101000'
  '000101000'
  '000101000'
  '000101000'
  '000111000',
  #violet3
  '000000000'
  '000000000'
  '001111100'
  '001000100'
  '001000100'
  '001000100'
  '001000100'
  '001000100'
  '001111100',
  #violet4
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '011111110'
  '010000010'
  '010000010'
  '010000010'
  '011111110'
],[
  #turquoise1
  '011100000'
  '001000000'
  '011100000'
  '000001010'
  '001010100'
  '010100000'
  '000001110'
  '000000100'
  '000001110',
  #turquoise2
  '000000000'
  '000000000'
  '000000000'
  '001111100'
  '000000000'
  '111010111'
  '101010101'
  '001010100'
  '101010101',
  #turquoise3
  '101000101'
  '101000101'
  '111111111'
  '000010000'
  '001010100'
  '000010000'
  '111111111'
  '101000101'
  '101000101',
  #turquoise4
  '001111100'
  '010000010'
  '100111001'
  '101000101'
  '101010101'
  '101000101'
  '100111001'
  '010000010'
  '001111100',
  #turquoise5
  '001000100'
  '111111111'
  '001000100'
  '111111111'
  '001000100'
  '001010100'
  '001010100'
  '001010100'
  '001000100',
  #turquoise6
  '000011000'
  '001000000'
  '000011010'
  '011111010'
  '000000000'
  '010111110'
  '010110000'
  '000000100'
  '000110000',
  #turquoise7
  '000000000'
  '000000000'
  '101010101'
  '001010100'
  '110111011'
  '001010100'
  '101010101'
  '000000000'
  '000000000',
  #turquoise8
  '011111110'
  '000000000'
  '011101110'
  '010001000'
  '010111010'
  '000100010'
  '011101110'
  '000000000'
  '011111110',
  #turquoise9
  '100100101'
  '111111101'
  '100000001'
  '101111101'
  '101000101'
  '101111101'
  '100000001'
  '101111111'
  '101001001',
],[
  
  #indigo1
  '000000000'
  '000000000'
  '000000000'
  '000011000'
  '000011000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo2
  '000000000'
  '000000000'
  '000111100'
  '000111100'
  '000111100'
  '000111100'
  '000000000'
  '000000000'
  '000000000',
  #indigo3
  '000000000'
  '001111110'
  '001111110'
  '001111110'
  '001111110'
  '001111110'
  '001111110'
  '000000000'
  '000000000',
  #indigo4
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000000000',
  #indigo5
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000111111'
  '110111111'
  '110000000',
  #indigo6
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000001111'
  '001101111'
  '001100000',
  #indigo7
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000000011'
  '000011011'
  '000011000',
  #indigo8
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000000000'
  '000000110'
  '000000110',
  #indigo9
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000111111'
  '110111111'
  '110000000'
  '000000000'
  '000000000',
  #indigo10
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000001111'
  '001101111'
  '001100000'
  '000000000'
  '000000000',
  #indigo11
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000000011'
  '000011011'
  '000011000'
  '000000000'
  '000000000',
  #indigo12
  '011111111'
  '011111111'
  '011111111'
  '011111111'
  '000000000'
  '000000110'
  '000000110'
  '000000000'
  '000000000',
  #indigo13
  '011111111'
  '011111111'
  '000111111'
  '110111111'
  '110000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo14
  '011111111'
  '011111111'
  '000001111'
  '001101111'
  '001100000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo15
  '011111111'
  '011111111'
  '000000011'
  '000011011'
  '000011000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo16
  '011111111'
  '011111111'
  '000000000'
  '000000110'
  '000000110'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo17
  '000111111'
  '110111111'
  '110000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo18
  '000001111'
  '001101111'
  '001100000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo19
  '000000011'
  '000011011'
  '000011000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo20
  '000000000'
  '000000110'
  '000000110'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo21
  '000000000'
  '000000000'
  '000000000'
  '000110000'
  '000110000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo22
  '000000000'
  '000000000'
  '001111000'
  '001111000'
  '001111000'
  '001111000'
  '000000000'
  '000000000'
  '000000000',
  #indigo23
  '000000000'
  '011111100'
  '011111100'
  '011111100'
  '011111100'
  '011111100'
  '011111100'
  '000000000'
  '000000000',
  #indigo24
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '000000000',
  #indigo25
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111000'
  '111111011'
  '000000011',
  #indigo26
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111100000'
  '111101100'
  '000001100',
  #indigo27
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '110000000'
  '110110000'
  '000110000',
  #indigo28
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '000000000'
  '011000000'
  '011000000',
  #indigo29
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111111000'
  '111111011'
  '000000011'
  '000000000'
  '000000000',
  #indigo30
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '111100000'
  '111101100'
  '000001100'
  '000000000'
  '000000000',
  #indigo31
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '110000000'
  '110110000'
  '000110000'
  '000000000'
  '000000000',
  #indigo32
  '111111110'
  '111111110'
  '111111110'
  '111111110'
  '000000000'
  '011000000'
  '011000000'
  '000000000'
  '000000000',
  #indigo33
  '111111110'
  '111111110'
  '111111000'
  '111111011'
  '000000011'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo34
  '111111110'
  '111111110'
  '111100000'
  '111101100'
  '000001100'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo35
  '111111110'
  '111111110'
  '110000000'
  '110110000'
  '000110000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo36
  '111111110'
  '111111110'
  '000000000'
  '011000000'
  '011000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo37
  '111111000'
  '111111011'
  '000000011'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo38
  '111100000'
  '111101100'
  '000001100'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo39
  '110000000'
  '110110000'
  '000110000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #indigo40
  '000000000'
  '011000000'
  '011000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '000000000'
], [
  #purple1
  '111101111'
  '111101111'
  '101101011'
  '001100011'
  '011000110'
  '011000110'
  '000000000'
  '011000110'
  '011000110',
  #purple2
  '111111111'
  '100000001'
  '100000101'
  '100000001'
  '100000001'
  '100000001'
  '101000001'
  '100000001'
  '111111111',
  #purple3
  '111111111'
  '100000001'
  '100000101'
  '100000001'
  '100010001'
  '100000001'
  '101000001'
  '100000001'
  '111111111',
  #purple4
  '111111111'
  '100000001'
  '101000101'
  '100000001'
  '100000001'
  '100000001'
  '101000101'
  '100000001'
  '111111111',
  #purple5
  '111111111'
  '100000001'
  '101000101'
  '100000001'
  '100010001'
  '100000001'
  '101000101'
  '100000001'
  '111111111',
  #purple6
  '111111111'
  '100000001'
  '101000101'
  '100000001'
  '101000101'
  '100000001'
  '101000101'
  '100000001'
  '111111111',
  #purple7
  '111111111'
  '100000001'
  '101000101'
  '100000001'
  '101010101'
  '100000001'
  '101000101'
  '100000001'
  '111111111',
  #purple8
  '111111111'
  '100000001'
  '101010101'
  '100000001'
  '101000101'
  '100000001'
  '101010101'
  '100000001'
  '111111111',
  #purple9
  '000010000'
  '000011000'
  '000011100'
  '111111110'
  '111111111'
  '111111110'
  '000011100'
  '000011000'
  '000010000',
  #purple10
  '110000011'
  '111000111'
  '011101110'
  '001111100'
  '000111000'
  '001111100'
  '011101110'
  '111000111'
  '110000011',
  #purple11
  '101010101'
  '000000000'
  '101010101'
  '000000000'
  '101010101'
  '000000000'
  '101010101'
  '000000000'
  '101010101',
  #purple12
  '001101100'
  '001101100'
  '001101100'
  '001101100'
  '001101100'
  '001101100'
  '000000000'
  '001101100'
  '001101100',
  #purple13
  '000111000'
  '000111000'
  '000111000'
  '000111000'
  '111111111'
  '011111110'
  '001111100'
  '000111000'
  '000010000'
],[
  #magenta1
  '000000000'
  '000000000'
  '000000000'
  '111000111'
  '010000010'
  '111000111'
  '000000000'
  '000000000'
  '000000000',
  #magenta2
  '111000111'
  '010000010'
  '010000010'
  '010000010'
  '010000010'
  '010000010'
  '010000010'
  '010000010'
  '111000111',
  #magenta3
  '000000000'
  '111000111'
  '010000010'
  '010000010'
  '010000010'
  '010000010'
  '010000010'
  '111000111'
  '000000000',
  #magenta4
  '000000000'
  '000000000'
  '111000111'
  '010000010'
  '010000010'
  '010000010'
  '111000111'
  '000000000'
  '000000000',
  #magenta5
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '010010010'
  '111111111'
  '000000000'
  '000000000'
  '000000000',
  #magenta6
  '111111111'
  '010010010'
  '010010010'
  '010010010'
  '010010010'
  '010010010'
  '010010010'
  '010010010'
  '111111111',
  #magenta7
  '000000000'
  '111111111'
  '010010010'
  '010010010'
  '010010010'
  '010010010'
  '010010010'
  '111111111'
  '000000000',
  #magenta8
  '000000000'
  '000000000'
  '111111111'
  '010010010'
  '010010010'
  '010010010'
  '111111111'
  '000000000'
  '000000000',
  #magenta9
  '000101000'
  '000111000'
  '000101000'
  '000000000'
  '000000000'
  '000000000'
  '000101000'
  '000111000'
  '000101000',
  #magenta10
  '100000001'
  '111111111'
  '100000001'
  '000000000'
  '000000000'
  '000000000'
  '100000001'
  '111111111'
  '100000001',
  #magenta11
  '010000010'
  '011111110'
  '010000010'
  '000000000'
  '000000000'
  '000000000'
  '010000010'
  '011111110'
  '010000010',
  #magenta12
  '001000100'
  '001111100'
  '001000100'
  '000000000'
  '000000000'
  '000000000'
  '001000100'
  '001111100'
  '001000100',
  #magenta13
  '000101000'
  '000111000'
  '000101000'
  '000101000'
  '000111000'
  '000101000'
  '000101000'
  '000111000'
  '000101000',
  #magenta14
  '100000001'
  '111111111'
  '100000001'
  '100000001'
  '111111111'
  '100000001'
  '100000001'
  '111111111'
  '100000001',
  #magenta15
  '010000010'
  '011111110'
  '010000010'
  '010000010'
  '011111110'
  '010000010'
  '010000010'
  '011111110'
  '010000010',
  #magenta16
  '001000100'
  '001111100'
  '001000100'
  '001000100'
  '001111100'
  '001000100'
  '001000100'
  '001111100'
  '001000100'
],[
  #pink1
  '001010101'
  '001010101'
  '001010101'
  '001011111'
  '001000100'
  '111110100'
  '101010100'
  '101010100'
  '101010100',
  #pink2
  '000000000'
  '000000000'
  '000111000'
  '000101000'
  '010111010'
  '010000010'
  '110111011'
  '000000000'
  '001111100',
  #pink3
  '000000000'
  '111111111'
  '100100001'
  '111111111'
  '000101000'
  '111111111'
  '100001001'
  '111111111'
  '000000000',
  #pink4
  '101111101'
  '010010010'
  '100111001'
  '000000000'
  '101010101'
  '011000110'
  '001000100'
  '001000100'
  '001000100',
  #pink5
  '110101111'
  '110100000'
  '000001111'
  '000100000'
  '000111000'
  '000001000'
  '111100000'
  '000001011'
  '111101011',
  #pink6
  '111000111'
  '100000001'
  '101111101'
  '100010001'
  '100101001'
  '100101001'
  '101111101'
  '100000001'
  '111000111',
  #pink7
  '001010100'
  '001010100'
  '111010111'
  '000000000'
  '111010111'
  '000000000'
  '111010111'
  '001010100'
  '001010100',
  #pink8
  '001111100'
  '001000100'
  '101111111'
  '100000101'
  '101111101'
  '101000001'
  '111111101'
  '001000100'
  '001111100',
  #pink9
  '010011100'
  '101010100'
  '101000100'
  '000010000'
  '111010111'
  '000010000'
  '001000101'
  '001010101'
  '001110010',
  #pink10
  '100010001'
  '101010101'
  '100111001'
  '010010010'
  '010111010'
  '010010010'
  '001010100'
  '011010110'
  '101010101',
  #pink11
  '101101101'
  '100111001'
  '100010001'
  '101010101'
  '001111100'
  '101010101'
  '100010001'
  '000111000'
  '101101101',
  #pink12
  '000010000'
  '001000100'
  '000010000'
  '011000110'
  '011010110'
  '000000000'
  '111010111'
  '111000111'
  '111010111',
  #pink13
  '000001111'
  '011101001'
  '010101001'
  '011101111'
  '000000000'
  '111101110'
  '100101010'
  '100101110'
  '111100000',
  #pink14
  '000010000'
  '001111100'
  '011010110'
  '010010010'
  '111111111'
  '010010010'
  '010010010'
  '010111010'
  '000010000',
  #pink15
  '101010000'
  '101000000'
  '101010111'
  '000010001'
  '111111111'
  '100010000'
  '111010101'
  '000000101'
  '000010101',
  #pink16
  '000000000'
  '010000010'
  '111000111'
  '000000000'
  '111111111'
  '100010001'
  '101111101'
  '101000101'
  '101000101',
  #pink17
  '111000111'
  '111000111'
  '111111111'
  '111000111'
  '000000000'
  '111000111'
  '111111111'
  '111000111'
  '111000111',
  #pink18
  '000000000'
  '000000000'
  '001111100'
  '000000000'
  '111010111'
  '000000000'
  '011101110'
  '000101000'
  '111101111',
  #pink19
  '111110011'
  '100001101'
  '100000010'
  '100111010'
  '100101001'
  '010111001'
  '010000001'
  '101100001'
  '110011111',
  #pink20
  '100100111'
  '101001000'
  '101010011'
  '101010100'
  '101010101'
  '101010100'
  '101010011'
  '101001000'
  '100100111',
  #pink21
  '111001001'
  '000100101'
  '110010101'
  '001010101'
  '101010101'
  '001010101'
  '110010101'
  '000100101'
  '111001001'
],[
  #grey1
  '111111111'
  '000010001'
  '000010001'
  '000010001'
  '000010001'
  '000000001'
  '000000001'
  '000000001'
  '000000001',
  #grey2
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000',
  #grey3
  '111110001'
  '000000001'
  '000000001'
  '000000001'
  '111110001'
  '000000001'
  '000000001'
  '000000001'
  '111111111',
  #grey4
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '111110000'
  '000010000'
  '111110000'
  '000010000'
  '111110000',
  #grey5
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '100010001'
  '100010001'
  '100010001'
  '100010001'
  '111111111',
  #grey6
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '100000001',
  #grey7
  '111111111'
  '000000001'
  '001000101'
  '001000101'
  '111111111'
  '101000101'
  '101000101'
  '100000001'
  '100000001',
  #grey8
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '111111111',
  #grey9
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '100000001'
  '000000001'
  '000000001'
  '000000001'
  '111111111',
  #grey10
  '111111111'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '000010000',
  #grey11
  '111111111'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '111111111',
  #grey12
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000000000'
  '000000000'
  '000000000'
  '000000000',
  #grey13
  '100000000'
  '100000000'
  '101000100'
  '101000100'
  '111111111'
  '101000100'
  '101000100'
  '100000000'
  '100000000',
  #grey14
  '000000000'
  '000000000'
  '000000000'
  '000000000'
  '101010000'
  '101010000'
  '101010000'
  '000010000'
  '111110000',
  #grey15
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '111111111'
  '100000001'
  '100000001'
  '100000001'
  '100000001',
  #grey16
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '111111111',
  #grey17
  '000010000'
  '000010000'
  '001010100'
  '001010100'
  '111111111'
  '001010101'
  '001010101'
  '000010001'
  '000010001',
  #grey18
  '111111111'
  '000000000'
  '001000100'
  '001000100'
  '111111111'
  '001010100'
  '001010100'
  '000010000'
  '000010000',
  #grey19
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '111110000'
  '000010000'
  '000010000'
  '000010000'
  '000011111',
  #grey20
  '111111111'
  '100010001'
  '100010001'
  '100010001'
  '111110001'
  '000000001'
  '000000001'
  '000000001'
  '000000001',
  #grey21
  '111110001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '111111111',
  #grey22
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '000000001'
  '111111111',
  #grey23
  '111111111'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000000000'
  '000000000'
  '000000000'
  '111111111',
  #grey24
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '000010000',
  #grey25
  '111111111'
  '000000000'
  '000000000'
  '000000000'
  '111111111'
  '000000001'
  '000000001'
  '000000001'
  '000000001',
  #grey26
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '111111111'
  '100000001'
  '100000001'
  '100000001'
  '100000001',
  #grey27
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '111111111',
  #grey28
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '111111111',
  #grey29
  '111111111'
  '000000001'
  '000000001'
  '000000001'
  '111111111'
  '100000001'
  '100000001'
  '100000001'
  '100000001',
  #grey30
  '000010000'
  '000010000'
  '001010100'
  '001010100'
  '111111111'
  '001010100'
  '001010100'
  '000010000'
  '111111111',
  #grey31
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '111111111'
  '000010001'
  '000010001'
  '000010001'
  '000010001',
  #grey32
  '111110001'
  '000000001'
  '001000101'
  '001000101'
  '111110101'
  '001000101'
  '001000101'
  '000000001'
  '111111111',
  #grey33
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '111111111'
  '100000000'
  '100000000'
  '100000000'
  '100000000',
  #grey34
  '000010000'
  '000010000'
  '001010100'
  '001010100'
  '101010101'
  '101010101'
  '101010101'
  '100010001'
  '111111111',
  #grey35
  '111111111'
  '000000001'
  '001000101'
  '001000101'
  '001000101'
  '001000101'
  '001000101'
  '000000001'
  '111111111',
  #grey36
  '111111111'
  '100010001'
  '101010101'
  '101010101'
  '111110101'
  '001000101'
  '001000101'
  '000000001'
  '000000001',
  #grey37
  '000010000'
  '000010000'
  '000010000'
  '000010000'
  '111111111'
  '000010000'
  '000010000'
  '000010000'
  '111110000',
  #grey38
  '100000000'
  '100000000'
  '100000000'
  '100000000'
  '111111111'
  '100010000'
  '100010000'
  '100010000'
  '100010000'
]]

patternCounts = [4,4,3,2,2,2,2,2,4,4,9,40,13,8,21,38]

colors = [[(108,25,14),(255,78,65)], [(108,54,16),(255,143,49)], [(104,83,15),(255,210,50)], [(85,95,13),(219,239,48)],
          [(51,92,14),(133,232,54)], [(12,88,13),(46,226,53)], [(10,92,48),(46,227,142)], [(10,93,85),(43,237,209)], 
          [(12,51,104),(56,136,255)], [(89,28,103),(218,83,243)], [(10,81,105), (46,206,255)], [(16,22,105), (56,72,255)],
          [(53,26,105), (142,79,255)], [(109,29,86),(253,85,226)], [(108,27,51), (254,83,136)], [(66,66,66), (169,169,169)]]

#75px square, 10x gaps
def display(c, PN, s, f):
  grid = patterns[c][PN-1]
  if f: grid = grid[::-1]
  color = colors[c]
  pygame.init()
  screen = pygame.display.set_mode((945, 945))
  pygame.display.set_caption(title[s])

  #draw border
  for i in range(11): pygame.draw.rect(screen, color[0], pygame.Rect(10+(85*i), 10, 75, 75))
  for i in range(9):
    pygame.draw.rect(screen, color[0], pygame.Rect((10, 95+(85*i), 75, 75)))
    pygame.draw.rect(screen, color[0], pygame.Rect((860, 95+(85*i), 75, 75)))
  for i in range(11): pygame.draw.rect(screen, color[0], pygame.Rect(10+(85*i), 860, 75, 75))

  #draw grid
  for i, square in enumerate(grid): pygame.draw.rect(screen, color[int(square)], pygame.Rect(95+(85*(i%9)), 95+(85*(i//9)), 75, 75))

  pygame.display.flip()
  wait = True
  while wait:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: wait=False
  pygame.quit()

def red(edge: Edge, prev, used, flip):
  PN = rangify(max(edge.totalBatteries, 1) * max(edge.indicatorCount, 1), 4)
  display(0, PN, len(prev), flip)
  prev.append([0, PN])
  return prev

def orange(edge: Edge, prev, used, flip):
  PN = rangify((len(prev)+1) * max(int(edge.serialDigits[-1]), 1), 4)
  display(1, PN, len(prev), flip)
  prev.append([1, PN])
  return prev

def yellow(edge: Edge, prev, used, flip):
  PN = len(prev)+1 if edge.serialDigitSum%2 != 0 else 4-(len(prev)+1)
  display(2, PN, len(prev), flip)
  prev.append([2, PN])
  return prev

def chartreuse(edge: Edge, prev, used, flip):
  lcount = 0
  for line in used:
    for char in line[:2]:
      if char == '0': lcount = lcount+1
  if lcount == 4: lcount = 8 if edge.portPlates%2 == 0 else 0
  PN = (1 if lcount > 4 else 2)
  display(3, PN, len(prev), flip)
  prev.append([3, PN])
  return prev

def lime(edge: Edge, prev, used, flip):
  if edge.dBatteries == edge.aBatteries: moreD = (edge.serialDigits[0]%2 == 1)
  else: moreD = edge.dBatteries > edge.aBatteries
  if prev == []: moreD = not moreD
  elif patternCounts[prev[-1][0]] <= 3: moreD = not moreD
  PN = (1 if moreD else 2)
  display(4, PN, len(prev), flip)
  prev.append([4, PN])
  return prev

def green(edge: Edge, prev, used, flip):
  if prev == []:
    for i, line in enumerate(used):
      for j, char in enumerate(line):
        if char == '0': 
          find = (i*4)+j
          pattern = 1
  else: find, pattern = prev[-1]
  pix = patterns[find][pattern].count('1')
  PN = rangify(pix, 2)
  display(5, PN, len(prev), flip)
  prev.append([5, PN])
  return prev

def teal(edge: Edge, prev, used, flip):
  ucount = 0
  for char in used[0]:
    if char == '0': ucount = ucount + 1
  for char in used[1]:
    if char == '0': ucount = ucount + 1
  if ucount == 4: ucount = 8 if edge.litIndicatorCount%2 == 1 else 0
  PN = (1 if ucount > 4 else 2)
  display(6, PN, len(prev), flip)
  prev.append([6, PN])
  return prev

def cyan(edge: Edge, prev, used, flip):
  PN = (1 if int(edge.serialDigits[-1])%2 == 1 else 2)
  display(7, PN, len(prev), flip)
  prev.append([7, PN])
  return prev

def blue(edge: Edge, prev, used, flip):
  x = ''
  while not x.isdigit(): x = input("How many Wavetapping modules? > ")
  PN = rangify(int(x), 4)
  display(8, PN, len(prev), flip)
  prev.append([8, PN])
  return prev

def violet(edge: Edge, prev, used, flip):
  if prev == []: PN = 1
  else:
    use = [1, 3] if prev[-1][0] <= 8 else [2, 4]
    PN = use[0] if prev[-1][1] <= math.ceil(patternCounts[prev[-1][0]] / 2) else use[1]
  display(9, PN, len(prev), flip)
  prev.append([9, PN])
  return prev

def turquoise(edge: Edge, prev, used, flip):
  indVal = edge.unlitIndicatorCount + (edge.litIndicatorCount * 2)
  if 'uBOB' in edge.indicators: indVal = indVal+4
  elif 'lBOB' in edge.indicators: indVal = indVal+3
  PN = rangify(max(edge.portPlates, 1) * max(indVal, 1), 9)
  display(10, PN, len(prev), flip)
  prev.append([10, PN])
  return prev

def indigo(edge: Edge, prev, used, flip):
  if prev == []: total = edge.serialDigitSum
  else: total = sum(x[1] for x in prev)
  PN = rangify(total*edge.totalModuleCount, 40)
  display(11, PN, len(prev), flip)
  prev.append([11, PN])
  return prev

def purple(edge: Edge, prev, used, flip):
  total = sum([(int(x) if x.isdigit() else a1z26(x)) for x in edge.serial])
  index = rangify(total*(edge.totalBatteries if edge.totalBatteries > 0 else 13), 95)-1
  phone = [1] + [int(x) for x in '727863264649'] + [10 for _ in range(5)] + [1] + [int(x) for x in '727833354649'] + [10 for _ in range(5)] + [1] + [int(x) for x in '727852648243'] + [10 for _ in range(5)] + [1] + [int(x) for x in '72788433374733678633778263464'] + [11] + [12 for _ in range(9)] + [13]
  PN = phone[index]
  display(12, PN, len(prev), flip)
  prev.append([12, PN])
  return prev

def magenta(edge: Edge, prev, used, flip):
  partA = sum([(int(x) if x.isdigit() else a1z26(x)) for x in edge.serial[:3]])
  partB = sum([(int(x) if x.isdigit() else a1z26(x)) for x in edge.serial[-3:]])
  total = partA+partB
  if total == 0: PN = 8
  else: PN = rangify(total, 8)
  if total > 2222: PN = PN+8
  display(13, PN, len(prev), flip)
  if total > 2222: PN = PN-8
  prev.append([13, PN])
  return prev

def pink(edge: Edge, prev, used, flip):
  total = int(''.join([str(x) for x in edge.serialDigits]))
  if total == 0:
    if prev == []: total = a1z26(edge.serialLetters[0])
    else: total = prev[-1][1]
  PN = rangify(total, 21)
  display(14, PN, len(prev), flip)
  prev.append([14, PN])
  return prev

def grey(edge: Edge, prev, used, flip):
  count = 0
  weird = [0,1,2,3,4,5,6,7,10,8,11,12,9,13,14,15]
  for i, x in enumerate(used[0]):
    if x == '0': count = count + patternCounts[weird[i]]
  for i, x in enumerate(used[1]):
    if x == "0": count = count + patternCounts[weird[i+4]]
  for i, x in enumerate(used[2]):
    if x == "0": count = count + patternCounts[weird[i+8]]
  for i, x in enumerate(used[3]):
    if x == "0": count = count + patternCounts[weird[i+12]]
  PN = rangify(count, 38)
  display(15, PN, len(prev), flip)
  prev.append([15, PN])
  return prev


def updateInput(screen, used):
  for i, c in enumerate(colors): pygame.draw.rect(screen, c[0] if used[i//4][i%4] == '0' else (255,255,255), pygame.Rect((29+(229*(i%4)), 29+(229*(i//4)), 200, 200)))
  pygame.display.flip()

grid = [red, orange, yellow, chartreuse, lime, green, teal, cyan, turquoise, blue, indigo, purple, violet, magenta, pink, grey]

def wavetapping(edge: Edge):
  used = [['0','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']]
  pygame.init()
  screen = pygame.display.set_mode((945, 945))
  pygame.display.set_caption(title[3])
  updateInput(screen, used)
  print("Click to toggle used colours.")
  areas = [pygame.Rect((29+(229*(i%4)), 29+(229*(i//4)), 200, 200)) for i in range(16)]
  wait = True
  while wait:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: wait=False
      if event.type == pygame.MOUSEBUTTONUP:
        for i, area in enumerate(areas):
          if area.collidepoint(event.pos):
            used[i//4][i%4] = '1' if used[i//4][i%4] == '0' else '0'
            updateInput(screen,used)
  pygame.quit()
  fc = 0
  for x in edge.serialLetters:
    if x in 'FRUMS': fc = fc + 1
  flip = fc >= 3
  stage1 = int(input("Enter first stage index [reading order, 1-16] > "))-1
  run = grid[stage1](edge, [], used, flip)
  stage2 = int(input("Enter second stage index [reading order, 1-16] > "))-1
  run = grid[stage2](edge, run, used, flip)
  stage3 = int(input("Enter third stage index [reading order, 1-16] > "))-1
  run = grid[stage3](edge, run, used, flip)