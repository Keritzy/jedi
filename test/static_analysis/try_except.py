try:
    #! attribute-error
    str.not_existing
except TypeError:
    pass

try:
    str.not_existing
except AttributeError:
    #! attribute-error
    str.not_existing
    pass

try:
    import not_existing_import
except ImportError:
    pass
try:
    #! import-error
    import not_existing_import
except AttributeError:
    pass

# -----------------
# detailed except
# -----------------
try:
    str.not_existing
except ((AttributeError)): pass
try:
    #! attribute-error
    str.not_existing
except [AttributeError]: pass
