# kt-cambio
Conversor de moedas.  
  
## Pré-requisitos
  Python instalado e disponível no terminal de comandos.  
    
## Instalação
```cmd
pip install kt-cambio
```

## Uso

```cmd
brlusd [--cambio <CAMBIO>] <REAL>
```
Onde:  
REAL Valor em real.  
--cambio, -c Càmbio do dólar.  
Exemplo:  
```cmd
brlusd 5000.00
909.09
```
  
```cmd
usdbrl [--cambio <CAMBIO>] <DOLAR>
```
Onde:  
DOLAR Valor em dólar.  
--cambio, -c Càmbio do dólar.  
Exemplo:  
```cmd
usdbrl 909.09
4999.99
```
