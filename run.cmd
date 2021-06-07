@echo OFF

if %1.==. (
    echo You must specify at least one positional argument.
) else (
    python -m todolist_backend %*
)

@echo ON