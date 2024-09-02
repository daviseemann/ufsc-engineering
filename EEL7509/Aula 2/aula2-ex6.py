# %%
listapredefinida = list(range(1_000_000_000))

# %%
%%timeit
# Eager evaluation da soma dos quadrados de uma lista:
quadrados = [x**2 for x in listapredefinida]
somaquads = sum(quadrados)
# %%
%%timeit
# Lazy evaluation da soma dos quadrados de uma lista:
quadrados = (x**2 for x in listapredefinida)
somaquads = sum(quadrados)
