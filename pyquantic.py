class elementosNome:
    def __init__(self, nome, atomicidade, massa, periodo, familia, distribuicao, bloco, classificacao, estado):
        self.nome = nome
        self.atomicidade = atomicidade
        self.massa = massa
        self.periodo = periodo
        self.familia = familia
        self.distribuicao = distribuicao
        self.bloco = bloco
 
H = elementosNome('Hidrogênio', 1, 1, 1, 1, '1s¹', 's', 'ametal', 'gás')
He = elementosNome('Hélio',2, 4, 1, 18, '1s²', 's', 'gás nobre', 'gás')
Li = elementosNome('Lítio', 3, 7, 2, 1, '1s² 2s¹', 's', 'metal alcalino', 'sólido')
Be = elementosNome('Berílio', 4, 9, 2, 2, '1s2 2s2', 's', 'metal alcalino-terroso', 'sólido')
B = elementosNome('Boro', 5, 11, 2, 13, '1s2 2s2 2p1', 'p', 'semimetal', 'sólido')
C = elementosNome('Carbono', 6, 12, 2, 14, '1s2 2s2 2p2', 'p', 'ametal', 'sólido')
N = elementosNome('Nitrogênio', 7, 14, 2, 15, '1s2 2s2 2p3', 'p', 'ametal', 'gás')
O = elementosNome('Oxigênio', 8, 16, 2, 16, '1s2 2s2 2p4', 'p', 'ametal', 'gás')
F = elementosNome('Flúor', 9, 19, 2, 17, '1s2 2s2 2p5', 'p', 'ametal', 'gás')
Ne = elementosNome('Neônio', 10, 20, 2, 18, '1s2 2s2 2p6', 'p', 'gás nobre', 'gás')
Na = elementosNome('Sódio', 11, 23, 3, 1, '1s2 2s2 2p6 3s1', 's', 'metal alcalino', 'sólido')
Mg = elementosNome('Magnésio', 12, 24, 3, 2, '1s2 2s2 2p6 3s2', 's', 'metal alcalino-terroso', 'sólido')
Al = elementosNome('Alumínio', 13, 27, 3, 13, '1s2 2s2 2p6 3s2 3p1', 'p', 'metal pós-transição', 'sólido')
Si = elementosNome('Silício', 14, 28, 3, 14, '1s2 2s2 2p6 3s2 3p2', 'p', 'semimetal', 'sólido')
P = elementosNome('Fósforo', 15, 31, 3, 15, '1s2 2s2 2p6 3s2 3p3', 'p', 'ametal', 'sólido')
S = elementosNome('Enxofre', 16, 32, 3, 16, '1s2 2s2 2p6 3s2 3p4', 'p', 'ametal', 'sólido')
Cl = elementosNome('Cloro', 17, 35.5, 3, 17, '1s2 2s2 2p6 3s2 3p5', 'p', 'ametal', 'gás')
Ar = elementosNome('Argônio', 18, 40, 3, 18, '1s2 2s2 2p6 3s2 3p6', 'p', 'gás nobre', 'gás')
K = elementosNome('Potássio', 19, 39, 4, 1, '1s2 2s2 2p6 3s2 3p6 4s1', 's', 'metal alcalino', 'sólido')
Ca = elementosNome('Cálcio', 20, 40, 4, 2, '1s2 2s2 2p6 3s2 3p6 4s2', 's', 'metal alcalino-terroso', 'sólido')
Sc = elementosNome('Escândio', 21, 45, 4, 3, '1s2 2s2 2p6 3s2 3p6 4s2 3d1', 'd', 'metal de transição', 'sólido')
Ti = elementosNome('Titânio', 22, 48, 4, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d2', 'd', 'metal de transição', 'sólido')
V = elementosNome('Vanádio', 23, 51, 4, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d3', 'd', 'metal de transição', 'sólido')
Cr = elementosNome('Cromo', 24, 52, 4, 6, '1s2 2s2 2p6 3s2 3p6 4s1 3d5', 'd', 'metal de transição', 'sólido')
Mn = elementosNome('Manganês', 25, 55, 4, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d5', 'd', 'metal de transição', 'sólido')
Fe = elementosNome('Ferro', 26, 56, 4, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d6', 'd', 'metal de transição', 'sólido')
Co = elementosNome('Cobalto', 27, 59, 4, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d7', 'd', 'metal de transição', 'sólido')
Ni = elementosNome('Níquel', 28, 59, 4, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d8', 'd', 'metal de transição', 'sólido')
Cu = elementosNome('Cobre', 29, 63.5, 4, 11, '1s2 2s2 2p6 3s2 3p6 4s1 3d10', 'd', 'metal de transição', 'sólido')
Zn = elementosNome('Zinco', 30, 65, 4, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10', 'd', 'metal de transição', 'sólido')
Ga = elementosNome('Gálio', 31, 70, 4, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1', 'p', 'metal pós-transição', 'sólido')
Ge = elementosNome('Germânio', 32, 73, 4, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2', 'p', 'semimetal', 'sólido')
As = elementosNome('Arsênio', 33, 75, 4, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3', 'p', 'semimetal', 'sólido')
Se = elementosNome('Selênio', 34, 79, 4, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4', 'p', 'ametal', 'sólido')
Br = elementosNome('Bromo', 35, 80, 4, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5', 'p', 'ametal', 'líquido')
Kr = elementosNome('Criptônio', 36, 84, 4, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6', 'p', 'gás nobre', 'gás')
Rb = elementosNome('Rubídio', 37, 85.5, 5, 1, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1', 's', 'metal alcalino', 'sólido')
Sr = elementosNome('Estrôncio', 38, 88, 5, 2, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2', 's', 'metal alcalino-terroso', 'sólido')
Y = elementosNome('Ítrio', 39, 89, 5, 3, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1', 'd', 'metal de transição', 'sólido')
Zr = elementosNome('Zircônio', 40, 91, 5, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2', 'd', 'metal de transição', 'sólido')
Nb = elementosNome('Nióbio', 41, 93, 5, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4', 'd', 'metal de transição', 'sólido')
Mo = elementosNome('Molibdênio', 42, 96, 5, 6, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5', 'd', 'metal de transição', 'sólido')
Tc = elementosNome('Tecnécio', 43, 98, 5, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5', 'd', 'metal de transição', 'sólido')
Ru = elementosNome('Rutênio', 44, 101, 5, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7', 'd', 'metal de transição', 'sólido')
Rh = elementosNome('Ródio', 45, 103, 5, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8', 'd', 'metal de transição', 'sólido')
Pd = elementosNome('Paládio', 46, 106.5, 5, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 4d10', 'd', 'metal de transição', 'sólido')
Ag = elementosNome('Prata', 47, 108, 5, 11, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10', 'd', 'metal de transição', 'sólido')
Cd = elementosNome('Cádmio', 48, 112.5, 5, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10', 'd', 'metal de transição', 'sólido')
In = elementosNome('Índio', 49, 115, 5, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1', 'p', 'metal pós-transição', 'sólido')
Sn = elementosNome('Estanho', 50, 119, 5, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2', 'p', 'metal pós-transição', 'sólido')
Sb = elementosNome('Antimônio', 51, 122, 5, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3', 'p', 'semimetal', 'sólido')
Te = elementosNome('Telúrio', 52, 128, 5, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4', 'p', 'semimetal', 'sólido')
I = elementosNome('Iodo', 53, 127, 5, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5', 'p', 'ametal', 'sólido')
Xe = elementosNome('Xenônio', 54, 131, 5, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6', 'p', 'gás nobre', 'gás')
Cs = elementosNome('Césio', 55, 133, 6, 1, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1', 's', 'metal alcalino', 'sólido')
Ba = elementosNome('Bário', 56, 137, 6, 2, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2', 's', 'metal alcalino-terroso', 'sólido')
La = elementosNome('Lantânio', 57, 139, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1', 'd', 'lantanídeo', 'sólido')
Ce = elementosNome('Cério', 58, 140, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1 5d1', 'f', 'lantanídeo', 'sólido')
Pr = elementosNome('Praseodímio', 59, 141, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3', 'f', 'lantanídeo', 'sólido')
Nd = elementosNome('Neodímio', 60, 144, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4', 'f', 'lantanídeo', 'sólido')
Pm = elementosNome('Promécio', 61, 145, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5', 'f', 'lantanídeo', 'sólido')
Sm = elementosNome('Samário', 62, 150, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6', 'f', 'lantanídeo', 'sólido')
Eu = elementosNome('Európio', 63, 152, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7', 'f', 'lantanídeo', 'sólido')
Gd = elementosNome('Gadolínio', 64, 157, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1', 'f', 'lantanídeo', 'sólido')
Tb = elementosNome('Térbio', 65, 159, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9', 'f', 'lantanídeo', 'sólido')
Dy = elementosNome('Disprósio', 66, 162.5, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10', 'f', 'lantanídeo', 'sólido')
Ho = elementosNome('Hólmio', 67, 165, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11', 'f', 'lantanídeo', 'sólido')
Er = elementosNome('Érbio', 68, 167, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12', 'f', 'lantanídeo', 'sólido')
Tm = elementosNome('Túlio', 69, 169, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13', 'f', 'lantanídeo', 'sólido')
Yb = elementosNome('Itérbio', 70, 173, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14', 'f', 'lantanídeo', 'sólido')
Lu = elementosNome('Lutécio', 71, 175, 6, 'Lantânidas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1', 'd', 'lantanídeo', 'sólido')
Hf = elementosNome('Háfnio', 72, 178.5, 6, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2', 'd', 'metal de transição', 'sólido')
Ta = elementosNome('Tântalo', 73, 181, 6, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3', 'd', 'metal de transição', 'sólido')
W = elementosNome('Tungstênio', 74, 184, 6, 6, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4', 'd', 'metal de transição', 'sólido')
Re = elementosNome('Rênio', 75, 186, 6, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5', 'd', 'metal de transição', 'sólido')
Os = elementosNome('Ósmio', 76, 190, 6, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6', 'd', 'metal de transição', 'sólido')
Ir = elementosNome('Irídio', 77, 192, 6, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7', 'd', 'metal de transição', 'sólido')
Pt = elementosNome('Platina', 78, 195, 6, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d9', 'd', 'metal de transição', 'sólido')
Au = elementosNome('Ouro', 79, 197, 6, 11, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1 4f14 5d10', 'd', 'metal de transição', 'sólido')
Hg = elementosNome('Mercúrio', 80, 200.5, 6, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10', 'd', 'metal de transição', 'líquido')
Tl = elementosNome('Tálio', 81, 204, 6, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p1', 'p', 'metal pós-transição', 'sólido')
Pb = elementosNome('Chumbo', 82, 207, 6, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p2', 'p', 'metal pós-transição', 'sólido')
Bi = elementosNome('Bismuto', 83, 209, 6, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p3', 'p', 'metal pós-transição', 'sólido')
Po = elementosNome('Polônio', 84, 209, 6, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p4', 'p', 'metal pós-transição', 'sólido')
At = elementosNome('Astato', 85, 210, 6, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p5', 'p', 'ametal', 'sólido')
Rn = elementosNome('Radônio', 86, 222, 6, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6', 'p', 'gás nobre', 'gás')
Fr = elementosNome('Frâncio', 87, 223, 7, 1, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1', 's', 'metal alcalino', 'sólido')
Ra = elementosNome('Rádio', 88, 226, 7, 2, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2', 's', 'metal alcalino-terroso', 'sólido')
Ac = elementosNome('Actínio', 89, 227, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d1', 'd', 'actinídeo', 'sólido')
Th = elementosNome('Tório', 90, 232, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 6d2', 'f', 'actinídeo', 'sólido')
Pa = elementosNome('Protactínio', 91, 231, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f2 6d1', 'f', 'actinídeo', 'sólido')
U = elementosNome('Urânio', 92, 238, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f3 6d1', 'f', 'actinídeo', 'sólido')
Np = elementosNome('Netúnio', 93, 237, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f4 6d1', 'f', 'actinídeo', 'sólido')
Pu = elementosNome('Plutônio', 94, 244, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f6', 'f', 'actinídeo', 'sólido')
Am = elementosNome('Amerício', 95, 243, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7', 'f', 'actinídeo', 'sólido')
Cm = elementosNome('Cúrio', 96, 247, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f7 6d1', 'f', 'actinídeo', 'sólido')
Bk = elementosNome('Berquélio', 97, 247, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f9', 'f', 'actinídeo', 'sólido')
Cf = elementosNome('Califórnio', 98, 251, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f10', 'f', 'actinídeo', 'sólido')
Es = elementosNome('Einstênio', 99, 252, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f11', 'f', 'actinídeo', 'sólido')
Fm = elementosNome('Férmio', 100, 257, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f12', 'f', 'actinídeo', 'sólido')
Md = elementosNome('Mendelévio', 101, 258, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f13', 'f', 'actinídeo', 'sólido')
No = elementosNome('Nobélio', 102, 259, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14', 'f', 'actinídeo', 'sólido')
Lr = elementosNome('Laurêncio', 103, 266, 7, 'Actinídas', '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 7p1', 'd', 'actinídeo', 'sólido')
Rf = elementosNome('Rutherfórdio', 104, 267, 7, 4, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d2', 'd', 'metal de transição', 'sólido')
Db = elementosNome('Dúbnio', 105, 268, 7, 5, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d3', 'd', 'metal de transição', 'sólido')
Sg = elementosNome('Seabórgio', 106, 269, 7, 6, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d4', 'd', 'metal de transição', 'sólido')
Bh = elementosNome('Bório', 107, 270, 7, 7, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d5', 'd', 'metal de transição', 'sólido')
Hs = elementosNome('Hássio', 108, 277, 7, 8, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d6', 'd', 'metal de transição', 'sólido')
Mt = elementosNome('Meitnério', 109, 278, 7, 9, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d7', 'd', 'metal de transição', 'sólido')
Ds = elementosNome('Darmstádio', 110, 281, 7, 10, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d8', 'd', 'metal de transição', 'sólido')
Rg = elementosNome('Roentgênio', 111, 282, 7, 11, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s1 5f14 6d10', 'd', 'metal de transição', 'sólido')
Cn = elementosNome('Copernício', 112, 285, 7, 12, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10', 'd', 'metal de transição', 'sólido')
Nh = elementosNome('Nihônio', 113, 286, 7, 13, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p1', 'p', 'metal pós-transição', 'sólido')
Fl = elementosNome('Fleróvio', 114, 289, 7, 14, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p2', 'p', 'metal pós-transição', 'sólido')
Mc = elementosNome('Moscóvio', 115, 290, 7, 15, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p3', 'p', 'metal pós-transição', 'sólido')
Lv = elementosNome('Livermório', 116, 293, 7, 16, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p4', 'p', 'metal pós-transição', 'sólido')
Ts = elementosNome('Tenessino', 117, 294, 7, 17, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p5', 'p', 'metal pós-transição', 'sólido')
Og = elementosNome('Oganessônio', 118, 294, 7, 18, '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6 7s2 5f14 6d10 7p6', 'p', 'gás nobre', 'gás')











elemento = input("digite a sigla de algum elemento da tabela periodica: ").capitalize()
if elemento == "H":
    print("seu elemento é o hidrogênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("seu elemento tem 1 de número atômico.")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Mg":
    print("seu elemento é o magnésio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("Seu elemento tem 12 de número atômico.")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Li":
    print("seu elemento é o lítio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("seu elemento tem 3 de número atômico.")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Na":
    print("seu elemento é o sódio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("Seu elemento tem 11 de número atômico.")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "K":
    print("seu elemento é o potássio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Rb":
    print("seu elemento é o rubídio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cs":
    print("seu elemento é o césio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Fr":
    print("seu elemento é o frâncio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Be":
    print("seu elemento é o Berílio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ca":
    print("seu elemento é o Cálcio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Sr":
    print("seu elemento é o Estrôncio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ba":
    print("seu elemento é o Bário, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ra":
    print("seu elemento é o Rádio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Sc":
    print("seu elemento é o Escândio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Y":
    print("seu elemento é o Ítrio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ti":
    print("seu elemento é o Titânio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Zr":
    print("seu elemento é o Zircônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Hf":
    print("seu elemento é o Háfnio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Rf":
    print("seu elemento é o Rutherfórdio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "V":
    print("seu elemento é o Vanádio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Nb":
    print("seu elemento é o Nióbio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ta":
    print("seu elemento é o Tântalo, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Db":
    print("seu elemento é o Dúbnio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cr":
    print("seu elemento é o Cromo, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Mo":
    print("seu elemento é o Moblidênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "W":
    print("seu elemento é o Tungstênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Sg":
    print("seu elemento é o Seabórgio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Mn":
    print("seu elemento é o Mangânes, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Tc":
    print("seu elemento é o Tecnécio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Re":
    print("seu elemento é o Rênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Bh":
    print("seu elemento é o Bóhrio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Fe":
    print("seu elemento é o Ferro, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ru":
    print("seu elemento é o Rutênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Os":
    print("seu elemento é o Ósmio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Hs":
    print("seu elemento é o Hássio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Co":
    print("seu elemento é o Cobalto, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Rh":
    print("seu elemento é o Ródio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ir":
    print("seu elemento é o Irídio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Mt":
    print("seu elemento é o Meitnério, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ni":
    print("seu elemento é o Níquel, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pd":
    print("seu elemento é o Paládio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pt":
    print("seu elemento é o Platina, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ds":
    print("seu elemento é o Darmstádio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cu":
    print("seu elemento é o Cobre, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ag":
    print("seu elemento é o Prata, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Au":
    print("seu elemento é o Ouro, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Rg":
    print("seu elemento é o Roentgênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Zn":
    print("seu elemento é o Zinco, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cd":
    print("seu elemento é o Cádmio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Hg":
    print("seu elemento é o Mercúrio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cn":
    print("seu elemento é o Copernício, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "B":
    print("seu elemento é o Boro, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Al":
    print("seu elemento é o Alumínio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ga":
    print("seu elemento é o Gálio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "In":
    print("seu elemento é o Índio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Tl":
    print("seu elemento é o Tálio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Nh":
    print("seu elemento é o Nihônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "C":
    print("seu elemento é o Carbono, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Si":
    print("seu elemento é o Silício, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ge":
    print("seu elemento é o Germânio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Sn":
    print("seu elemento é o Estanho, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pb":
    print("seu elemento é o Chumbo, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Fl":
    print("seu elemento é o Fleróvio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "N":
    print("seu elemento é o Nitrogênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "P":
    print("seu elemento é o Fósforo, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "As":
    print("seu elemento é o Arsênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Sb":
    print("seu elemento é o Antimônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Bi":
    print("seu elemento é o Bismuto, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Mc":
    print("seu elemento é o Moscóvio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")


elif elemento == "O":
    print("seu elemento é o Oxigênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "S":
    print("seu elemento é o Enxofre, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Se":
    print("seu elemento é o Selênio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Te":
    print("seu elemento é o Telúrio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Po":
    print("seu elemento é o Polônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Lv":
    print("seu elemento é o Livermório, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "F":
    print("seu elemento é o Flúor, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cl":
    print("seu elemento é o Cloro, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Br":
    print("seu elemento é o Bromo, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "I":
    print("seu elemento é Iodo, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "At":
    print("seu elemento é o Ástato, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ts":
    print("seu elemento é o Tenessino, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "He":
    print("seu elemento é o Hélio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ne":
    print("seu elemento é o Neônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ar":
    print("seu elemento é o Argônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Kr":
    print("seu elemento é o Criptônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Xe":
    print("seu elemento é o Xenônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Rn":
    print("seu elemento é o Radônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Og":
    print("seu elemento é o Oganessônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "La":
    print("seu elemento é o Lântanio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ce":
    print("seu elemento é o Cério, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pr":
    print("seu elemento é o Praseodímio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Nd":
    print("seu elemento é o Neodímio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pm":
    print("seu elemento é o Promécio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Sm":
    print("seu elemento é o Samário, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Eu":
    print("seu elemento é o Európio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Gd":
    print("seu elemento é o Gadolínio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Tb":
    print("seu elemento é o Térbio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Dy":
    print("seu elemento é o Disprósio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ho":
    print("seu elemento é o Hólmio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Er":
    print("seu elemento é o Érbio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Tm":
    print("seu elemento é o Túlio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Yb":
    print("seu elemento é o Itérbio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Lu":
    print("seu elemento é o Lutécio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Ac":
    print("seu elemento é o Actínio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Th":
    print("seu elemento é o Tório, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pa":
    print("seu elemento é o Protactínio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "U":
    print("seu elemento é o Urânio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Np":
    print("seu elemento é o Netúnio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Pu":
    print("seu elemento é o Plutônio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Am":
    print("seu elemento é o Amerício, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cm":
    print("seu elemento é o Cúrio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Bk":
    print("seu elemento é o Berquélio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Cf":
    print("seu elemento é o Califórnio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Es":
    print("seu elemento é o Einsténio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Fm":
    print("seu elemento é o Férmio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Md":
    print("seu elemento é o Mendelévio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "No":
    print("seu elemento é Nobélio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")

elif elemento == "Lr":
    print("seu elemento é o Laurêncio, deseja saber as informações?")
    escolha = input("(s/n): ")
    if escolha == "s":
        print("substituir")
    else:
        print("Obrigada! reinicie o código para escrever outro elemento.")
else:
    print("Não encontramos seu elemento, sentimos muito!")

lista = ['Massa', 'Nêutrons']
pergunta = input('quer fazer uma conta? escolha o que quer descobrir: Massa/Nêutrons: ').capitalize()
if pergunta == 'Massa':
        print('a fórmula para saber a massa é: P(prótons) + N(Nêutrons)! Nesse caso vamos fazer juntos: ')
        proton = int(input(f'digite a quantidade de prótons do elemento {elemento}:(ps: informamos ele acima!) '))
        neutron = int(input (f'digite a quantidade de Nêutrons do elemento {elemento}: '))
        resultado = proton + neutron
        print('o número de massa é: ', resultado)
        
elif pergunta == 'Nêutrons':
        print('a fórmula para saber a quantidade de Nêutrons é: A(Massa) - P(Prótons)! Nesse caso vamos fazer juntos: ')
        massa = int(input(f'digite a Massa do elemento {elemento}: (ps: informamos ele acima!)'))
        proton = int(input(f'digite a quantidade de prótons do elemento {elemento}: '))
        resultado = massa - proton
        print('a quantidade de Nêutrons é: ', resultado)

else: 
        print('Porfavor, reinicie o código e escreva um dos fatores!')

