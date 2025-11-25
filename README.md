<div align="center">
  <a href="#-ouroboros-or---python-done-right">🇺🇸 English</a> |
  <a href="#-ouroboros-or---python-feito-do-jeito-certo">🇧🇷 Português</a>
</div>

---

<div id="english"></div>

# 🐍 Ouroboros (.or) - Python, Done Right.

> *"Because significant indentation was the biggest bullshit ever told in the history of Computing."*

## What is this?

You love Python. It has libraries for everything. It's readable. It's powerful. But it has one fatal flaw: **It trusts that you know how to count invisible spaces.**

**Ouroboros** is a conceptual fork (read: a glorified wrapper) that fixes Python's biggest design error. We bring back sanity. We bring back structure.

If you've ever copied code from StackOverflow, pasted it into your project, and spent 20 minutes trying to figure out why the `else` wasn't firing only to realize you were missing **one damn space**... Welcome to Ouroboros.

## The Problem (A.K.A. "Pure" Python)

In Python, this is a fatal error:

```python
def save_the_world():
    if hero_arrived:
      defeat_villain() # Oops! 2 spaces instead of 4. The world ended.
The Python interpreter looks at this and says: IndentationError: unindent does not match any outer indentation level. Translation: "I didn't like the aesthetics of your text, so I refuse to work, blah blah blah."
```

### The Ouroboros Solution
In Ouroboros, the interpreter can go screw itself. We use explicit delimiters.

```Python

def save_the_world():
print("Indentation? Who cares?")
if hero_arrived:
defeat_villain()
end # The block ended HERE. Period.
end # End of function. Peace.
```
Ouroboros reads this "spaghetti", adds our special seasoning, and converts it into the fresh Python that the machine demands.

## Features
Paste-Proof Syntax: Copy code from anywhere. Paste it however you want. Just don't forget the end, dammit.

100% Compatibility: Runs Pandas, Numpy, Django, and any other library.

Auto Formatter: Did you write everything left-aligned like a caveman? Run ouroboros format and it fixes the indentation for you without nagging.

End of the Tabs vs. Spaces War: Use tabs. Use spaces. Use a profane mixture of both. Ouroboros doesn't judge. It just executes.

## How to Use
1. Installation (Simple, because we are lazy, and frankly I did this with AI)
Drop the ouroboros.py file into the root of your project. Done. You have installed the compiler. Congratulations, engineer.

2. Running a script
Forget python script.py. You are part of the cult now.

```Bash

# Runs your superior code
python ouroboros.py run my_beautiful_code.or
```
3. The Formatter Magic
You wrote this (your eyes bleed, but the logic is there):

```Python

# file: chaos.or
if x > 10:
print("Greater")
else:
print("Smaller")
end
```
Run the sacred command:

```Bash

python ouroboros.py format chaos.or
```
And voilà, the file is rewritten with correct indentation, ready to be read by humans or people with OCD.

## FAQ (Frequently Annoying Questions)
Q: Isn't this just Ruby with extra steps? A: Yes. Next question.

Q: Why not just learn to indent properly? A: Try refactoring "Cowboy Code" (spaghetti code), removing unnecessary loops and nesting hell, and then come back to talk to me.

Q: Will this make my code slower? A: It adds about 0.0001ms to translate the file before running. If that's a problem for you, go code in Assembly and stop bugging me.

Q: What happens if I forget an end? A: The same thing that happens if you forget to close a parenthesis in C or Java. The code breaks. But at least you know where.

## License
MIT License (But if you mix Tabs and Spaces in the final generated code, the license is revoked and you will be cursed).

Made with pure hatred for IndentationError.

<div align="right"> <a href="#-ouroboros-or---python-done-right">⬆ Back to Top</a> </div>

<div id="portugues"></div>

# 🐍 Ouroboros (.or) - Python, feito do jeito certo.
"Porque indentação significativa foi a maior bullshit que já contaram na história da Computação."

