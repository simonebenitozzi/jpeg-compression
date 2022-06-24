from numpy import ndarray
from scipy.fftpack import dctn, idctn


class Compression:
    """
    Per ogni blocco f eseguire le seguenti operazioni: - applicare la DCT2 (della libreria): c = DCT2(f); - eliminare
    le frequenze clk con k + l ≥ d (sto assumendo che le frequenze partano da 0: se d = 0 le elimino tutte,
    se d = (2F − 2) elimino solo la più alta, cio`e quella con k = F − 1, ‘ = F − 1). - applicare la DCT2 inversa
    all’array c cos`ı modificato: ff = IDCT2(c); - arrotondare ff all’intero pi`u vicino, mettere a zero i valori
    negativi e a 255 quelli maggiori di 255 in modo da avere dei valori ammissibili (1 byte);
    """

    def __init__(self, matrix_list: list[ndarray], d: int):
        self.__matrix_list = matrix_list
        self.__d = d

    def start(self) -> list[ndarray]:
        compressed_matrix_list: list[ndarray] = []
        for matrix in self.__matrix_list:
            c = self.dct2(matrix)
            c = self.remove_frequencies(c)
            ff = self.idct2(c)
            ff = self.round(ff)
            compressed_matrix_list.append(ff)

        return compressed_matrix_list

    def dct2(self, matrix: ndarray) -> ndarray:
        """
        applicare la DCT2 (della libreria): c = DCT2(f);

        :param matrix:
        :return:
        """
        return dctn(matrix, norm='ortho')

    def remove_frequencies(self, c: ndarray) -> ndarray:
        """
        Eliminare le frequenze clk con k + l ≥ d (sto assumendo che le frequenze partano da 0: se d = 0 le elimino
        tutte, se d = (2F − 2) elimino solo la più alta, cio`e quella con k = F − 1, ‘ = F − 1).

        :param c:
        :return:
        """

        for k in range(len(c)):
            for l in range(len(c[k])):
                if k + l >= self.__d:
                    c[k][l] = 0

        return c

    def idct2(self, c: ndarray) -> ndarray:
        """
        Applicare la DCT2 inversa all’array c così modificato: ff = IDCT2(c);
        :param c:
        :return:
        """

        return idctn(c, norm='ortho')

    def round(self, ff: ndarray) -> ndarray:
        """
        Arrotondare ff all’intero pi`u vicino, mettere a zero i valori negativi e a 255
        quelli maggiori di 255 in modo da avere dei valori ammissibili (1 byte);
        :param ff:
        :return:
        """

        ff[ff < 0] = 0
        ff[ff > 255] = 255
        return ff.astype(int)
