from uyghur_toolkit.processing.ProcesType import ProcesType
from uyghur_toolkit.processing.conversion.UEYConversionStrategy import UEYConversionStrategy


if __name__ == '__main__':

    uey_proces=(UEYConversionStrategy()
                .addConvertionOption(ProcesType.NORMALIZATION)
                .addConvertionOption(ProcesType.NUMBER)
                .addConvertionOption(ProcesType.SYMBOL)
    .addConvertionOption(ProcesType.SYLLABLES)
                .addConvertionOption(ProcesType.NORMALIZATION | ProcesType.REVERSE)
                )
    for text in uey_texts:
        print(uey_proces.convert(text))
