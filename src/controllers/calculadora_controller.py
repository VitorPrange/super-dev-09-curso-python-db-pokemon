from fastapi import APIRouter


router = APIRouter()


@router.get("/mensagem")
def mensagem():
    """Rota para uma mensagem de boas vindas"""
    return {"mensagem": "Olá mundo"}


@router.get("/calculadora/somar")
def somar(numero1: int, numero2: int):
    soma = numero1 + numero2
    return{
        "resultado": soma
    }


@router.get("/calculadora/imc")
def calcular_imc(peso:float, altura:float):
    imc = peso / altura ** 2

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    return {
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }


@router.get("/concatenar")
def concatenar(nome: str, sobrenome: str):

    return{
        "nome_completo": f"{nome} {sobrenome}"
    }


@router.get("/calcular/desconto")
def calcular_desconto(preco: float, percentual: int):
    valor_desconto = preco * (percentual / 100)
    preco_final = preco - valor_desconto
    return {
        "preco": preco,
        "percentual": percentual,
        "valor_do_desconto": valor_desconto,
        "valor_com_desconto": preco_final
    }


@router.get("/calcular/media")
def calcular_media(nota1: float, nota2: float, nota3: float, nota4: float):
    media = ((nota1 + nota2 + nota3 + nota4) / 4)

    return{
        "nota_1": nota1,
        "nota_2": nota2,
        "nota_3": nota3,
        "nota_4": nota4,
        "media": media
    }