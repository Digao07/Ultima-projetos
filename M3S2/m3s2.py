def decorator_imprimir(funcao):
    def imprimir(*args, **kwargs):
        capital, taxa, tempo = args
        resultado = funcao(*args, **kwargs)

        return print(f"CAPITAL: {capital}, TAXA: {taxa}, TEMPO: {tempo}, RESULTADO: {resultado}")
    return imprimir

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_simples(capital, taxa,tempo)