## O que é isso?
Você ama Python. Ele tem bibliotecas para tudo. Ele é legível. Ele é poderoso. Mas ele tem um defeito fatal: Ele confia que você sabe contar espaços invisíveis.

Ouroboros é um fork conceitual (leia-se: um wrapper glorificado) que corrige o maior erro de design do Python. Nós trazemos de volta a sanidade. Nós trazemos de volta a estrutura.

Se você já copiou um código do StackOverflow, colou no seu projeto e passou 20 minutos tentando descobrir por que o else não estava funcionando só para perceber que faltava um espaço maldito... Bem-vindo ao Ouroboros.

## O Problema (A.K.A. Python "Puro")
Em Python, isso é um erro fatal:

```Python

def salvar_mundo():
    if heroi_chegou:
      derrotar_vilao() # Ops! 2 espaços em vez de 4. O mundo acabou.
```
O interpretador do Python olha para isso e diz: IndentationError: unindent does not match any outer indentation level. Tradução: "Eu não gostei da estética do seu texto, então me recuso a trabalhar, blá blá blá."

### A Solução Ouroboros
No Ouroboros, o interpretador que se exploda. Nós usamos delimitadores explícitos.

```Python

def salvar_mundo():
print("Indentação? Quem liga?")
if heroi_chegou:
derrotar_vilao()
end # O bloco acabou AQUI. Ponto final.
end # Fim da função. Peace.
```
O Ouroboros lê essa "macarronada", adiciona nosso tempero, e converte para o fresco do Python.

## Funcionalidades
Sintaxe à prova de "Colar": Copie código de qualquer lugar. Cole de qualquer jeito. Não esqueça o end, porra.

Compatibilidade 100%: Roda Pandas, Numpy, Django, e qualquer outra biblioteca.

Formatador Automático: Escreveu tudo alinhado à esquerda como um homem das cavernas? Rode ouroboros format e ele arruma a indentação para você sem te encher o saco.

Fim da Guerra Tabs vs. Spaces: Use tabs. Use espaços. Use uma mistura profana dos dois. O Ouroboros não julga. Ele apenas executa.

## Como Usar
1. Instalação (Simples, porque somos preguiçosos, e sem tempo aliás fiz isso com IA)
Jogue o arquivo ouroboros.py na raiz do seu projeto. Pronto. Você instalou o compilador. Parabéns, engenheiro.

2. Rodando um script
Esqueça o python script.py. Agora você é parte da seita.

```Bash

# Executa seu código superior
python ouroboros.py run meu_codigo_lindo.or
```
3. A Mágica do Formatador
Você escreveu isso (seus olhos sangram, mas a lógica está lá):

```Python
# arquivo: caos.or
if x > 10:
print("Maior")
else:
print("Menor")
end
```
Rode o comando sagrado:

```Bash

python ouroboros.py format caos.or
```
E voilà, o arquivo é reescrito indentado corretamente, pronto para ser lido por seres humanos ou pessoas com TOC.

## FAQ (Perguntas Frequentemente Irritantes)
P: Isso não é apenas Ruby com passos extras? R: Sim. Próxima pergunta.

P: Por que não aprender a indentar direito? R: Experimente refatorar o código feito a Go Horse, removendo laços desnecessários, e voltamos a conversar.

P: Isso vai deixar meu código mais lento? R: Adiciona cerca de 0.0001ms para traduzir o arquivo antes de rodar. Se isso é um problema para você, vá programar em Assembly e pare de me encher.

P: O que acontece se eu esquecer um end? R: O mesmo que acontece se você esquecer de fechar um parênteses em C ou Java. O código quebra. Mas pelo menos você sabe onde.

## Licença
MIT License (Mas se você usar Tabs misturados com Espaços no código final gerado, a licença é revogada e você será amaldiçoado).

Feito com ódio aos IndentationError.

<div align="right"> <a href="#-ouroboros-or---python-feito-do-jeito-certo">⬆ Voltar ao Topo</a> </div>
