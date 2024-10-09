for c in range(1, 6):
    p = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if c == 1:
        pma = p
        pme = p
    else:
        if p > pma:
            pma = p
        elif p < pme:
            pme = p

print('O maior peso digitado foi: {}'.format(pma))
print('O menor peso digitado foi: {}'.format(pme))


