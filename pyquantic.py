class elementosNome:
    def __init__(self, sigla, nome, atomicidade, massa, periodo, familia, distribuicao, bloco, classificacao, estado):
        self.sigla = sigla
        self.nome = nome
        self.atomicidade = atomicidade
        self.massa = massa
        self.periodo = periodo
        self.familia = familia
        self.distribuicao = distribuicao
        self.bloco = bloco
        self.classificacao = classificacao
        self.estado = estado
 
H = elementosNome('H','Hidrogênio', 1, 1, 1, 1, '1s¹', 's', 'ametal', 'gás')
He = elementosNome('He','Hélio',2, 4, 1, 18, '1s²', 's', 'gás nobre', 'gás')
Li = elementosNome('Li','Lítio', 3, 7, 2, 1, '1s² 2s¹', 's', 'metal alcalino', 'sólido')
Be = elementosNome('Be','Berílio', 4, 9, 2, 2, '1s2 2s2', 's', 'metal alcalino-terroso', 'sólido')
B = elementosNome('B','Boro', 5, 11, 2, 13, '1s2 2s2 2p1', 'p', 'semimetal', 'sólido')
C = elementosNome('C','Carbono', 6, 12, 2, 14, '1s2 2s2 2p2', 'p', 'ametal', 'sólido')
N = elementosNome('N','Nitrogênio', 7, 14, 2, 15, '1s2 2s2 2p3', 'p', 'ametal', 'gás')
O = elementosNome('O','Oxigênio', 8, 16, 2, 16, '1s2 2s2 2p4', 'p', 'ametal', 'gás')
F = elementosNome('F','Flúor', 9, 19, 2, 17, '1s2 2s2 2p5', 'p', 'ametal', 'gás')
Ne = elementosNome('Ne','Neônio', 10, 20, 2, 18, '1s2 2s2 2p6', 'p', 'gás nobre', 'gás')
Na = elementosNome('Na','Sódio', 11, 23, 3, 1, '1s2 2s2 2p6 3s1', 's', 'metal alcalino', 'sólido')
Mg = elementosNome('Mg','Magnésio', 12, 24, 3, 2, '1s2 2s2 2p6 3s2', 's', 'metal alcalino-terroso', 'sólido')
Al = elementosNome('Al','Alumínio', 13, 27, 3, 13, '1s2 2s2 2p6 3s2 3p1', 'p', 'metal pós-transição', 'sólido')
Si = elementosNome('Si','Silício', 14, 28, 3, 14, '1s2 2s2 2p6 3s2 3p2', 'p', 'semimetal', 'sólido')
P = elementosNome('P','Fósforo', 15, 31, 3, 15, '1s2 2s2 2p6 3s2 3p3', 'p', 'ametal', 'sólido')
S = elementosNome('S','Enxofre', 16, 32, 3, 16, '1s2 2s2 2p6 3s2 3p4', 'p', 'ametal', 'sólido')
Cl = elementosNome('Cl','Cloro', 17, 35.5, 3, 17, '1s2 2s2 2p6 3s2 3p5', 'p', 'ametal', 'gás')
Ar = elementosNome('Ar','Argônio', 18, 40, 3, 18, '1s2 2s2 2p6 3s2 3p6', 'p', 'gás nobre', 'gás')
K = elementosNome('K','Potássio', 19, 39, 4, 1, '1s2 2s2 2p6 3s2 3p6 4s1', 's', 'metal alcalino', 'sólido')
Ca = elementosNome('Ca','Cálcio', 20, 40, 4, 2, '1s2 2s2 2p6 3s2 3p6 4s2', 's', 'metal alcalino-terroso', 'sólido')
Sc = elementosNome('Sc','Escândio', 21, 45, 4, 3, '1s2 2s2 2p6 3s2 3p6 4s2 3d1', 'd', 'metal de transição', 'sólido')
Ti = elementosNome('Ti','Titânio', 22, 48, 4, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d2', 'd', 'metal de transição', 'sólido')
V = elementosNome('V','Vanádio', 23, 51, 4, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d3', 'd', 'metal de transição', 'sólido')
Cr = elementosNome('Cr','Cromo', 24, 52, 4, 6, '1s2 2s2 2p6 3s2 3p6 4s1 3d5', 'd', 'metal de transição', 'sólido')
Mn = elementosNome('Mn','Manganês', 25, 55, 4, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d5', 'd', 'metal de transição', 'sólido')
Fe = elementosNome('Fe','Ferro', 26, 56, 4, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d6', 'd', 'metal de transição', 'sólido')
Co = elementosNome('Fe','Cobalto', 27, 59, 4, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d7', 'd', 'metal de transição', 'sólido')
Ni = elementosNome('Ni','Níquel', 28, 59, 4, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d8', 'd', 'metal de transição', 'sólido')
Cu = elementosNome('Cu','Cobre', 29, 63.5, 4, 11, '1s2 2s2 2p6 3s2 3p6 4s1 3d10', 'd', 'metal de transição', 'sólido')
Zn = elementosNome('Zn','Zinco', 30, 65, 4, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10', 'd', 'metal de transição', 'sólido')
Ga = elementosNome('Ga','Gálio', 31, 70, 4, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1', 'p', 'metal pós-transição', 'sólido')
Ge = elementosNome('Ge','Germânio', 32, 73, 4, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2', 'p', 'semimetal', 'sólido')
As = elementosNome('As','Arsênio', 33, 75, 4, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3', 'p', 'semimetal', 'sólido')
Se = elementosNome('Se','Selênio', 34, 79, 4, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4', 'p', 'ametal', 'sólido')
Br = elementosNome('Br','Bromo', 35, 80, 4, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5', 'p', 'ametal', 'líquido')
Kr = elementosNome('Kr','Criptônio', 36, 84, 4, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6', 'p', 'gás nobre', 'gás')
Rb = elementosNome('Rb','Rubídio', 37, 85.5, 5, 1, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1', 's', 'metal alcalino', 'sólido')
Sr = elementosNome('Sr','Estrôncio', 38, 88, 5, 2, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2', 's', 'metal alcalino-terroso', 'sólido')
Y = elementosNome('Y','Ítrio', 39, 89, 5, 3, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1', 'd', 'metal de transição', 'sólido')
Zr = elementosNome('Zr','Zircônio', 40, 91, 5, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2', 'd', 'metal de transição', 'sólido')
Nb = elementosNome('Nb','Nióbio', 41, 93, 5, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4', 'd', 'metal de transição', 'sólido')
Mo = elementosNome('Mo','Molibdênio', 42, 96, 5, 6, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5', 'd', 'metal de transição', 'sólido')
Tc = elementosNome('Tc','Tecnécio', 43, 98, 5, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5', 'd', 'metal de transição', 'sólido')
Ru = elementosNome('Ru','Rutênio', 44, 101, 5, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7', 'd', 'metal de transição', 'sólido')
Rh = elementosNome('Rh','Ródio', 45, 103, 5, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8', 'd', 'metal de transição', 'sólido')
Pd = elementosNome('Pd','Paládio', 46, 106.5, 5, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10', 'd', 'metal de transição', 'sólido')
Ag = elementosNome('Ag','Prata', 47, 108, 5, 11, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10', 'd', 'metal de transição', 'sólido')
Cd = elementosNome('Cd','Cádmio', 48, 112.5, 5, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10', 'd', 'metal de transição', 'sólido')
In = elementosNome('In','Índio', 49, 115, 5, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1', 'p', 'metal pós-transição', 'sólido')
Sn = elementosNome('Sn','Estanho', 50, 119, 5, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2', 'p', 'metal pós-transição', 'sólido')
Sb = elementosNome('Sb','Antimônio', 51, 122, 5, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3', 'p', 'semimetal', 'sólido')
Te = elementosNome('Te','Telúrio', 52, 128, 5, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4', 'p', 'semimetal', 'sólido')
I = elementosNome('I','Iodo', 53, 127, 5, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5', 'p', 'ametal', 'sólido')
Xe = elementosNome('Xe','Xenônio', 54, 131, 5, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6', 'p', 'gás nobre', 'gás')
Cs = elementosNome('Cs','Césio', 55, 133, 6, 1, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1', 's', 'metal alcalino', 'sólido')
Ba = elementosNome('Ba','Bário', 56, 137, 6, 2, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2', 's', 'metal alcalino-terroso', 'sólido')
La = elementosNome('La','Lantânio', 57, 139, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1', 'd', 'lantanídeo', 'sólido')
Ce = elementosNome('Ce','Cério', 58, 140, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1 5d1', 'f', 'lantanídeo', 'sólido')
Pr = elementosNome('Pr','Praseodímio', 59, 141, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3', 'f', 'lantanídeo', 'sólido')
Nd = elementosNome('Nd','Neodímio', 60, 144, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4', 'f', 'lantanídeo', 'sólido')
Pm = elementosNome('Pm','Promécio', 61, 145, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5', 'f', 'lantanídeo', 'sólido')
Sm = elementosNome('Sm','Samário', 62, 150, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6', 'f', 'lantanídeo', 'sólido')
Eu = elementosNome('Eu','Európio', 63, 152, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7', 'f', 'lantanídeo', 'sólido')
Gd = elementosNome('Gd','Gadolínio', 64, 157, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1', 'f', 'lantanídeo', 'sólido')
Tb = elementosNome('Tb','Térbio', 65, 159, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9', 'f', 'lantanídeo', 'sólido')
Dy = elementosNome('Dy','Disprósio', 66, 162.5, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10', 'f', 'lantanídeo', 'sólido')
Ho = elementosNome('Ho','Hólmio', 67, 165, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11', 'f', 'lantanídeo', 'sólido')
Er = elementosNome('Er','Érbio', 68, 167, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12', 'f', 'lantanídeo', 'sólido')
Tm = elementosNome('Tm','Túlio', 69, 169, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13', 'f', 'lantanídeo', 'sólido')
Yb = elementosNome('Yb','Itérbio', 70, 173, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14', 'f', 'lantanídeo', 'sólido')
Lu = elementosNome('Lu','Lutécio', 71, 175, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1', 'd', 'lantanídeo', 'sólido')
Hf = elementosNome('Hf','Háfnio', 72, 178.5, 6, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2', 'd', 'metal de transição', 'sólido')
Ta = elementosNome('Ta','Tântalo', 73, 181, 6, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3', 'd', 'metal de transição', 'sólido')
W = elementosNome('W','Tungstênio', 74, 184, 6, 6, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4', 'd', 'metal de transição', 'sólido')
Re = elementosNome('Re','Rênio', 75, 186, 6, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5', 'd', 'metal de transição', 'sólido')
Os = elementosNome('Os','Ósmio', 76, 190, 6, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6', 'd', 'metal de transição', 'sólido')
Ir = elementosNome('Ir','Irídio', 77, 192, 6, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7', 'd', 'metal de transição', 'sólido')
Pt = elementosNome('Pt','Platina', 78, 195, 6, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9', 'd', 'metal de transição', 'sólido')
Au = elementosNome('Au','Ouro', 79, 197, 6, 11, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10', 'd', 'metal de transição', 'sólido')
Hg = elementosNome('Hg','Mercúrio', 80, 200.5, 6, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10', 'd', 'metal de transição', 'líquido')
Tl = elementosNome('Tl','Tálio', 81, 204, 6, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p1', 'p', 'metal pós-transição', 'sólido')
Pb = elementosNome('Pb','Chumbo', 82, 207, 6, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p2', 'p', 'metal pós-transição', 'sólido')
Bi = elementosNome('Bi','Bismuto', 83, 209, 6, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p3', 'p', 'metal pós-transição', 'sólido')
Po = elementosNome('Po','Polônio', 84, 209, 6, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p4', 'p', 'metal pós-transição', 'sólido')
At = elementosNome('At','Astato', 85, 210, 6, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p5', 'p', 'ametal', 'sólido')
Rn = elementosNome('Rn','Radônio', 86, 222, 6, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6', 'p', 'gás nobre', 'gás')
Fr = elementosNome('Fr','Frâncio', 87, 223, 7, 1, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1', 's', 'metal alcalino', 'sólido')
Ra = elementosNome('Ra','Rádio', 88, 226, 7, 2, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2', 's', 'metal alcalino-terroso', 'sólido')
Ac = elementosNome('Ac','Actínio', 89, 227, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1', 'd', 'actinídeo', 'sólido')
Th = elementosNome('Th','Tório', 90, 232, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2', 'f', 'actinídeo', 'sólido')
Pa = elementosNome('Pa','Protactínio', 91, 231, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f2 6d1', 'f', 'actinídeo', 'sólido')
U = elementosNome('U','Urânio', 92, 238, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f3 6d1', 'f', 'actinídeo', 'sólido')
Np = elementosNome('Np','Netúnio', 93, 237, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4 6d1', 'f', 'actinídeo', 'sólido')
Pu = elementosNome('Pu','Plutônio', 94, 244, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f6', 'f', 'actinídeo', 'sólido')
Am = elementosNome('Am','Amerício', 95, 243, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7', 'f', 'actinídeo', 'sólido')
Cm = elementosNome('Cm','Cúrio', 96, 247, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7 6d1', 'f', 'actinídeo', 'sólido')
Bk = elementosNome('Bk','Berquélio', 97, 247, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f9', 'f', 'actinídeo', 'sólido')
Cf = elementosNome('Cf','Califórnio', 98, 251, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f10', 'f', 'actinídeo', 'sólido')
Es = elementosNome('Es','Einstênio', 99, 252, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f11', 'f', 'actinídeo', 'sólido')
Fm = elementosNome('Fm','Férmio', 100, 257, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f12', 'f', 'actinídeo', 'sólido')
Md = elementosNome('Md','Mendelévio', 101, 258, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f13', 'f', 'actinídeo', 'sólido')
No = elementosNome('No','Nobélio', 102, 259, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14', 'f', 'actinídeo', 'sólido')
Lr = elementosNome('Lr','Laurêncio', 103, 266, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 7p1', 'd', 'actinídeo', 'sólido')
Rf = elementosNome('Rf','Rutherfórdio', 104, 267, 7, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d2', 'd', 'metal de transição', 'sólido')
Db = elementosNome('Db','Dúbnio', 105, 268, 7, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d3', 'd', 'metal de transição', 'sólido')
Sg = elementosNome('Sg','Seabórgio', 106, 269, 7, 6, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d4', 'd', 'metal de transição', 'sólido')
Bh = elementosNome('Bh','Bório', 107, 270, 7, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d5', 'd', 'metal de transição', 'sólido')
Hs = elementosNome('Hs','Hássio', 108, 277, 7, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d6', 'd', 'metal de transição', 'sólido')
Mt = elementosNome('Mt','Meitnério', 109, 278, 7, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d7', 'd', 'metal de transição', 'sólido')
Ds = elementosNome('Ds','Darmstádio', 110, 281, 7, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d8', 'd', 'metal de transição', 'sólido')
Rg = elementosNome('Rg','Roentgênio', 111, 282, 7, 11, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1 5f14 6d10', 'd', 'metal de transição', 'sólido')
Cn = elementosNome('Cn','Copernício', 112, 285, 7, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10', 'd', 'metal de transição', 'sólido')
Nh = elementosNome('Nh','Nihônio', 113, 286, 7, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p1', 'p', 'metal pós-transição', 'sólido')
Fl = elementosNome('Fl','Fleróvio', 114, 289, 7, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p2', 'p', 'metal pós-transição', 'sólido')
Mc = elementosNome('Mc','Moscóvio', 115, 290, 7, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p3', 'p', 'metal pós-transição', 'sólido')
Lv = elementosNome('Lv','Livermório', 116, 293, 7, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p4', 'p', 'metal pós-transição', 'sólido')
Ts = elementosNome('Ts','Tenessino', 117, 294, 7, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p5', 'p', 'metal pós-transição', 'sólido')
Og = elementosNome('Og','Oganessônio', 118, 294, 7, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6', 'p', 'gás nobre', 'gás')



elementos = [H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn, Fr, Ra, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Nh, Fl, Mc, Lv, Ts, Og]






while True:
   

   elemento = input("digite a sigla de algum elemento da tabela periodica: ").capitalize()

   for elementoX in elementos:
    if elementoX.sigla == elemento:
      print(f'seu elemento é o {elementoX.nome}, deseja saber as informações?')
      escolha = input("(s/n): ")
      if escolha == "s":
       print('================')
       print(f" Sigla: {elementoX.sigla} ; \n Nome: {elementoX.nome} ; \n Número atômico: {elementoX.atomicidade} ; \n Massa: {elementoX.massa} ; \n Período: {elementoX.periodo} ; \n Família: {elementoX.familia} ; \n Distribuição eletrônica: {elementoX.distribuicao} ; \n Bloco: {elementoX.bloco} ; \n Classificação: {elementoX.classificacao} ; \n Estado físico: {elementoX.estado} .")
       print('================')

      break 
   else:
      print('sua sigla nao foi encontrada')
   continuar = input('quer consultar outro elemento? (s/n):')
   if continuar == 'n':
     break
        
   
            
